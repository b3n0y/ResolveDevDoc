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
* Size()			Returns size
* Pos()				Returns position
* HasFocus()		Returns boolean
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

	This function is selecting all the text in the LineEdit element. 

**Type:** 

..  code-block:: python

	win.Find('le_1').SelectAll()


Clear()
^^^^^^^

..  topic:: Description

	This function deletes all the text in the LineEdit element. 

**Type:** return 

..  code-block:: python

	win.Find('le_1').Clear()


Cut()
^^^^^

..  topic:: Description

	This function will copy to clipboard and remove the selected LineEdit characters. 
	``A selection in the LineEdit is required``

**Type:** 

..  code-block:: python

	win.Find('le_1').SetSelection(0, 4)
	win.Find('le_1').Cut()  #this will cut the first 4 characters
	

Copy()
^^^^^^

..  topic:: Description

	This function will copy to clipboard the selected LineEdit characters.
	``A selection in the LineEdit is required``
 

**Type:** return

..  code-block:: python

	win.Find('le_1').SetSelection(0, 4)
	win.Find('le_1').Copy()  #this will copy the first 4 characters


Paste()
^^^^^^^

..  topic:: Description

	This function paste the clipboard content to the LineEdit element. 

**Type:** 

..  code-block:: python

	win.Find('le_1').Paste()


Undo()
^^^^^^

..  topic:: Description

	This function wil undo the last action made in the TextEdit element. 

**Type:** 

..  code-block:: python

	win.Find('le_1').Undo()


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

	This function will deselect the selected text of the LineEdit element. 

**Type:** 

..  code-block:: python

	win.Find('le_1').Deselect()


Insert(string)
^^^^^^^^^^^^^^

..  topic:: Description

	This function insert the text string at the cursor position in the LineEdit element. 

**Type:** 

..  code-block:: python

	win.Find('le_1').Insert('New Text')


Backspace()
^^^^^^^^^^^

..  topic:: Description

	This function remove the last character from the cursor position in the LineEdit element. 

**Type:** 

..  code-block:: python

	win.Find('le_1').Backspace()


Del()
^^^^^

..  topic:: Description

	This function remove the next character from the cursor position in the LineEdit element. 

**Type:** 

..  code-block:: python

	win.Find('le_1').Del()


Home(bool)
^^^^^^^^^^

..  topic:: Description

	This function is selecting all characters from cursor to beginning when set to True. 

**Type:** 

..  code-block:: python

	win.Find('le_1').Home(True)


End(bool)
^^^^^^^^^

..  topic:: Description

	This function is selecting all characters from cursor to end when set to True. 

**Type:** 

..  code-block:: python

	win.Find('le_1').End(True)


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

	This function insert the text string at the cursor position in the TextEdit element. 


**Type:** func 

..  code-block:: python

	win.Find('te_1').InsertPlainText('New text')


InsertHTML(string)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function insert the HTML code string at the cursor position in the TextEdit element. 

**Type:** func 

..  code-block:: python

	win.Find('te_1').InsertHTML('<h1>My title</h1>')


Append(string)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is adding the string on the next line of the TextEdit box.  

**Type:** func 

..  code-block:: python

	win.Find('te_1').Append('My text')


SelectAll()
^^^^^^^^^^^

..  topic:: Description

	This function is selecting all the text in the TextEdit element. 

**Type:** func 

..  code-block:: python

	win.Find('te_1').SelectAll()



Clear()
^^^^^^^

..  topic:: Description

	This function deletes all the text in the LineEdit element. 

**Type:** func 

..  code-block:: python

	win.Find('te_1').Clear()


Cut()
^^^^^

..  topic:: Description

	This function will copy to clipboard and remove the selected LineEdit characters. 
	``A selection in the LineEdit is required``

**Type:** 

..  code-block:: python

	win.Find('te_1').SetSelection(0, 4)
	win.Find('te_1').Cut()  #this will cut the first 4 characters
	

Copy()
^^^^^^

..  topic:: Description

	This function will copy to clipboard the selected characters.
	``A selection in the TextEdit is required``
 

**Type:** return

..  code-block:: python

	win.Find('te_1').SelectAll()
	win.Find('te_1').Copy()  #this will copy all text to clipbboard


Paste()
^^^^^^^

..  topic:: Description

	This function paste the clipboard content to the cursor position in the TextEdit element. 

**Type:** 

