Event Handlers
--------------

Window objects will call user-defined event handler functions in response to various interaction events. Event handlers are managed using a window member called 'On'. This has sub-members for each GUI element with an ID, and those have members for each available event. To set up an event handler, define a function for it, then assign the function to the window's On.ID.Event member as follows:

..  code-block:: python

	def OnClose(ev):
		dispatcher.ExitLoop()

	win.On.myWindow.Close = OnClose

Alternatively, if your object's ID is stored in a string variable called 'buttonID', you could use:

..  code-block:: python

	win.On[buttonID].Clicked = OnButtonClicked

Many objects have specific events that can be handled:

	Button:				Clicked, Toggled, Pressed, Released
	CheckBox:			Clicked, Toggled, Pressed, Released
	ComboBox:			CurrentIndexChanged, CurrentTextChanged, TextEdited, EditTextChanged, EditingFinished, ReturnPressed, Activated
	SpinBox:			ValueChanged, EditingFinished
	Slider:				ValueChanged, SliderMoved, ActionTriggered, SliderPressed, SliderReleased, RangeChanged
	LineEdit:			TextChanged, TextEdited, EditingFinished, ReturnPressed, SelectionChanged, CursorPositionChanged
	TextEdit:			TextChanged, SelectionChanged, CursorPositionChanged
	ColorPicker:		ColorChanged
	TabBar:				CurrentChanged, CloseRequested, TabMoved, TabBarClicked, TabBarDoubleClicked
	Tree:				CurrentItemChanged, ItemClicked, ItemPressed, ItemActivated, ItemDoubleClicked, ItemChanged, ItemEntered, 
						ItemExpanded, ItemCollapsed, CurrentItemChanged, ItemSelectionChanged
	Window:				Close, Show, Hide, Resize, MousePress, MouseRelease, MouseDoubleClick, MouseMove, Wheel, KeyPress, KeyRelease,
						FocusIn, FocusOut, ContextMenu, Enter, Leave

Event handler functions are called with a dictionary of related attributes such as who, what, when, sender, and modifiers. Common events and some additional attributes they receive include:

	MousePress:			Pos, GlobalPos, Button, Buttons
	MouseRelease:		Pos, GlobalPos, Button, Buttons 
	MouseDoubleClick:	Pos, GlobalPos, Button, Buttons 
	MouseMove:			Pos, GlobalPos, Button, Buttons
	Wheel:				Pos, GlobalPos, Buttons, Delta, PixelDelta, AngleDelta, Orientiation, Phase
	KeyPress:			Key, Text, IsAutoRepeat, Count
	KeyRelease:			Key, Text, IsAutoRepeat, Count
	ContextMenu:		Pos, GlobalPos
	Move:				Pos, OldPos
	FocusIn:			Reason
	FocusOut:			Reason

Event handlers can be enabled or disabled for a given element by turning them on or off in the Events attribute:

..  code-block:: python

	ui.Slider({ 'ID': 'mySlider', 'Events': { 'SliderMoved': true } })
	
Some common events like Clicked or Close are enabled by default.