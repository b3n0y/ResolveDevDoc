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


	LineEdit:			SetSelection(int, int), bool HasSelectedText(), string SelectedText(), int SelectionStart(), SelectAll(), Clear(), Cut(), Copy(), Paste(),
						Undo(), Redo(), Deselect(), Insert(string), Backspace(), Del(), Home(bool), End(bool), int CursorPositionAt(point)
	TextEdit:			InsertPlainText(string), InsertHTML(string), Append(string), SelectAll(), Clear(), Cut(), Copy(), Paste(), Undo(), Redo(), 
						ScrollToAnchor(string), ZoomIn(int), ZoomOut(int), EnsureCursorVisible(), MoveCursor(moveOperation, moveMode), bool CanPaste(),
						string AnchorAt(point), bool Find(string, findFlags)
	TabBar:				int AddTab(strubg), int InsertTab(string), int Count(), RemoveTab(int), MoveTab(int, int)
	Tree:				AddTopLevelItem(item), InsertTopLevelItem(item), SetHeaderLabel(string), int CurrentColumn(), int SortColumn(),
						int TopLevelItemCount(), item CurrentItem(), item TopLevelItem(int), item TakeTopLevelItem(int), item InvisibleRootItem(),
						item HeaderItem(), int IndexOfTopLevelItem(item), item ItemAbove(item), item ItemBelow(item), item ItemAt(point), 
						Clear(), rect VisualItemRect(item), SetHeaderLabels(list), SetHeaderItem(item), InsertTopLevelItems(list), AddTopLevelItems(list),
						list SelectedItems(), list FindItems(string, flags), SortItems(int, order), ScrollToItem(item), ResetIndentation(), 
						SortByColumn(int, order), int FrameWidth()
	TreeItem:			AddChild(item), InsertChild(item), RemoveChild(iitem), SortChildren(int, order), InsertChildren(int, list), AddChildren(list),
						int IndexOfChild(item), item Clone(), tree TreeWidget(), item Parent(), item Child(int), item TakeChild(int),
						int ChildCount(), int ColumnCount() NewItem()
	Window:				Show(), Hide(), RecalcLayout()
	Dialog:				Exec(), IsRunning(), Done(), RecalcLayout()


Elements can be accessed by the window's FindWindow(id) function, or by assigning them to a variable for later usage, which is more efficient. 
The GetItems() function will return a dictionary of all child elements for ease of access.


..  code-block: python

	win_itms = win.GetItems()
	win_itms['ElementID'].func()
