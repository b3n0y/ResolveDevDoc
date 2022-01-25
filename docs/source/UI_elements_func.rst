Functions
=========

Most elements have functions that can be called from them as well:

* Show()
* Hide()
* Raise()
* Lower()
* Close()			Returns boolean
* Find(ID)			Returns child element with matching ID
* GetChildren()		Returns list
* AddChild(element)
* RemoveChild(element)
* SetParent(element)
* Move(point)
* Resize(size)
* Size()				Returns size
* Pos()				Returns position
* HasFocus()			Returns boolean
* SetFocus(reason)	Accepts string "MouseFocusReason", "TabFocusReason", "ActiveWindowFocusReason", "OtherFocusreason", etc
* FocusWidget()		Returns element
* IsActiveWindow()	Returns boolean
* SetTabOrder(element)
* Update()
* Repaint()
* SetPaletteColor(r,g,b)
* QueueEvent(name, info)  Accepts event name string and dictionary of event attributes
* GetItems()			Returns dictionary of all child elements


Some elements have extra functions of their own:


Label
-----

SetSelection(int, int)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function used to 

**Type:** int= int=

..  note:: Not tested yet

	win['mylabel'].SetSelection(0,1)


HasSelection()
^^^^^^^^^^^^^^

..  topic:: Description

	This function return True if Label has selection

**Type:** return bool

..  note:: Not tested yet

	win['mylabel'].HasSelection()


SelectedText()
^^^^^^^^^^^^^^

..  topic:: Description

	This function return SelectedText string

**Type:** return string

..  note:: Not tested yet

	win['mylabel'].SelectedText()


SelectionStart()
^^^^^^^^^^^^^^^^

..  topic:: Description

	This function return the index of the selection

**Type:** return int

..  note:: Not tested yet

	win['mylabel'].SelectionStart()


Button
------

Click()
^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['mybutton'].Click()


Toggle()
^^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mybutton'].Toggle()


AnimateClick()
^^^^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mybutton'].AnimateClick()



CheckBox
--------

Click()
^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['mycheckbox'].Click()


Toggle()
^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['mycheckbox'].Toggle()


AnimateClick()
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['mycheckbox'].AnimateClick()



ComboBox
--------

AddItem(string)
^^^^^^^^^^^^^^^

..  topic:: Description

	This function add the item to the ComboBox list. 

**Type:** func

..  code-block:: python

	win.Find('combo_1').AddItem('Item Name')


InsertItem(int, string)
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is inserting an item at the specified index. 

**Type:** func

..  code-block:: python

	win.Find('combo_1').InsertItem(1, 'New item')


AddItems(list)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is adding a list of item to the ComboBox list. 

**Type:** func

..  code-block:: python

	win.Find('combo_1').AddItems(['Item 1', 'Item 2', 'Item 3'])


InsertItems(int, list)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is inserting a list of items at the specified index. 

**Type:** int= index, list=[string]

..  code-block:: python

	win.Find('combo_1').InsertItems(1, ['Item 1', 'Item 2'])


InsertSeparator(int)
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function inserts a Seprator in the list at the specified index. 

**Type:** int= index

..  code-block:: python

	win.Find('combo_1').InsertSeparator(2)  #insert after second item


RemoveItem(int)
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** int= index

..  code-block:: python

	win.Find('combo_1').RemoveItem(2)  #remove third item


Clear()
^^^^^^^

..  topic:: Description

	This function removes all item from the ComboBox list

**Type:** func

..  code-block:: python

	win.Find('combo_1').Clear()


SetEditText(string)
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function sets the Text to appear in the editable Combox Item. 

	``ComboBox must be Editable``

**Type:** func

..  code-block:: python

	ui.ComboBox({'ID':'combo_1', 'Editable': True }),

	win.Find('combo_1').SetEditText('My text')


ClearEditText()
^^^^^^^^^^^^^^^

