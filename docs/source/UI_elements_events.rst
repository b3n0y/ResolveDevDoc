Event Handlers
==============

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


..  important::

	Event handlers can be enabled or disabled for a given element by turning them on or off in the Events attribute:

	..  code-block:: python

		ui.Slider({ 'ID': 'mySlider', 'Events': { 'SliderMoved': True } })
	
	Some common events like Clicked or Close are enabled by default.


Many objects have specific events that can be handled:


Button
------

Clicked
^^^^^^^

..  topic:: Description

	This event is triggered with a mouse click. (default=True)

**Type:** event

..  code-block:: python

    ui.Button({'ID':'buttonID', 'Text': "My Button"})

	def OnButtonClicked(ev):
        print(f"{win.Find('buttonID').Text} was clicked")

    # assign event handlers
	win.On['buttonID'].Clicked = OnButtonClicked


Toggled
^^^^^^^

..  topic:: Description

	This event is triggered if button is Toggled

**Type:** event

..  note:: Not tested yet

    ui.Button({'ID':'buttonID', 'Text': "My Button"})

    def OnButtonToggled(ev):
        print(f"{win.Find('buttonID').Text} was Toggled")

    # assign event handlers
    win.On['buttonID'].Toggled = OnButtonToggled


Pressed
^^^^^^^

..  topic:: Description

	This event is triggered button is pressed. (default=False)

**Type:** event

..  code-block:: python
	
    ui.Button({'ID':'buttonID', 'Text': "My Button", 'Events': { 'Pressed': True }})

    def OnButtonPressed(ev):
        print(f"{win.Find('buttonID').Text} was Pressed")

    # assign event handlers
    win.On['buttonID'].Pressed = OnButtonPressed


Released
^^^^^^^^

..  topic:: Description

	This event is triggered when button is released. (default=False)

**Type:** event

..  code-block:: python

    ui.Button({'ID':'buttonID', 'Text': "My Button", 'Events': { 'Released': True }})

    def OnButtonReleased(ev):
        print(f"{win.Find('buttonID').Text} was Released")

    # assign event handlers
    win.On['buttonID'].Released = OnButtonReleased


CheckBox
--------

Clicked
^^^^^^^

..  topic:: Description

	This event is triggered with a mouse click  (default=True)

**Type:** event

..  code-block:: python

    ui.CheckBox({'ID':'my_checkbox', 'Text': "My CheckBox" })

    def OnCheckBoxClicked(ev):
        print(f"{win.Find('my_checkbox').Text} was Clicked")

    # assign event handlers
    win.On['my_checkbox'].Clicked = OnCheckBoxClicked


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

	This event is triggered when CheckBox is pressed (default=False)

**Type:** event

..  code-block:: python

    ui.CheckBox({'ID':'my_checkbox', 'Text': "My CheckBox", 'Events': { 'Pressed': True } })
    
	def OnCheckBoxPressed(ev):
        print(f"{win.Find('my_checkbox').Text} was Pressed")

    # assign event handlers
    win.On['my_checkbox'].Pressed = OnCheckBoxPressed



Released
^^^^^^^^

..  topic:: Description

	This event is triggered when CheckBox is released  (default=False)

**Type:** event

..  code-block:: python

    ui.CheckBox({'ID':'my_checkbox', 'Text': "My CheckBox", 'Events': { 'Released': True } })

    def OnCheckBoxReleased(ev):
        print(f"{win.Find('my_checkbox').Text} was Released")

    # assign event handlers
    win.On['my_checkbox'].Released = OnCheckBoxReleased



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

	This event is triggered each time the ComboBox current Text is changed

**Type:** event

..  code-block:: python

    ui.ComboBox({'ID':'combo_1', 'Text': "My ComboBox", 'Events': { 'CurrentTextChanged': True} })
    
	def OnComboBoxCurrentTextChanged(ev):
        print(f"ComboBox CurrentTextChanged changed")

    # assign event handlers
    win.On['combo_1'].CurrentTextChanged = OnComboBoxCurrentTextChanged


TextEdited
^^^^^^^^^^

..  topic:: Description

	This event is triggered when Text is edited by user in a ComboBox item.
	``The ComboBox must be Editable``