..  code-block:: python

	win.Find('te_1').Paste()


Undo()
^^^^^^

..  topic:: Description

	This function wil undo the last action made on each line of the TextEdit element. 

**Type:** 

..  code-block:: python

	win.Find('te_1').Undo()


Redo()
^^^^^^

..  topic:: Description

	This function is

**Type:** 

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

	This function is increase the displayed text size by defined number. 

**Type:** func 

..  code-block:: python

	win.Find('te_1').ZoomIn(14)  #will display text with 14pt size


ZoomOut(int)
^^^^^^^^^^^^

..  topic:: Description

	This function is decrease the displayed text size by defined number. 

**Type:** func 

..  note:: Not tested yet

	win.Find('te_1').ZoomOut(2)  #will reduce text size of 2pt


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

AddTab(string)
^^^^^^^^^^^^^^

..  topic:: Description

	This function adds a Tab with specified name to the TabBar

**Type:** string

..  code-block:: python

	win.Find('tabbar_1').AddTab('Tab 1')


InsertTab(int, string)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function insert a Tab in the TabBar at specified index. 

**Type:** returns tab index (int)

..  code-block:: python

	win.Find('tabbar_1').InsertTab(0, 'Tab 0')  #insert tab at index 0


Count()
^^^^^^^

..  topic:: Description

	This function counts the number of Tabs

**Type:** return number of Tab 

..  code-block:: python

	print(win.Find('tabbar_1').Count())


RemoveTab(int)
^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** int= Tab index 

..  code-block:: python

	win.Find('tabbar_1').RemoveTab(0)  #remove first tab


MoveTab(int, int)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function moves a Tab to another position

**Type:** int=tab index to move  int=tab index destination 

..  code-block:: python

	win.Find('tabbar_1').MoveTab(1, 0)  #move second tab to first position


Tree
----

AddTopLevelItem(item)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function adds the item at the top of the Tree.

**Type:** item= TreeItem

..  code-block:: python

	item = win.Find('tree_1').NewItem()
	item.Text[0] = 'My Text'
	win.Find('tree_1').AddTopLevelItem(item)


InsertTopLevelItem(int, item)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function insert the item at specified position. 

**Type:** int= index, item= TreeItem  

..  code-block:: python

	item = win.Find('tree_1').NewItem()
	item.Text[0] = 'Insert'
	win.Find('tree_1').InsertTopLevelItem(0, item)


SetHeaderLabel(string)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is setting the name for the first header

**Type:** string= header label

..  code-block:: python

	win.Find('tree_1').SetHeaderLabel('New header')


CurrentColumn()
^^^^^^^^^^^^^^^

..  topic:: Description

	This function returns the selected column index. 

**Type:** returns int

..  code-block:: python

	print(win.Find('tree_1').CurrentColumn())


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

	This function return the number of Item in the Tree. (row)

**Type:** returns

..  code-block:: python

	print(win.Find('tree_1').TopLevelItemCount())


CurrentItem()
^^^^^^^^^^^^^

..  topic:: Description

	This function returns the selected Item in the Tree (row)

**Type:** return the UITreeItem

..  code-block:: python

	print(win.Find('tree_1').CurrentItem().Text[0])  #print first column Text of the selected TreeItem (row)


TopLevelItem(int)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function return the UITreeItem at the specified index. (row) 

**Type:** int= index 

..  code-block:: python

	print(win.Find('tree_1').TopLevelItem(1).Text[0])  #will print the Text of the second Item (row), first column


TakeTopLevelItem(int)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function removes and returns the UITreeItem at the specified index. (row) 

**Type:** int=   return item

..  code-block:: python

	win.Find('tree_1').TakeTopLevelItem(1)


InvisibleRootItem()
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return item

..  note:: Not tested yet

	win['mytree'].InvisibleRootItem()


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

	This function returns the index of the specified UITreeItem.

**Type:** return int

..  code-block:: python

	some_item = win.Find('tree_1').TopLevelItem(1)
	print(win.Find('tree_1').IndexOfTopLevelItem(some_item))  #print 1


ItemAbove(item)
^^^^^^^^^^^^^^^

..  topic:: Description

	This function returns the UITreeItem above the specified UITreeItem. 

**Type:** item= UITreeItem   returns UITreeItem

..  code-block:: python

	some_item = win.Find('tree_1').TopLevelItem(1)
	item_above = win.Find('tree_1').ItemAbove(some_item)  #item_above is UITreeItem at index 0