..  topic:: Description

	This function clears the EditText box in the Combox Item. 

	``ComboBox must be Editable``

**Type:** func

..  code-block:: python

		ui.ComboBox({'ID':'combo_1', 'Editable': True }),

	    win.Find('combo_1').ClearEditText()


Count()
^^^^^^^

..  topic:: Description

	This function returns the number of item in the ComboBox list. 

**Type:** func

..  code-block:: python

    ui.ComboBox({'ID':'combo_1'}),
	win.Find("combo_1").AddItems(["Item 1","Item 2","Item 3"])
	item_count = win.Find('combo_1').Count()
	print(item_count)  # 3


ShowPopup()
^^^^^^^^^^^

..  topic:: Description

	This function opens the ComboBox list to display content

**Type:** func

..  code-block:: python

	win.Find('combo_1').ShowPopup()


HidePopup()
^^^^^^^^^^^

..  topic:: Description

	This function closes the ComboBox list to hide content

**Type:** func

..  code-block:: python

	win.Find('combo_1').HidePopup()


SpinBox
-------

SetRange(int, int)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is setting a Minimum and Maximum value to the SpinBox. 

**Type:** func

..  code-block:: python

	win.Find('spinbox_1').SetRange(0, 4)  #min=0, max=4


StepBy(int)
^^^^^^^^^^^

..  topic:: Description

	This function adding the specified value to the SpinBox.

**Type:** func

..  code-block:: python

	win.Find('spinbox_1').StepBy(2)  #adds 2


StepUp()
^^^^^^^^

..  topic:: Description

	This function is adding the current Step value to the SpinBox (default=1)

**Type:** func

..  code-block:: python

        win.Find('spinbox_1').StepUp()


StepDown()
^^^^^^^^^^

..  topic:: Description

	This function is removing the current Step value to the SpinBox (default=1)

**Type:** func

..  code-block:: python

	win['myspinbox'].StepDown()


SelectAll()
^^^^^^^^^^^

..  topic:: Description

	This function is selecting all the numbers in the SpinBox 

**Type:** func

..  code-block:: python

	win.Find('spinbox_1').SelectAll()


Clear()
^^^^^^^

..  topic:: Description

	This function clears the SpinBox display

**Type:** func

..  code-block:: python

	win.Find('spinbox_1').Clear()



Slider
------

SetRange(int, int)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is setting a Minimum and Maximum value to the Slider. 

**Type:** func

..  code-block:: python

	win.Find('slider_1').SetRange(0, 4)  #min=0, max=4


TriggerAction(string)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['myslider'].TriggerAction(string)


LineEdit
--------

SetSelection(int, int)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is selecting a range of characters in the LineEdit. 

**Type:** func int = index start, index end

..  code-block:: python

	win.Find('le_1').SetSelection(0, 4)  #selects the first 4 characters


HasSelectedText()
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return bool

..  note:: Not tested yet

	win['le_1'].HasSelectedText()


SelectedText()
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return string

..  note:: Not tested yet

	win['le_1'].SelectedText()


SelectionStart()
^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['le_1'].SelectionStart()


SelectAll()
^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].SelectAll()


Clear()
^^^^^^^

..  topic:: Description

	This function is

**Type:** return 

..  note:: Not tested yet

	win['le_1'].Clear()


Cut()
^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Cut()


Copy()
^^^^^^

..  topic:: Description

	This function is

**Type:** return bool

..  note:: Not tested yet

	win['le_1'].Copy()


Paste()
^^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Paste()


Undo()
^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Undo()


Redo()
^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Redo()


Deselect()
^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Deselect()


Insert(string)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Insert('My text')


Backspace()
^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Backspace()


Del()
^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Del()


Home(bool)
^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].Home(True)


End(bool)
^^^^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['le_1'].End(True)


CursorPositionAt(point)
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['le_1'].CursorPositionAt(point)


TextEdit
--------

InsertPlainText(string)
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].InsertPlainText('My text')