**Type:** event

..  code-block:: python

    ui.ComboBox({'ID':'combo_1', 'Text': "My ComboBox", 'Editable': True, 'Events': { 'TextEdited': True} })

    def OnComboBoxTextEdited(ev):
        print(f"ComboBox Text was Edited")

    # assign event handlers
    win.On['combo_1'].TextEdited = OnComboBoxTextEdited


EditTextChanged
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when modifications are made to a ComboBox item and ComboBox is changed. 
	``The ComboBox must be Editable``


**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].EditTextChanged = OnComboBoxEditTextChanged


EditingFinished
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered 
	``The ComboBox must be Editable``


**Type:** event

..  note:: Not tested yet

	win.On['my_combobox'].EditingFinished = OnComboBoxEditingFinished


ReturnPressed
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when Return is pressed with the ComboBox item selected.
	Return will also add the modified ComboBox item to the list
	``The ComboBox must be Editable``

**Type:** event

..  code-block:: python

    ui.ComboBox({'ID':'combo_1', 'Text': "My ComboBox", 'Editable': True, 'Events': { 'ReturnPressed': True} })

	def OnComboBoxReturnPressed(ev):
        print(f"ReturnPressed on ComboBox")   

    # assign event handlers
    win.On['combo_1'].ReturnPressed = OnComboBoxReturnPressed


Activated
^^^^^^^^^

..  topic:: Description

	This event is triggered when activity is detected on the ComboBox. 

**Type:** event

..  code-block:: python

    ui.ComboBox({'ID':'combo_1', 'Text': "My ComboBox", 'Events': { 'Activated': True } })

    def OnComboBoxIActivated(ev):
        print(f"ComboBox was Activated")

    # assign event handlers
    win.On['combo_1'].Activated = OnComboBoxIActivated


SpinBox
-------

ValueChanged
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when SpinBox value is changed. (default=True)

**Type:** event

..  code-block:: python

    ui.SpinBox({'ID':'spinbox_1'})
    
	def OnSpinBoxValueChanged(ev):
        print(f"Value Changed on SpinBox")   

    # assign event handlers
    win.On['spinbox_1'].ValueChanged = OnSpinBoxValueChanged


EditingFinished
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when Edit are made to the SpinBox items. (default=False)

**Type:** event

..  code-block:: python

    ui.SpinBox({'ID':'spinbox_1', 'Events': { 'EditingFinished': True} })

    def OnSpinBoxEditingFinished(ev):
        print(f"EditingFinished on SpinBox")   

    # assign event handlers
    win.On['spinbox_1'].EditingFinished = OnSpinBoxEditingFinished


Slider
------

ValueChanged
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when Slider value is changed (default=True)

**Type:** event

..  code-block:: python

    ui.Slider({'ID':'slider_1'})

	def OnSliderValueChanged(ev):
        print(f"Slider value changed")   

    # assign event handlers
    win.On['slider_1'].ValueChanged = OnSliderValueChanged


SliderMoved
^^^^^^^^^^^

..  topic:: Description

	This event is triggered each time the slider is moved with mouse cursor. (default=False)

**Type:** event

..  code-block:: python

    ui.Slider({'ID':'slider_1', 'Events': {'SliderMoved': True } })

   	def OnSliderSliderMoved(ev):
        print(f"Slider moved")   

    # assign event handlers
    win.On['slider_1'].SliderMoved = OnSliderSliderMoved


ActionTriggered
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when activity is detected on the Slider. (default=False)

**Type:** event

..  code-block:: python
	
    ui.Slider({'ID':'slider_1', 'Events': { 'ActionTriggered': True}  })

    def OnSliderActionTriggered(ev):
        print(f"Action Triggered")   

    # assign event handlers
    win.On['slider_1'].ActionTriggered = OnSliderActionTriggered


SliderPressed
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered each time the slider is pressed, even if not moved.  (default=False)

**Type:** event

..  code-block:: python

    ui.Slider({'ID':'slider_1', 'Events': {'SliderPressed': True}  })

    def OnSliderSliderPressed(ev):
        print(f"Slider pressed")   

    # assign event handlers
    win.On['slider_1'].SliderPressed = OnSliderSliderPressed


