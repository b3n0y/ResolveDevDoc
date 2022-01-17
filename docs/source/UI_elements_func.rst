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

	Label:				SetSelection(int, int), bool HasSelection(), string SelectedText(), int SelectionStart()
	Button:				Click(), Toggle(), AnimateClick()
	CheckBox:			Click(), Toggle(), AnimateClick()
	ComboBox:			AddItem(string), InsertItem(string), AddItems(list), InsertItems(int, list), InsertSeparator(int), RemoveItem(int), Clear(),
						SetEditText(string), ClearEditText(), Count(), ShowPopup(), HidePopup()
	SpinBox:			SetRange(int, int), StepBy(int), StepUp(), StepDown(), SelectAll(), Clear()
	Slider:				SetRange(int, int), TriggerAction(string)
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
						int ChildCount(), int ColumnCount()
	Window:				Show(), Hide(), RecalcLayout()
	Dialog:				Exec(), IsRunning(), Done(), RecalcLayout()

Elements can be accessed by the window's FindWindow(id) function, or by assigning them to a variable for later usage, which is more efficient. The GetItems() function will return a dictionary of all child elements for ease of access.
