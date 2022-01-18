Event Handlers
--------------

Window objects will call user-defined event handler functions in response to various interaction events. 
Event handlers are managed using a window member called 'On'. 
This has sub-members for each GUI element with an ID, and those have members for each available event. 
To set up an event handler, define a function for it, then assign the function to the window's On.ID.

Event member as follows:

..  code-block:: python

	def OnClose(ev):
		dispatcher.ExitLoop()

	win.On.myWindow.Close = OnClose

Alternatively, if your object's ID is stored in a string variable called 'buttonID', you could use:

..  code-block:: python

	win.On[buttonID].Clicked = OnButtonClicked


Many objects have specific events that can be handled:

Button
------

Clicked
^^^^^^^

..  topic:: Description

	This event is triggered with a mouse click

**Type:** event

..  note:: Not tested yet

	win.On['my_button'].Clicked = OnButtonClicked


Toggled
^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_button'].Toggled = OnToggle


Pressed
^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_button'].Pressed = OnPress


Released
^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_button'].Released = OnRelease


CheckBox
--------

Clicked
^^^^^^^

..  topic:: Description

	This event is triggered with a mouse click

**Type:** event

..  note:: Not tested yet

	win.On['my_checkbox'].Clicked = OnCheckboxClicked


Toggled
^^^^^^^

..  topic:: Description

	This event is triggered

**Type:** event

..  note:: Not tested yet

	win.On['my_checkbox'].Toggled = OnCheckboxToggle


Pressed
^^^^^^^

..  topic:: Description

	This event is triggered

**Type:** event

..  note:: Not tested yet

	win.On['my_checkbox'].Pressed = OnCheckboxPress


Released
^^^^^^^^

..  topic:: Description

	This event is triggered

**Type:** event

..  note:: Not tested yet

	win.On['my_checkbox'].Released = OnCheckboxRelease


ComboBox
--------

CurrentIndexChanged
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].CurrentIndexChanged = OnComboBoxCurrentIndexChanged


CurrentTextChanged
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].CurrentTextChanged = OnComboBoxCurrentTextChanged


TextEdited
^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].TextEdited = OnComboBoxTextEdited


EditTextChanged
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].EditTextChanged = OnComboBoxEditTextChanged


EditingFinished
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].EditingFinished = OnComboBoxEditingFinished


ReturnPressed
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].ReturnPressed = OnComboBoxReturnPressed


Activated
^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].Activated = OnComboBoxActivated


SpinBox
-------

ValueChanged
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_spinbox'].ValueChanged = OnSpinBoxValueChanged


EditingFinished
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_spinbox'].EditingFinished = OnSpinBoxEditingFinished


Slider
------

ValueChanged
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_slider'].ValueChanged = OnSliderValueChanged


SliderMoved
^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_slider'].SliderMoved = OnSliderSliderMoved


ActionTriggered
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_slider'].ActionTriggered = OnSliderActionTriggered


SliderPressed
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_slider'].SliderPressed = OnSliderPressed


SliderReleased
^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_slider'].SliderReleased = OnSliderReleased


RangeChanged
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_slider'].RangeChanged = OnSliderRangeChanged


LineEdit
--------

TextChanged
^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_le'].TextChanged = OnLineEditTextChanged


TextEdited
^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_le'].TextEdited = OnLineEditTextEdited


EditingFinished
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_le'].EditingFinished = OnLineEditEditingFinished


ReturnPressed
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_le'].ReturnPressed = OnLineEditReturnPressed


SelectionChanged
^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_le'].SelectionChanged = OnLineEditSelectionChanged


CursorPositionChanged
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_le'].CursorPositionChanged = OnLineEditCursorPositionChanged


TextEdit
--------

TextChanged
^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_te'].TextChanged = OnTextEditTextChanged


SelectionChanged
^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_te'].SelectionChanged = OnTextEditSelectionChanged


CursorPositionChanged
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_te'].CursorPositionChanged = OnTextEditCursorPositionChanged


ColorPicker
-----------

ColorChanged
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_colorpicker'].ColorChanged = OnColorPickerColorChanged


TabBar
------

CurrentChanged
^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tabbar'].CurrentChanged = OnTabBarCurrentChanged


CloseRequested
^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tabbar'].CloseRequested = OnTabBarCloseRequested


TabMoved
^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tabbar'].TabMoved = OnTabBarTabMoved


TabBarClicked
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tabbar'].TabBarClicked = OnTabBarClicked


TabBarDoubleClicked
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tabbar'].TabBarDoubleClicked = OnTabBarDoubleClicked


Tree
----

CurrentItemChanged
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].CurrentItemChanged = OnTreeCurrentItemChanged


ItemClicked
^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemClicked = OnTreeItemClicked


ItemPressed
^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemPressed = OnTreeItemPressed


ItemActivated
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemActivated = OnTreeItemActivated


ItemDoubleClicked
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemDoubleClicked = OnTreeItemDoubleClicked


ItemChanged
^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemChanged = OnTreeItemChanged


ItemEntered
^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemEntered = OnTreeItemEntered


ItemExpanded
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemExpanded = OnTreeItemExpanded


ItemCollapsed
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemCollapsed = OnTreeItemCollapsed


CurrentItemChanged
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].CurrentItemChanged = OnTreeCurrentItemChanged


ItemSelectionChanged
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_tree'].ItemSelectionChanged = OnTreeItemSelectionChanged


Window
------

Close
^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].Close = OnWindowClose


Show
^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].Show = OnWindowShow


Hide
^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].Hide = OnWindowHide


Resize
^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].Resize = OnWindowResize


MousePress
^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].MousePress = OnWindowMousePress


MouseRelease
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].MouseRelease = OnWindowMouseRelease


MouseDoubleClick
^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].MouseDoubleClick = OnWindowMouseDoubleClick


MouseMove
^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].MouseMove = OnWindowMouseMove


Wheel
^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].Wheel = OnWindowWheel


KeyPress
^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].KeyPress = OnWindowKeyPress


KeyRelease
^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].KeyRelease = OnWindowKeyRelease


FocusIn
^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].FocusIn = OnWindowFocusIn


FocusOut
^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].FocusOut = OnWindowFocusOut


ContextMenu
^^^^^^^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].ContextMenu = OnWindowContextMenu


Enter
^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].Enter = OnWindowEnter


Leave
^^^^^

..  topic:: Description

	This event is triggered 

**Type:** event

..  note:: Not tested yet

	win.On['my_window'].Leave = OnWindowLeave


Event handler functions are called with a dictionary of related attributes such as who, what, when, sender, and modifiers. 

**Common events and some additional attributes they receive include:**

* **MousePress:**		Pos, GlobalPos, Button, Buttons
* **MouseRelease:**	    Pos, GlobalPos, Button, Buttons 
* **MouseDoubleClick:**	Pos, GlobalPos, Button, Buttons 
* **MouseMove:**		Pos, GlobalPos, Button, Buttons
* **Wheel:**			Pos, GlobalPos, Buttons, Delta, PixelDelta, AngleDelta, Orientiation, Phase
* **KeyPress:**			Key, Text, IsAutoRepeat, Count
* **KeyRelease:**		Key, Text, IsAutoRepeat, Count
* **ContextMenu:**		Pos, GlobalPos
* **Move:**				Pos, OldPos
* **FocusIn:**			Reason
* **FocusOut:**			Reason

..  warning::

	Event handlers can be enabled or disabled for a given element by turning them on or off in the Events attribute:

	..  code-block:: python

		ui.Slider({ 'ID': 'mySlider', 'Events': { 'SliderMoved': true } })
	
	Some common events like Clicked or Close are enabled by default.