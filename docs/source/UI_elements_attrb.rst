Attributes
==========

The element's ID is used to find, manage, and dispatch events for that element. GUI elements also support a set of common attributes including 
Enabled, Hidden, Visible, Font, WindowTitle, BackgroundColor, Geometry, ToolTip, StatusTip, StyleSheet, WindowOpacity, MinimumSize, MaximumSize, 
and FixedSize. Some other common GUI elements and their main attributes include:


.. note:: For better management of elements, define an ID attribute. Not all example will contain an ID but keep that in mind. 

Label
-----

Text
^^^^

..  topic:: Description

	This label attribute is used to display Text on the element. 

**Type:** string

..  code-block:: python

	ui.Label({ 'Text': "This is a text" })

Alignment 
^^^^^^^^^

**Type:** ({'Parameter': bool})

..  topic:: Description

	This label attribute is used to display Text on the element.

	* AlignCenter
	* AlignHCenter
	* AlighVCenter
	* Others to list

..  code-block:: python

	ui.Label({ 'Text': "This is a text", 'Alignment': { 'AlignCenter' : True } })


FrameStyle
^^^^^^^^^^

**Type:** 

..  topic:: Description

	This label attribute is used to Style

..  note:: Not yet tested

	ui.Label({ 'FrameStyle': "" })

WordWrap
^^^^^^^^

**Type:** bool

..  topic:: Description

	This label attribute enable Wordwrap when the Text attribute is longer than the window's width

..  code-block:: python
	
	ui.Label({ 'Text': "This is a longer text than the window that was created" , 'WordWrap': True })

Indent
^^^^^^

**Type:** bool

..  topic:: Description
	
	This label attribute

..  note:: Not yet tested

	ui.Label({ 'Indent': "" })

..  topic:: Margin

	This label attribute

..  note:: Not yet tested

	ui.Label({ 'Margin': "" })

Button
------

..  topic:: Text (string)
	
	This label attribute is used to display Text on the element. 

..  code-block:: 

    ui.Button({ 'ID': 'ok_btn',  'Text': "OK" })

..  topic:: Down ()
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.Button({ 'ID': 'ok_btn',  'Down': "" })

..  topic:: Checkable (bool)
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.Button({ 'ID': 'ok_btn',  'Checkable': True })


..  topic:: Checked (bool)
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.Button({ 'ID': 'ok_btn',  'Checked': True })


..  topic:: Icon ()
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.Button({ 'ID': 'ok_btn',  'Icon': "" })


..  topic:: IconSize ()
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.Button({ 'ID': 'ok_btn',  'IconSize': "" })


..  topic:: Flat ()
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.Button({ 'ID': 'ok_btn',  'Flat': "" })


CheckBox
--------


..  topic:: Text (string)
	
	This label attribute is used to display Text on the element. 

..  code-block:: 

    ui.CheckBox({ 'ID': 'ok_btn',  'Text': "OK" })

..  topic:: Down ()
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.CheckBox({ 'ID': 'ok_btn',  'Down': "" })

..  topic:: Checkable (bool)
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.CheckBox({ 'ID': 'ok_btn',  'Checkable': True })


..  topic:: Checked (bool)
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.CheckBox({ 'ID': 'ok_btn',  'Checked': True })


..  topic:: Tristate ()
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.CheckBox({ 'ID': 'ok_btn',  'Tristate': "" })


..  topic:: CheckState ()
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.CheckBox({ 'ID': 'ok_btn',  'CheckState': "" })


ComboBox
--------


..  topic:: ItemText ()
	
	This label attribute is used to display Text on the element. 

..  note:: Not yet tested

    ui.ComboBox({ 'ID': 'combo_1',  'ItemText': "OK" })

..  topic:: Down ()
	
	This label attribute is used to 

..  note:: Not yet tested

    ui.ComboBox({ 'ID': 'ok_btn',  'Down': "" })


+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Element                                                                               | Attributes                                                                                                                    |
+=======================================================================================+===============================================================================================================================+
| ComboBox:                                                                             | ItemText, Editable, CurrentIndex, CurrentText, Count                                                                          |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| SpinBox:                                                                              | Value, Minimum, Maximum, SingleStep, Prefix, Suffix, Alignment, ReadOnly, Wrapping                                            |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Slider:                                                                               | Value, Minimum, Maximum, SingleStep, PageStep, Orientation, Tracking, SliderPosition                                          |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| LineEdit:                                                                             | Text, PlaceholderText, Font, MaxLength, ReadOnly, Modified, ClearButtonEnabled                                                |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| TextEdit:                                                                             | Text, PlaceholderText, HTML, Font, Alignment, ReadOnly, TextColor, TextBackgroundColor, TabStopWidth, Lexer, LexerColors      |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ColorPicker:                                                                          | Text, Color, Tracking, DoAlpha                                                                                                |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Font:                                                                                 | Family, StyleName, PointSize, PixelSize, Bold, Italic, Underline, Overline, StrikeOut, Kerning, Weight, Stretch, MonoSpaced   |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Icon:                                                                                 | File                                                                                                                          |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| TabBar:                                                                               | CurrentIndex, TabsClosable, Expanding, AutoHide, Movable, DrawBase, UsesScrollButtons, DocumentMode, ChangeCurrentOnDrag      |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Tree:                                                                                 | ColumnCount, SortingEnabled, ItemsExpandable, ExpandsOnDoubleClick, AutoExpandDelay, HeaderHidden, IconSize, RootIsDecorated, |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
|                                                                                       | Animated, AllColumnsShowFocus, WordWrap, TreePosition, SelectionBehavior, SelectionMode, UniformRowHeights, Indentation,      |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
|                                                                                       | VerticalScrollMode, HorizontalScrollMode, AutoScroll, AutoScrollMargin, TabKeyNavigation, AlternatingRowColors,               |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
|                                                                                       | FrameStyle, LineWidth, MidLineWidth, FrameRect, FrameShape, FrameShadow                                                       |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| TreeItem:                                                                             | Selected, Hidden, Expanded, Disabled, FirstColumnSpanned, Flags, ChildIndicatorPolicy                                         |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+


Some elements also have property arrays, indexed by item or column (zero-based), e.g. newItem.Text[2] = 'Third column text'

	Combo:		ItemText[]
	TabBar:		TabText[], TabToolTip[], TabWhatsThis[], TabTextColor[]
	Tree:		ColumnWidth[]
	Treeitem: 	Text[], StatusTip[], ToolTip[], WhatsThis[], SizeHint[], TextAlignment[], CheckState[], BackgroundColor[], TextColor[], Icon[], Font[]
	
Some elements like Label and Button will automatically recognise and render basic HTML in their Text attributes, and TextEdit is capable of displaying and returning HTML too. Element attributes can be specified when creating the element, or can be read or changed later:

..  code-block:: python

	win.Find('myButton').Text = "Processing..."