SliderReleased
^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered each time the slider is released, even if not moved.  (default=False)

**Type:** event

..  code-block:: python

    ui.Slider({'ID':'slider_1', 'Events': { 'SliderReleased': True}  })

    def OnSliderSliderReleased(ev):
        print(f"Slider released")   

    # assign event handlers
    win.On['slider_1'].SliderReleased = OnSliderSliderReleased


RangeChanged
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered is Minimum or Maximum slider value is change. (default=False)

**Type:** event

..  code-block:: python

    ui.Slider({'ID':'slider_1', 'Events': { 'RangeChanged': True}  })
    
	def OnSliderRangeChanged(ev):
        print("Range Changed")   

    # assign event handlers
    win.On['slider_1'].RangeChanged = OnSliderRangeChanged

	win.Find('slider_1').Maximum = 4  #trigger RangeChanged


LineEdit
--------

TextChanged
^^^^^^^^^^^

..  topic:: Description

	This event is triggered each time Text is modified in the LineEdit element.  (default=True)

**Type:** event

..  code-block:: python

    ui.LineEdit({'ID':'le_1' })

    def OnLineEditTextChanged(ev):
        print(f"LineEdit text changed")   

    # assign event handlersdfg
    win.On['le_1'].TextChanged = OnLineEditTextChanged


TextEdited
^^^^^^^^^^

..  topic:: Description

	This event is triggered each time Text is modified in the LineEdit element.  (default=False)

**Type:** event

..  code-block:: python

    ui.LineEdit({'ID':'le_1', 'Events': {'TextEdited': True } })

    def OnLineEditTextEdited(ev):
        print(f"LineEdit Text Edited")   

    # assign event handlersdfg
    win.On['le_1'].TextEdited = OnLineEditTextEdited


EditingFinished
^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered if, after a modification to the Text, Return is pressed or Focus change to another Element.  (default=False)

**Type:** event

..  code-block:: python

    ui.LineEdit({'ID':'le_1', 'Events': { 'EditingFinished': True } })

  	def OnLineEditEditingFinished(ev):
        print(f"Editing Finished")   

    # assign event handlersdfg
    win.On['le_1'].EditingFinished = OnLineEditEditingFinished


ReturnPressed
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when Return is pressed with LineEdit element selected.  (default=False)

**Type:** event

..  code-block:: python

    ui.LineEdit({'ID':'le_1', 'Events': { 'ReturnPressed': True } })

    def OnLineEditReturnPressed(ev):
        print(f"Return Pressed")   

    # assign event handlersdfg
    win.On['le_1'].ReturnPressed = OnLineEditReturnPressed


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

	This event is triggered each time the cursor change position in the LineEdit Element.   (default=False)  
	Inserting new character also changes the cursor position. 

**Type:** event

..  code-block:: python

    ui.LineEdit({'ID':'le_1', 'Events': { 'CursorPositionChanged': True} })

    def OnLineEditCursorPositionChanged(ev):
        print(f"Cursor Position Changed")   

    # assign event handlersdfg
    win.On['le_1'].CursorPositionChanged = OnLineEditCursorPositionChanged


TextEdit
--------

TextChanged
^^^^^^^^^^^

..  topic:: Description

	This event is triggered each time Text is modified in the TextEdit element.  (default=True)

**Type:** event

..  code-block:: python

    ui.TextEdit({'ID':'te_1' })

    def OnLineEditTextChanged(ev):
        print(f"TextEdit text changed")   

    # assign event handlersdfg
    win.On['te_1'].TextChanged = OnTextEditTextChanged


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

	This event is triggered each time the cursor change position in the TextEdit Element.   (default=False)  
	Inserting new character also changes the cursor position. 

**Type:** event

..  code-block:: python

    ui.TextEdit({'ID':'te_1', 'Events': { 'CursorPositionChanged': True } })

    def OnTextEditCursorPositionChanged(ev):
        print(f"Cursor Position Changed")   

    # assign event handlersdfg
    win.On['te_1'].CursorPositionChanged = OnTextEditCursorPositionChanged


ColorPicker
-----------

ColorChanged
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when color is changed on ColorPicker element. (default=True)

**Type:** event

