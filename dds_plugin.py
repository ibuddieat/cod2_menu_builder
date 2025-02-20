"""
A Pillow loader for some .dds files
Jerome Leclanche <jerome@leclan.ch>
Documentation:
  http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_compression_s3tc.txt
The contents of this file are hereby released in the public domain, through
the terms of the CC0 license:
  https://creativecommons.org/publicdomain/zero/1.0/
"""

import struct
from io import BytesIO
from PIL import Image, ImageFile


# Magic ("DDS ")
DDS_MAGIC = 0x20534444

# DDS flags
DDSD_CAPS = 0x1
DDSD_HEIGHT = 0x2
DDSD_WIDTH = 0x4
DDSD_PITCH = 0x8
DDSD_PIXELFORMAT = 0x1000
DDSD_MIPMAPCOUNT = 0x20000
DDSD_LINEARSIZE = 0x80000
DDSD_DEPTH = 0x800000

# DDS caps
DDSCAPS_COMPLEX = 0x8
DDSCAPS_TEXTURE = 0x1000
DDSCAPS_MIPMAP = 0x400000

DDSCAPS2_CUBEMAP = 0x200
DDSCAPS2_CUBEMAP_POSITIVEX = 0x400
DDSCAPS2_CUBEMAP_NEGATIVEX = 0x800
DDSCAPS2_CUBEMAP_POSITIVEY = 0x1000
DDSCAPS2_CUBEMAP_NEGATIVEY = 0x2000
DDSCAPS2_CUBEMAP_POSITIVEZ = 0x4000
DDSCAPS2_CUBEMAP_NEGATIVEZ = 0x8000

# Pixel Format
DDPF_ALPHAPIXELS = 0x1
DDPF_ALPHA = 0x2
DDPF_FOURCC = 0x4
DDPF_PALETTEINDEXED8 = 0x20
DDPF_RGB = 0x40
DDPF_LUMINANCE = 0x20000


# dds.h

DDS_FOURCC = DDPF_FOURCC
DDS_RGB = DDPF_RGB
DDS_RGBA = DDPF_RGB | DDPF_ALPHAPIXELS
DDS_LUMINANCE = DDPF_LUMINANCE
DDS_LUMINANCEA = DDPF_LUMINANCE | DDPF_ALPHAPIXELS
DDS_ALPHA = DDPF_ALPHA
DDS_PAL8 = DDPF_PALETTEINDEXED8

DDS_HEADER_FLAGS_TEXTURE = DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PIXELFORMAT
DDS_HEADER_FLAGS_MIPMAP = DDSD_MIPMAPCOUNT
DDS_HEADER_FLAGS_VOLUME = DDSD_DEPTH
DDS_HEADER_FLAGS_PITCH = DDSD_PITCH
DDS_HEADER_FLAGS_LINEARSIZE = DDSD_LINEARSIZE

DDS_HEIGHT = DDSD_HEIGHT
DDS_WIDTH = DDSD_WIDTH

DDS_SURFACE_FLAGS_TEXTURE = DDSCAPS_TEXTURE
DDS_SURFACE_FLAGS_MIPMAP = DDSCAPS_COMPLEX | DDSCAPS_MIPMAP
DDS_SURFACE_FLAGS_CUBEMAP = DDSCAPS_COMPLEX

DDS_CUBEMAP_POSITIVEX = DDSCAPS2_CUBEMAP | DDSCAPS2_CUBEMAP_POSITIVEX
DDS_CUBEMAP_NEGATIVEX = DDSCAPS2_CUBEMAP | DDSCAPS2_CUBEMAP_NEGATIVEX
DDS_CUBEMAP_POSITIVEY = DDSCAPS2_CUBEMAP | DDSCAPS2_CUBEMAP_POSITIVEY
DDS_CUBEMAP_NEGATIVEY = DDSCAPS2_CUBEMAP | DDSCAPS2_CUBEMAP_NEGATIVEY
DDS_CUBEMAP_POSITIVEZ = DDSCAPS2_CUBEMAP | DDSCAPS2_CUBEMAP_POSITIVEZ
DDS_CUBEMAP_NEGATIVEZ = DDSCAPS2_CUBEMAP | DDSCAPS2_CUBEMAP_NEGATIVEZ


def decode565(bits):
	a = ((bits >> 11) & 0x1f) << 3
	b = ((bits >> 5) & 0x3f) << 2
	c = (bits & 0x1f) << 3
	return a, b, c


def _c2a(a, b):
	return (2 * a + b) // 3

def _c2b(a, b):
	return (a + b) // 2

def _c3(a, b):
	return (2 * b + a) // 3


def dxt1(data, width, height):
	ret = bytearray(4 * width * height)
	data = BytesIO(data)

	for y in range(0, height, 4):
		for x in range(0, width, 4):
			color0, color1, bits = struct.unpack("<HHI", data.read(8))

			r0, g0, b0 = decode565(color0)
			r1, g1, b1 = decode565(color1)

			# Decode this block into 4x4 pixels
			for j in range(4):
				for i in range(4):
					# get next control op and generate a pixel
					control = bits & 3
					bits = bits >> 2
					if control == 0:
						r, g, b = r0, g0, b0
					elif control == 1:
						r, g, b = r1, g1, b1
					elif control == 2:
						if color0 > color1:
							r, g, b = _c2a(r0, r1), _c2a(g0, g1), _c2a(b0, b1)
						else:
							r, g, b = _c2b(r0, r1), _c2b(g0, g1), _c2b(b0, b1)
					elif control == 3:
						if color0 > color1:
							r, g, b = _c3(r0, r1), _c3(g0, g1), _c3(b0, b1)
						else:
							r, g, b = 0, 0, 0

					idx = 4 * ((y + j) * width + (x + i))
					ret[idx:idx+4] = bytes([r, g, b, 0xff])

	return ret


def _dxtc_alpha(a0, a1, ac0, ac1, ai):
	if ai <= 12:
		ac = (ac0 >> ai) & 7
	elif ai == 15:
		ac = (ac0 >> 15) | ((ac1 << 1) & 6)
	else:
		ac = (ac1 >> (ai - 16)) & 7

	if ac == 0:
		alpha = a0
	elif ac == 1:
		alpha = a1
	elif a0 > a1:
		alpha = ((8 - ac) * a0 + (ac - 1) * a1) // 7
	elif ac == 6:
		alpha = 0
	elif ac == 7:
		alpha = 0xff
	else:
		alpha = ((6 - ac) * a0 + (ac - 1) * a1) // 5

	return alpha


def dxt5(data, width, height):
	ret = bytearray(4 * width * height)
	data = BytesIO(data)

	for y in range(0, height, 4):
		for x in range(0, width, 4):
			a0, a1, ac0, ac1, c0, c1, code = struct.unpack("<2BHI2HI", data.read(16))

			r0, g0, b0 = decode565(c0)
			r1, g1, b1 = decode565(c1)

			for j in range(4):
				for i in range(4):
					ai = 3 * (4 * j + i)
					alpha = _dxtc_alpha(a0, a1, ac0, ac1, ai)

					cc = (code >> 2 * (4 * j + i)) & 3
					if cc == 0:
						r, g, b = r0, g0, b0
					elif cc == 1:
						r, g, b = r1, g1, b1
					elif cc == 2:
						r, g, b = _c2a(r0, r1), _c2a(g0, g1), _c2a(b0, b1)
					elif cc == 3:
						r, g, b = _c3(r0, r1), _c3(g0, g1), _c3(b0, b1)

					idx = 4 * ((y + j) * width + (x + i))
					ret[idx:idx+4] = bytes([r, g, b, alpha])

	return ret