Layout
======

Additionally, elements can be nested to define layout, using the HGroup and VGroup elements. 
As with Window and other elements, you can pass a single dictionary or list with all properties and children, 
or separate them into a dict of properties and list of children, for convenience:

..  code-block:: python

	winLayout = ui.VGroup([
		ui.Label({ 'Text': "A 2x2 grid of buttons", 'Weight': 1 }),
		
		ui.HGroup({ 'Weight': 5 }, [
			ui.Button({ 'ID': "myButton1",  'Text': "Go" }),
			ui.Button({ 'ID': "myButton2",  'Text': "Stop" }),
			]),
		ui.VGap(2),
		ui.HGroup({ 'Weight': 5 }, [
			ui.Button({ 'ID': "myButtonA",  'Text': "Begin" }),
			ui.Button({ 'ID': "myButtonB",  'Text': "End" }),
			]),
		]),

	win = dispatcher.AddWindow({ 'ID': "myWindow" }, winLayout)


HGap and VGap elements can included for finer spacing control. Note also the Weight attribute, 
which can be applied to most elements to control how they adjust their relative sizes. 

..  note:: 

	A Weight of 0 will use the element's minimum size.