InsertHTML(string)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].InsertHTML('<h1>My title</h1>')


Append(string)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].Append('My text')


SelectAll()
^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].SelectAll()


Clear()
^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].Clear()




Cut()
^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].Cut()


Copy()
^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].Copy()


Paste()
^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].Paste()


Undo()
^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].Undo()


Redo()
^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].Redo()


ScrollToAnchor(string)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].ScrollToAnchor('My text')


ZoomIn(int)
^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].ZoomIn(2)


ZoomOut(int)
^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].ZoomOut(2)


EnsureCursorVisible()
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func 

..  note:: Not tested yet

	win['te_1'].EnsureCursorVisible()


MoveCursor(moveOperation, moveMode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** moveOperation = , moveMode =

..  note:: Not tested yet

	win['te_1'].MoveCursor(moveOperation, moveMode)


CanPaste()
^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return bool 

..  note:: Not tested yet

	win['te_1'].CanPaste()


AnchorAt(point)
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return string 

..  note:: Not tested yet

	win['te_1'].AnchorAt(point)


Find(string, findFlags)
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** string= , findFlags= : return bool 

..  note:: Not tested yet

	win['te_1'].Find('my text', findFlags)


TabBar
------

AddTab(strubg)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int 

..  note:: Not tested yet

	win['te_1'].AddTab(strubg)


InsertTab(string)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int 

..  note:: Not tested yet

	win['te_1'].InsertTab('Tab name')


Count()
^^^^^^^

..  topic:: Description

	This function is

**Type:** return int 

..  note:: Not tested yet

	win['te_1'].Count()


RemoveTab(int)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int= Tab index 

..  note:: Not tested yet

	win['te_1'].RemoveTab(1)


MoveTab(int, int)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int=tab index to move  int=tab index destination 

..  note:: Not tested yet

	win['te_1'].MoveTab(0, 2)


Tree
----

AddTopLevelItem(item)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** item= TreeItem

..  note:: Not tested yet

	item = win['mytree'].NewItem()
	item.Text[0] = 'My Text'
	win['mytree'].AddTopLevelItem(item)


InsertTopLevelItem(item)
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** item= TreeItem

..  note:: Not tested yet

	item = win['mytree'].NewItem()
	item.Text[0] = 'My Text'
	win['mytree'].InsertTopLevelItem(item)


SetHeaderLabel(string)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** string= header label

..  note:: Not tested yet

	win['mytree'].SetHeaderLabel('New header')


CurrentColumn()
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['mytree'].CurrentColumn()


SortColumn()
^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['mytree'].SortColumn()


TopLevelItemCount()
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['mytree'].TopLevelItemCount()


CurrentItem()
^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return item

..  note:: Not tested yet

	win['mytree'].CurrentItem()


TopLevelItem(int)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int=   return item

..  note:: Not tested yet

	win['mytree'].TopLevelItem(1)


TakeTopLevelItem(int)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int=   return item

..  note:: Not tested yet

	win['mytree'].TakeTopLevelItem(1)


InvisibleRootItem()
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return item

..  note:: Not tested yet

	win['mytree'].TakeTopLevelItem(1)


HeaderItem()
^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return item

..  note:: Not tested yet

	win['mytree'].HeaderItem()


IndexOfTopLevelItem(item)
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['mytree'].IndexOfTopLevelItem(item)


ItemAbove(item)
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** item=    return item

..  note:: Not tested yet

	win['mytree'].ItemAbove(item)


ItemBelow(item)
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** item=    return item

..  note:: Not tested yet

	win['mytree'].ItemBelow(item)


ItemAt(point)
^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** point=    return item

..  note:: Not tested yet

	win['mytree'].ItemAt(point)


Clear()
^^^^^^^

..  topic:: Description

	This function is

**Type:** 

..  note:: Not tested yet

	win['mytree'].Clear()


VisualItemRect(item)
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return rect

..  note:: Not tested yet

	win['mytree'].VisualItemRect(item)


SetHeaderLabels(list)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** list = 

..  note:: Not tested yet
	
	win['mytree'].SetHeaderLabels(['header1', 'header2'])


SetHeaderItem(item)
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** item = 

..  note:: Not tested yet

	win['mytree'].SetHeaderItem(item)


InsertTopLevelItems(list)
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** list = 

..  note:: Not tested yet

	win['mytree'].InsertTopLevelItems([item1, item2])


AddTopLevelItems(list)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** list = 

..  note:: Not tested yet

	win['mytree'].AddTopLevelItems([item1, item2])


SelectedItems()
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return list

..  note:: Not tested yet

	win['mytree'].SelectedItems()


FindItems(string, flags)
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** string=  , flags=   return list

..  note:: Not tested yet

	win['mytree'].FindItems(string, flags)


SortItems(int, order)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int= , order= 

..  note:: Not tested yet

	win['mytree'].SortItems(0, 'AscendingOrder')


ScrollToItem(item)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** item=

..  note:: Not tested yet

	win['mytree'].ScrollToItem(item)


ResetIndentation()
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['mytree'].ResetIndentation()


SortByColumn(int, order)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int= , order= 

..  note:: Not tested yet

	win['mytree'].SortByColumn(0, 'AscendingOrder')


FrameWidth()
^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['mytree'].FrameWidth()


TreeItem
--------

AddChild(item)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is addind an item as a child of an existing TreeItem. 

**Type:** func

..  code-block:: python

	itm = win.Find('my_tree').NewItem()
	itm.Text[0] = "First cell"
    itm2 = win.Find('my_tree').NewItem()
	itm2.Text[0] = "Child of itm"

    win.Find('my_tree').AddTopLevelItem(itm)

	itm.AddChild(itm2)


InsertChild(item)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['mytreeitem'].InsertChild(item)


RemoveChild(item)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['mytreeitem'].RemoveChild(item)


SortChildren(int, order)
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int= , order= 

..  note:: Not tested yet

	win['mytreeitem'].SortChildren(0, 'AscendingOrder')


InsertChildren(int, list)
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int= , list= 

..  note:: Not tested yet

	win['mytreeitem'].InsertChildren(int, list)


AddChildren(list)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** list= 

..  note:: Not tested yet

	win['mytreeitem'].AddChildren(list)


IndexOfChild(item)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['mytreeitem'].IndexOfChild(item)


Clone()
^^^^^^^

..  topic:: Description

	This function is

**Type:** return item

..  note:: Not tested yet

	win['mytreeitem'].Clone()


TreeWidget()
^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return tree

..  note:: Not tested yet

	win['mytreeitem'].TreeWidget()


Parent()
^^^^^^^^

..  topic:: Description

	This function is

**Type:** return item

..  note:: Not tested yet

	win['mytreeitem'].Parent()


Child(int)
^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int=   return item

..  note:: Not tested yet

	win['mytreeitem'].Child(int)


TakeChild(int)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int=   return item

..  note:: Not tested yet

	win['mytreeitem'].TakeChild(int)


ChildCount()
^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['mytreeitem'].ChildCount()


ColumnCount()
^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return int

..  note:: Not tested yet

	win['mytreeitem'].ColumnCount()


Window
------

Show()
^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win.Show()


Hide()
^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win.Hide()


RecalcLayout()
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win.RecalcLayout()


Dialog
------

Exec()
^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	dialog.Exec()


IsRunning()
^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	dialog.IsRunning()


Done()
^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	dialog.Done()


RecalcLayout()
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet
	
	dialog.RecalcLayout()


Elements can be accessed by the window's FindWindow(id) function, or by assigning them to a variable for later usage, which is more efficient. 
The GetItems() function will return a dictionary of all child elements for ease of access.


..  code-block:: python

	win_itms = win.GetItems()
	win_itms['ElementID'].func()