..  code-block:: python

    ui.ColorPicker({'ID':'colorpicker_1' })

    def OnColorPickerColorChanged(ev):
        print(f"Color Changed")   

    # assign event handlersdfg
    win.On['colorpicker_1'].ColorChanged = OnColorPickerColorChanged


TabBar
------

CurrentChanged
^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered each time Tab is changed.  (default=True)

**Type:** event

..  code-block:: python

    ui.TabBar({'ID':'tabbar_1'})

    def OnTabBarCurrentChanged(ev):
        print(f"Tab Changed")   

    # assign event handlersdfg
    win.On['tabbar_1'].CurrentChanged = OnTabBarCurrentChanged


CloseRequested
^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when a Tab is closed.  (default=False)
	``TabsClosable must be set to True``

**Type:** event

..  code-block:: python

    ui.TabBar({'ID':'tabbar_1', 'TabsClosable': True, 'Events': {'CloseRequested': True} })
    
	def OnTabBarCloseRequested(ev):
        print(f"Tab Close Requested")   

    # assign event handlersdfg
    win.On['tabbar_1'].CloseRequested = OnTabBarCloseRequested


TabMoved
^^^^^^^^

..  topic:: Description

	This event is triggered when a Tab is moved.  (default=False)
	``TabBar must be Movable``


**Type:** event

..  code-block:: python

    ui.TabBar({'ID':'tabbar_1', 'Movable': True, 'Events': {'TabMoved': True} })
	    
	def OnTabBarTabMoved(ev):
        print(f"Tab Moved")   

    # assign event handlersdfg
    win.On['tabbar_1'].TabMoved = OnTabBarTabMoved


TabBarClicked
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered each time the TabBar is clicked.  (default=False)

**Type:** event

..  code-block:: python

    ui.TabBar({'ID':'tabbar_1', 'Events': {'TabBarClicked': True} })

    def OnTabBarClicked(ev):
        print(f"TabBar Clicked")   

    # assign event handlersdfg
    win.On['tabbar_1'].TabBarClicked = OnTabBarClicked


TabBarDoubleClicked
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered each time the TabBar is double clicked.  (default=False)

**Type:** event

..  code-block:: python

    ui.TabBar({'ID':'tabbar_1', 'Events': {'TabBarDoubleClicked': True} })

    def OnTabBarDoubleClicked(ev):
        print(f"TabBar Double Clicked")   

    # assign event handlersdfg
    win.On['tabbar_1'].TabBarDoubleClicked = OnTabBarDoubleClicked


Tree
----

CurrentItemChanged
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when the TreeItem is changed.  (default=True)

**Type:** event

..  code-block:: python

	ui.Tree({'ID':'tree_1'})

	def OnCurrentItemChanged(ev):
		print('TreeItem was changed')

	win.On['my_tree'].CurrentItemChanged = OnCurrentItemChanged


ItemClicked
^^^^^^^^^^^

..  topic:: Description

	This event is triggered when a TreeItem is Clicked.  (default=True)

**Type:** event

..  code-block:: python

	ui.Tree({'ID':'my_tree' })

	def OnTreeItemClicked(ev):
		print('Item was clicked')

	win.On['my_tree'].ItemClicked = OnTreeItemClicked


ItemPressed
^^^^^^^^^^^

..  topic:: Description

	This event is triggered when a TreeItem is Clicked.  (default=False)

**Type:** event

..  code-block:: python

	ui.Tree({'ID':'my_tree' })

	def OnTreeItemPressed(ev):
		print('Item was pressed')

	win.On['my_tree'].ItemPressed = OnTreeItemPressed


ItemActivated
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when a TreeItem is DoubleClicked or...  (default=False)

**Type:** event

..  code-block:: python

	ui.Tree({'ID':'my_tree', 'Events' : { 'ItemDouItemActivatedbleClicked' : True } })

	def OnTreeItemActivated(ev):
		print('Item was activated')

	win.On['my_tree'].ItemActivated = OnTreeItemActivated


ItemDoubleClicked
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when a TreeItem is DoubleClicked.  (default=False)

**Type:** event

