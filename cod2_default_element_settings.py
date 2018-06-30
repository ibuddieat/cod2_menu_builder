'''       __ ___________            
  _______/  |\_   _____/__  ______  
 /  ___/\   __\    __)_\  \/ /  _ \ 
 \___ \  |  | |        \\   (  <_> )
/____  > |__|/_______  / \_/ \____/ 
     \/              \/             

stevo.mitric@yahoo.com

This code has no licence, feel free to do whatever you want with it.
'''

rectSettings = {
	'visible':		['MENU_TRUE', 'OM|bool', None, None],
	'rect':			['0 0 200 200 4 4', 'E', None, None],
	'origin':		['0 0', 'E', None, None],
	'bordercolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'backcolor':	['0 0 0 .5', 'CB|globalColours', None, None],
	'border':		['MENU_FALSE', 'OM|bool', None, None],
	'style': 		['WINDOW_STYLE_FILLED', 'L', None, None],
}

imageSettings = {
	'visible':		['MENU_TRUE', 'OM|bool', None, None],
	'rect':			['0 0 200 200 4 4', 'E', None, None],
	'origin':		['0 0', 'E', None, None],
	'bordercolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'border':		['MENU_FALSE', 'OM|bool', None, None],
	'style': 		['WINDOW_STYLE_SHADER', 'L', None, None],
	'background': 	['', 'L', None, None],
}


fieldSettings = {
	'name': 		['datafield', 'E|S', None, None],
	'visible':		['MENU_TRUE', 'OM|bool', None, None],
	'rect':			['0 0 128 24 4 4', 'E', None, None],
	'origin':		['0 0', 'E', None, None],
	'forecolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'type':			['ITEM_TYPE_UPREDITFIELD', 'L', None, None],
	'text':			['You typed:', 'E|S', None, None],
	'dvar':			['testdvar', 'E|DNIIN', None, None],
	'textfont':		['UI_FONT_NORMAL', 'OM|font', None, None],
	'textscale':	['GLOBAL_TEXT_SIZE', 'CB|size', None, None],
	'textstyle':	['ITEM_TEXTSTYLE_NORMAL', 'OM|style', None, None],
	'textaligny':	['20', 'L', None, None],
	'bordercolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'border':		['MENU_FALSE', 'OM|bool', None, None],
	'backcolor':	['0 0 0 .5', 'CB|globalColours', None, None],
	'maxPaintChars':['5', 'E', None, None],
	'style': 		['WINDOW_STYLE_EMPTY', 'OM|windowstyle', None, None],
}

listSettings = {
	'name': 		['label', 'E|S', None, None],
	'visible':		['MENU_TRUE', 'OM|bool', None, None],
	'rect':			['0 0 128 24 4 4', 'E', None, None],
	'origin':		['0 0', 'E', None, None],
	'forecolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'type':			['ITEM_TYPE_MULTI', 'L', None, None],
	'text':			['You have chosen:', 'E|S', None, None],
	'dvar':			['testDvar', 'E|CBN', None, None],
	'dvarFloatList':['{ "1.choice" 1 "sec" 2 }', 'E|DNIIN', None, None],
	'textfont':		['UI_FONT_NORMAL', 'OM|font', None, None],
	'textscale':	['GLOBAL_TEXT_SIZE', 'CB|size', None, None],
	'textstyle':	['ITEM_TEXTSTYLE_NORMAL', 'OM|style', None, None],
	'textaligny':	['20', 'L', None, None],
	'bordercolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'border':		['MENU_FALSE', 'OM|bool', None, None],
	'style': 		['WINDOW_STYLE_EMPTY', 'OM|windowstyle', None, None],
	'backcolor':	['0 0 0 .5', 'CB|globalColours', None, None],
}

