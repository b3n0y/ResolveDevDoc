Attributes
----------

The element's ID is used to find, manage, and dispatch events for that element. GUI elements also support a set of common attributes including 
Enabled, Hidden, Visible, Font, WindowTitle, BackgroundColor, Geometry, ToolTip, StatusTip, StyleSheet, WindowOpacity, MinimumSize, MaximumSize, 
and FixedSize. Some other common GUI elements and their main attributes include:

+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Element                                                                               | Attributes                                                                                                                    |
+=======================================================================================+===============================================================================================================================+
| Label                                                                                 | Text, Alignment, FrameStyle, WordWrap, Indent, Margin                                                                         |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Button                                                                                | Text, Down, Checkable, Checked, Icon, IconSize, Flat                                                                          |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| CheckBox                                                                              | Text, Down, Checkable, Checked, Tristate, CheckState                                                                          |
+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
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