..  code-block:: python

	ui.Tree({'ID':'my_tree', 'Events' : { 'ItemDoubleClicked' : True } })

	def OnTreeItemDoubleClicked(ev):
		print('Item was double clicked')

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

	This event is triggered when Enter is pressed on a TreeItem.  (default=False)

**Type:** event

..  note:: Not tested yet

	ui.Tree({'ID':'tree_1', 'Events': {'ItemEntered': True} })

    def OnItemEntered(ev):
        print(f"Item Entered")   

    # assign event handlers
    win.On['tree_1'].ItemEntered = OnItemEntered


ItemExpanded
^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when a TreeItem with Child is Expanded.  (default=False)

**Type:** event

..  code-block:: python

	ui.Tree({'ID':'tree_1', 'Events': {'ItemExpanded': True} })

    def OnItemExpanded(ev):
        print(f"Item Expanded")   

    # assign event handlers
    win.On['tree_1'].ItemExpanded = OnItemExpanded


ItemCollapsed
^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when a TreeItem with Child is Collapsed.  (default=False)

**Type:** event

..  code-block:: python

	ui.Tree({'ID':'tree_1', 'Events': {'ItemCollapsed': True} })

    def OnItemExpanded(ev):
        print(f"Item Collapsed")   

    # assign event handlers
    win.On['tree_1'].ItemCollapsed = OnItemCollapsed


CurrentItemChanged
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when the selected Tree item is changed.  (default=True)

**Type:** event

..  note:: Not tested yet

	ui.Tree({'ID':'tree_1'})

    def OnCurrentItemChanged(ev):
        print(f"Current Item Changed")   

    # assign event handlers
    win.On['tree_1'].CurrentItemChanged = OnCurrentItemChanged


ItemSelectionChanged
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This event is triggered when the selected Tree item is changed.  (default=False)

**Type:** event

..  code-block:: python

	ui.Tree({'ID':'tree_1', 'Events': {'ItemSelectionChanged': True}  })

    def OnItemSelectionChanged(ev):
        print(f"Item Selection Changed")   

    # assign event handlers
    win.On['tree_1'].ItemSelectionChanged = OnItemSelectionChanged


Window
------

Close
^^^^^

..  topic:: Description

	This event is triggered when the Window close button is pressed. (default=True)

**Type:** event

..  code-block:: python

    # Event handlers
    def OnWindowClose(ev):
        dispatcher.ExitLoop()

	win.On['my_window'].Close = OnWindowClose


Show
^^^^

..  topic:: Description

	This event is triggered when the Window is shown or returns from a hidden state. 

**Type:** event

..  code-block:: python

    win = dispatcher.AddWindow({
        'ID': "my_window",
        'Geometry': [ 400,200,250,125 ],
        'WindowTitle': 'My Window',
        'Events': {'Show': True, 'Clicked': True, 'Close': True} 
        },
        ui.VGroup([
    		ui.Label({'ID':'label_1', 'Text': 'My label' })
        ])
    )

    def OnWindowShow(ev):
        print(f"Show") 

	# assign event handlers
	win.On['my_window'].Show = OnWindowShow


Hide
^^^^

..  topic:: Description

	This event is triggered when the Window is hidden by another Window

**Type:** event

..  code-block:: python

    win = dispatcher.AddWindow({
        'ID': "my_window",
        'Geometry': [ 400,200,250,125 ],
        'WindowTitle': 'My Window',
        'Events': {'Hide': True, 'Clicked': True, 'Close': True} 
        },
        ui.VGroup([
    		ui.Label({'ID':'label_1', 'Text': 'My label' })
        ])
    )

    def OnWindowHide(ev):
        print(f"Hidden") 

	# assign event handlers
	win.On['my_window'].Hide = OnWindowHide


Resize
^^^^^^

..  topic:: Description

	This event is triggered each time the Window is resized.  (default=False)

**Type:** event

..  code-block:: python

    win = dispatcher.AddWindow({
        'ID': "my_window",
        'Events': {'Resize': True, 'Clicked': True, 'Close': True} 
        },
        ui.VGroup([
    		ui.Label({'ID':'label_1', 'Text': 'My label' })
        ])
    )

	def OnWindowResize(ev):
        print(f"Window resized")   

    # assign event handler
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