labelSettings = {
	'name': 		['label', 'E|S', None, None],
	'visible':		['MENU_TRUE', 'OM|bool', None, None],
	'rect':			['0 0 128 24 4 4', 'E', None, None],
	'origin':		['0 0', 'E', None, None],
	'forecolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'type':			['ITEM_TYPE_TEXT', 'L', None, None],
	'text':			['Example Text', 'E|S', None, None],
	'dvar':			['', 'E|DNIIN', None, None],
	'textfont':		['UI_FONT_NORMAL', 'OM|font', None, None],
	'textscale':	['GLOBAL_TEXT_SIZE', 'CB|size', None, None],
	'textstyle':	['ITEM_TEXTSTYLE_NORMAL', 'OM|style', None, None],
	'textaligny':	['20', 'L', None, None],
	'bordercolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'border':		['MENU_FALSE', 'OM|bool', None, None],
	'textalign':	['ITEM_ALIGN_LEFT', 'OM|align', None, None],
}


sliderSettings = {
	'name': 		['slider', 'E|S', None, None],
	'visible':		['MENU_TRUE', 'OM|bool', None, None],
	'rect':			['0 0 128 24 4 4', 'E', None, None],
	'origin':		['0 0', 'E', None, None],
	'forecolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'type':			['ITEM_TYPE_SLIDER', 'L', None, None],
	'text':			['Move me: ', 'E|S|CBN', None, None],
	'dvar':			['', 'E|DNIIN', None, None],
	'textfont':		['UI_FONT_NORMAL', 'OM|font', None, None],
	'textscale':	['GLOBAL_TEXT_SIZE', 'CB|size', None, None],
	'textstyle':	['ITEM_TEXTSTYLE_NORMAL', 'OM|style', None, None],
	'textaligny':	['20', 'L', None, None],
	'bordercolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'border':		['MENU_FALSE', 'OM|bool', None, None],
	'dvartest':		['', 'E|S|DNIIN', None, None],
	'hideDvar':		['', 'E|DNIIN', None, None],
	'showDvar':		['', 'E|DNIIN', None,None],
	'dvarfloat':	['testDvar 1 1 100', 'E|DNIIN', None,None],
	'style': 		['WINDOW_STYLE_EMPTY', 'OM|windowstyle', None, None],
	'backcolor':	['0 0 0 0.5', 'CB|globalColours', None, None],
}

buttonSettings = {
	'name': 		['button', 'E|S', None, None],
	'visible':		['MENU_TRUE', 'OM|bool', None, None],
	'rect':			['0 0 128 24 4 4', 'E', None, None],
	'origin':		['0 0', 'E', None, None],
	'forecolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'type':			['ITEM_TYPE_BUTTON', 'L', None, None],
	'text':			['Example Button', 'E|S', None, None],
	'dvar':			['', 'E|S|DNIIN', None, None],
	'textfont':		['UI_FONT_NORMAL', 'OM|font', None, None],
	'textscale':	['GLOBAL_TEXT_SIZE', 'CB|size', None, None],
	'textstyle':	['ITEM_TEXTSTYLE_NORMAL', 'OM|style', None, None],
	'textaligny':	['20', 'L', None, None],
	'textalign':	['ITEM_ALIGN_LEFT', 'OM|align', None, None],
	'bordercolor':	['0 0 0 1', 'CB|globalColours', None, None],
	'border':		['MENU_FALSE', 'OM|bool', None, None],
	'dvartest':		['', 'E|S|DNIIN', None, None],
	'hideDvar':		['', 'E|DNIIN', None, None],
	'showDvar':		['', 'E|DNIIN', None,None],
	'backcolor':	['0 0 0 0.5', 'CB|globalColours', None, None],
	'style': 		['WINDOW_STYLE_EMPTY', 'OM|windowstyle', None, None],
}

menuSettings = {
	'name': 		['Menu', 'E|S', None, None],
	'rect': 		['0 0 640 480 4 4', 'L', None, None],
	'focuscolor': 	['GLOBAL_FOCUSED_COLOR', 'CB|globalColours', None, None],
	'style': 		['WINDOW_STYLE_EMPTY', 'OM|windowstyle', None, None],
	'blurWorld': 	['5.0', 'E', None, None],
	'backcolor':	['0 0 0 .5', 'CB|globalColours', None, None],
	
}

