UIDispatcher Functions
----------------------

The UIDispatcher object has a few important functions to manage processing of events. The most important are:

	AddWindow(props, children):	Accepts a dictionary of properties and a list of children, returns a Window object
	AddDialog(props, children):	Accepts a dictionary of properties and a list of children, returns a Dialog object
	int RunLoop():				Call when your window is ready to receive user clicks and other events
	ExitLoop(int):				Terminates the event processing, and returns any supplied exit code from RunLoop()

Common usage is to create your window and set up any event handlers, including a Close handler for the window that calls ExitLoop(), then Show() your window and call RunLoop() to wait for user interaction:

..  code-block:: python

	ui = fusion.UIManager
	dispatcher = bmd.UIDispatcher(ui)

	win = dispatcher.AddWindow({ 'ID': 'myWindow' }, [ ui.Label({ 'Text': 'Hello World!' }) ])

	def OnClose(ev):
		dispatcher.ExitLoop()

	win.On.myWindow.Close = OnClose

	win.Show()
	dispatcher.RunLoop()

AddWindow() will also accept a single child without needing a list, or a single dictionary containing both proprties and child elements, for ease of use.

As well as constructing new child elements and layouts, the UIManager also offers a few useful functions:

	FindWindow(ID):						Returns an element with matching ID
	FindWindows(ID):					Returns a list of all elements with matching ID
	QueueEvent(element, event, info):	Calls the element's event handler for 'event', passing it the dictionary 'info'