ItemBelow(item)
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** item= UITreeItem   returns UITreeItem

..  code-block:: python

	some_item = win.Find('tree_1').TopLevelItem(0)
	item_below = win.Find('tree_1').ItemBelow(some_item)  #item_below is UITreeItem at index 1


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

	This function empty all data from the Tree. 

**Type:** 

..  code-block:: python

	win.Find('tree_1').Clear()


VisualItemRect(item)
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function returns the rectangle on the viewport occupied by the item 

**Type:** returns {int x, int y, int width, int height}

..  code-block:: python

	some_item = win.Find('tree_1').TopLevelItem(1)
	print(win.Find('tree_1').VisualItemRect(some_item))   #print {1: 20, 2: 20, 3: 208, 4: 20}


SetHeaderLabels(list)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function sets the labels header for multiple columns

**Type:** list of string

..  code-block:: python
	
	win.Find('tree_1').SetHeaderLabels(['header1', 'header2'])


SetHeaderItem(item)
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** item = 

..  note:: Not tested yet

	win['mytree'].SetHeaderItem(item)


InsertTopLevelItems(int, list)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function inserts a list of UITreeItems from a list at the specified index. 

**Type:** int= index to insert items, list = list of UITreeItems

..  code-block:: python

	item1 = win.Find('tree_1').NewItem()
	item1.Text[0] = 'name1'
	item2 = win.Find('tree_1').NewItem()
	item2.Text[0] = 'name2'
	win.Find('tree_1').InsertTopLevelItems(0, [item1, item2])  #insert items at index 0


AddTopLevelItems(list)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function adds the list of TreeItems at the end of the Tree. 

**Type:** list = list of TreeItem

..  code-block:: python

	item1 = win.Find('tree_1').NewItem()
	item1.Text[0] = 'name1'
	item2 = win.Find('tree_1').NewItem()
	item2.Text[0] = 'name2'
	win.Find('tree_1').AddTopLevelItems([item1, item2])


SelectedItems()
^^^^^^^^^^^^^^^

..  topic:: Description

	This function is

**Type:** return list of all selected UITreeItems

..  note:: Not tested yet

	win['mytree'].SelectedItems()


FindItems(string, flags, column)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function searches for a string with a dictionary or conditions in a specified column index. 
	
flags:

* 'MatchExactly' : bool
* 'MatchFixedString' : bool
* 'MatchContains' : bool
* 'MatchStartsWith' : bool
* 'MatchEndsWith' : bool
* 'MatchCaseSensitive' : bool
* 'MatchRegExp' : bool
* 'MatchWildcard' : bool
* 'MatchWrap' : bool
* 'MatchRecursive' : bool
    

**Type:** string= text to find , flags= dict, column = int  Returns list of UITreeItems

..  code-block:: python

	found_item = win.Find('tree_1').FindItems("*",
	{
		'MatchExactly' : False,
		'MatchFixedString' : False,
		'MatchContains' : False,
		'MatchStartsWith' : False,
		'MatchEndsWith' : False,
		'MatchCaseSensitive' : False,
		'MatchRegExp' : False,
		'MatchWildcard' : True,
		'MatchWrap' : False,
		'MatchRecursive' :True,
	}, 0)
	# print all items of column 0 matching conditions, * is used as a wildcard


SortItems(int, string)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is sorting the TreeItems of the specified column index based on the specified ordering.  

	`Check out the qt5 documentation for more details <https://doc.qt.io/qt-5/qtreewidget.html#sortItems>`_
	
order:

* 'AscendingOrder' : The items are sorted ascending e.g. starts with 'AAA' ends with 'ZZZ' in Latin-1 locales
* 'DescendingOrder' : The items are sorted descending e.g. starts with 'ZZZ' ends with 'AAA' in Latin-1 locales
`Check out the qt5 documentation for more details <https://doc.qt.io/qt-5/qt.html#SortOrder-enum>`_


**Type:** int= column index, string= sorting option

..  code-block:: python

	win.Find('tree_1').SortItems(0, 'AscendingOrder')


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


SortByColumn(int, string)
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function Sorts the model by the values in the given column and order.

	`Check out the qt5 documentatatoin for more details <https://doc.qt.io/qt-5/qtreeview.html#sortByColumn>`_

order:

* 'AscendingOrder' : The items are sorted ascending e.g. starts with 'AAA' ends with 'ZZZ' in Latin-1 locales
* 'DescendingOrder' : The items are sorted descending e.g. starts with 'ZZZ' ends with 'AAA' in Latin-1 locales


**Type:** int= column index, string= order 

..  code-block:: python

	win.Find('tree_1').SortByColumn(0, 'AscendingOrder')


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

	This function is adding an item as a child to an existing TreeItem. 

**Type:** func

..  code-block:: python

	itm = win.Find('my_tree').NewItem()
	itm.Text[0] = "First cell"
    itm2 = win.Find('my_tree').NewItem()
	itm2.Text[0] = "Child of itm"

    win.Find('my_tree').AddTopLevelItem(itm)

	itm.AddChild(itm2)


InsertChild(int, item)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is inserting an item as a child to an existing TreeItem to a specified index.  

**Type:** func

..  code-block:: python

        parent = win.Find('tree_1').NewItem()
        parent.Text[0] = 'Text A'
        child = win.Find('tree_1').NewItem()
        child.Text[0] = 'Text B'
        win.Find('tree_1').AddTopLevelItem(parent)
        
        parent.InsertChild(0, child)


RemoveChild(item)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function remove the child of the UITreeItem.

**Type:** func

..  code-block:: python

	parent.RemoveChild(child)        


SortChildren(int, order)
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function is sorting the Child of UITreeItem of the specified column index based on the specified ordering.  

order:

* 'AscendingOrder' : The items are sorted ascending e.g. starts with 'AAA' ends with 'ZZZ' in Latin-1 locales
* 'DescendingOrder' : The items are sorted descending e.g. starts with 'ZZZ' ends with 'AAA' in Latin-1 locales


**Type:** int= column index, string= order 

..  code-block:: python

	parent.SortChildren(0, 'AscendingOrder')


InsertChildren(int, list)
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function inserts a list of UITreeItem as child of a parent UITreeItem at specified index. 

**Type:** int= , list= 

..  code-block:: python

	parent.InsertChildren(0, [child, child2]) 


AddChildren(list)
^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function adds a list of UITreeItem as child of a parent UITreeItem. 

**Type:** list= [UITreeItem, ...]

..  code-block:: python

	parent.AddChildren([child, child2])


IndexOfChild(item)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	This function returns the index of the specified UITreeItem child. 

**Type:** return int

..  code-block:: python

	print(parent.IndexOfChild(child2))  #print 1 for second child


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

	This function returns the UITreeItem parent of the specified UITreeItem child. 

**Type:** return item

..  code-block:: python

	print(child.Parent())


Child(int)
^^^^^^^^^^

..  topic:: Description

	This function returns the UITreeItem child at specified index of the UITreeItem parent. 

**Type:** int=   return item

..  code-block:: python

	print(parent.Child(0))  #the UITreeItem child at index 0


TakeChild(int)
^^^^^^^^^^^^^^

..  topic:: Description

	This function removes and returns the child UITreeItem at specified index.  

**Type:** int=index   return item

..  code-block:: python

	removed_child = parent.TakeChild(0)


ChildCount()
^^^^^^^^^^^^

..  topic:: Description

	This function returns the child count of the parent UITreeItem. 

**Type:** return int

..  code-block:: python

	print(parent.ChildCount())


ColumnCount()
^^^^^^^^^^^^^

..  topic:: Description

	This function returns the number of column of a UITreeItem containing data.

**Type:** return int

..  code-block:: python

	print(parent.ColumnCount())



Window
------

Show()
^^^^^^

..  topic:: Description

	This function is showing the window to the user. 

**Type:** func

..  code-block:: python

	win.Show()


Hide()
^^^^^^

..  topic:: Description

	This function is hiding the window. 

**Type:** func

..  code-block:: python

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


Timer
-----

Start()
^^^^^^^

..  topic:: Description

	This function starts the Timer element. 

**Type:** func

..  note:: Not tested yet
	
	ui.Timer({ 'ID': 'MyTimer', 'Interval': 1000 })  # 1000 millisecs
    MyTimer.Start()
	dispatcher['On']['Timeout'] = OnTimer  #this create a loop each 1000ms


Stop()
^^^^^^

..  topic:: Description

	This function stops the Timer element. 

**Type:** func

..  note:: Not tested yet
	
    MyTimer.Stop()