elementOrder = ['name', 'visible', 'rect', 'background', 'focuscolor', 'style', 'blurWorld', 'origin', 'forecolor', 'type', 'text', 'dvar', 'textalign', 'textfont', 'textscale', 'textstyle', 'textaligny', 'backcolor', 'bordercolor', 'border', 'maxPaintChars', 'dvartest', 'dvarfloat', 'dvarFloatList', 'hideDvar', 'showDvar', 'decoration' ]

elementGroup = {
	'text': ['text', 'textfont', 'textscale', 'textstyle', 'textaligny', 'bordercolor', 'border', 'forecolor', 'textalign'],
	'basic': ['name', 'visible', 'origin', 'rect', 'style', 'blurWorld', 'focuscolor', 'type', 'decoration', 'backcolor', 'background'],
	'function': ['dvar', 'dvartest', 'hideDvar', 'showDvar', 'dvarfloat', 'dvarFloatList'],
	'other': ['maxPaintChars',]
}


globalDefinitions = {
	'type': {
		'ITEM_TYPE_TEXT':				'0',
		'ITEM_TYPE_BUTTON':				'1',
		'ITEM_TYPE_RADIOBUTTON':		'2',
		'ITEM_TYPE_CHECKBOX':			'3',
		'ITEM_TYPE_EDITFIELD': 			'4',
		'ITEM_TYPE_COMBO': 				'5',
		'ITEM_TYPE_LISTBOX':			'6',
		'ITEM_TYPE_MODEL': 				'7',
		'ITEM_TYPE_OWNERDRAW': 			'8',
		'ITEM_TYPE_NUMERICFIELD':		'9',
		'ITEM_TYPE_SLIDER':				'10',
		'ITEM_TYPE_YESNO': 				'11',
		'ITEM_TYPE_MULTI': 				'12',
		'ITEM_TYPE_DVARENUM': 			'13',
		'ITEM_TYPE_BIND':				'14',
		'ITEM_TYPE_MENUMODEL': 			'15',
		'ITEM_TYPE_VALIDFILEFIELD':		'16',
		'ITEM_TYPE_DECIMALFIELD':		'17',
		'ITEM_TYPE_UPREDITFIELD':		'18',
	
	},
	
	'align': {
		'ITEM_ALIGN_LEFT':				'0',
		'ITEM_ALIGN_CENTER':			'1',
		'ITEM_ALIGN_RIGHT':				'2',
		#'ITEM_ALIGN_CENTER2':			'3',
	},
	
	'windowborder': {
		'WINDOW_BORDER_NONE':			'0',
		'WINDOW_BORDER_FULL':			'1',
		'WINDOW_BORDER_HORZ':			'2',
		'WINDOW_BORDER_VERT':			'3',
	},
	
	'windowstyle': {
		'WINDOW_STYLE_EMPTY':			'0',
		'WINDOW_STYLE_FILLED':			'1',
		'WINDOW_STYLE_SHADER':			'3',
	},
	
	'font': {
		'UI_FONT_NORMAL':				'',		#'1',
		'UI_FONT_BOLD':					'bold',	#'4',
	
	},

	'bool': {
		'MENU_TRUE':					'1',
		'MENU_FALSE':					'0',
	},
	
	'globalColours': {
		'GLOBAL_FOCUSED_COLOR':			'.98 .827 .58 1',
		'GLOBAL_UNFOCUSED_COLOR':		'1 1 1 1',
		'GLOBAL_DISABLED_COLOR':		'.35 .35 .35 1',
		'UI_FOCUS_COLOR':				'.96 .66 .04 1',
	},
	
	
	'size': {
		'GLOBAL_TEXT_SIZE':				'.35',
		'GLOBAL_HEADER_SIZE':			'.50',
	},	
	
	'style': {
		'ITEM_TEXTSTYLE_NORMAL':		'0',
		'ITEM_TEXTSTYLE_SHADOWED':		'3',
	},
	
	
}


def getValueFromKey(key):
	for temp1 in globalDefinitions:
		for temp2 in globalDefinitions[temp1]:
			if temp2 == key:
				return globalDefinitions[temp1][temp2]
	return key
	
	