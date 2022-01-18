Functions
---------

Most elements have functions that can be called from them as well:

	Show()
	Hide()
	Raise()
	Lower()
	Close()				Returns boolean
	Find(ID)			Returns child element with matching ID
	GetChildren()		Returns list
	AddChild(element)
	RemoveChild(element)
	SetParent(element)
	Move(point)
	Resize(size)
	Size()				Returns size
	Pos()				Returns position
	HasFocus()			Returns boolean
	SetFocus(reason)	Accepts string "MouseFocusReason", "TabFocusReason", "ActiveWindowFocusReason", "OtherFocusreason", etc
	FocusWidget()		Returns element
	IsActiveWindow()	Returns boolean
	SetTabOrder(element)
	Update()
	Repaint()
	SetPaletteColor(r,g,b)
	QueueEvent(name, info)  Accepts event name string and dictionary of event attributes
	GetItems()			Returns dictionary of all child elements

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

	This function is

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].AddItem('Item Name')


InsertItem(string)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].InsertItem('Item Name')


AddItems(list)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].AddItems(['Item1', 'Item2'])


InsertItems(int, list)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** int= index, list=[string]

..  note:: Not tested yet

	win['mycombobox'].InsertItems(2, ['Item1', 'Item2'])


InsertSeparator(int)
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** int= index

..  note:: Not tested yet

	win['mycombobox'].InsertSeparator(2)


RemoveItem(int)
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** int= index

..  note:: Not tested yet

	win['mycombobox'].RemoveItem(2)


Clear()
^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].Clear()


SetEditText(string)
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].SetEditText('My text')


ClearEditText()
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].ClearEditText()


Count()
^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].Count()


ShowPopup()
^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].ShowPopup()


HidePopup()
^^^^^^^^^^^

..  topic:: Description

	This function is 

**Type:** func

..  note:: Not tested yet

	win['mycombobox'].HidePopup()


SpinBox
-------

SetRange(int, int)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['myspinbox'].SetRange(0, 2)


StepBy(int)
^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['myspinbox'].StepBy(2)


StepUp()
^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['myspinbox'].StepUp()


StepDown()
^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['myspinbox'].StepDown()


SelectAll()
^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['myspinbox'].SelectAll()


Clear()
^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['myspinbox'].Clear()


Slider
------

SetRange(int, int)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** func

..  note:: Not tested yet

	win['myslider'].SetRange(0, 2)


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

	This function is

**Type:** func int = index start, index end

..  note:: Not tested yet

	win['le_1'].SetSelection(0, 2)


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

	This function is

**Type:** func

..  note:: Not tested yet
	win['mytreeitem'].AddChild(item)


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
	win['mytree'].SortChildren(0, 'AscendingOrder')


InsertChildren(int, list)
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int= , list= 

..  note:: Not tested yet
	win['mytree'].InsertChildren(int, list)


AddChildren(list)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** list= 

..  note:: Not tested yet
	win['mytree'].AddChildren(list)




	TreeItem:			int IndexOfChild(item), item Clone(), tree TreeWidget(), item Parent(), item Child(int), item TakeChild(int),
						int ChildCount(), int ColumnCount() NewItem()
	Window:				Show(), Hide(), RecalcLayout()
	Dialog:				Exec(), IsRunning(), Done(), RecalcLayout()


Elements can be accessed by the window's FindWindow(id) function, or by assigning them to a variable for later usage, which is more efficient. 
The GetItems() function will return a dictionary of all child elements for ease of access.


..  code-block: python

	win_itms = win.GetItems()
	win_itms['ElementID'].func()
