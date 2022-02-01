.. versionadded::  Updated as of 25 August, 2020


In this package, you will find a brief introduction to the Workflow Integration Plugins support for DaVinci Resolve Studio. Apart from this README.txt file, this package contains following folders:
Examples: containing some representative sample plugin, and a sample script.
Scripts: containing some sample workflow scripts to interact with Resolve.


**Overview**

DaVinci Resolve Studio now supports Workflow Integration Plugins to be loaded and communicate with Resolve. Resolve can run one or more Workflow Integration Plugins at the same time.
Users can write their own Workflow Integration Plugin (an Electron app) which could be loaded into DaVinci Resolve Studio. To interact with Resolve, Resolve's JavaScript APIs can be used from the plugin.

Alternatively, a Python or Lua script can be invoked, with the option of a user interface built with Resolve's built-in Qt-based UIManager, or with an external GUI manager. See the "Sample Workflow Integration Script" section below for details.


**Sample Workflow Integration Plugin**

A sample Workflow Integration Plugin is available in the "Examples/SamplePlugin" directory. In order for Resolve to register this plugin, this directory needs to be copied to 'Workflow Integration Plugins' root directory (mentioned in below section).
Once a plugin is registered, plugin can be loaded from UI sub-menu under 'Workspace->Workflow Integrations'. This will load the plugin and show the plugin HTML page in a separate window.

Sample plugin helps to understand how a plugin should be structured and how it works with Resolve. Please refer to the directory/file structure, manifest file info, plugin loading, JavaScript API usage examples, etc.
This sample plugin and scripts demonstrates few basic scriptable JavaScript API usages to interact with Resolve.


**Loading Workflow Integration Plugin**

On startup, DaVinci Resolve Studio scans the Workflow Integration Plugins root directory and enumerates all plugin modules. For each valid plugin module, it creates a UI sub-menu entry under 'Workspace->Workflow Integrations' menu.
DaVinci Resolve Studio reads the basic details of the plugin from its manifest.xml file during load time. Once plugin is loaded, user can click on the 'Workflow Integrations' sub-menu to load the corresponding plugin.


**Workflow Integration Plugin directory structure**

..  code-block:: javascript

	com.<company>.<plugin_name>/
		package.js
		main.js
		index.html
		manifest.xml
		node_modules/
			<Node.js modules>
		js/
			<supporting js files>
		css/
			<css files containing styling info>
		img/
			<image files>


**Workflow Integration Plugins root directory**

User should place their Workflow Integration Plugin under the following directory:

.. note::

   Mac OS X:
   "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Workflow Integration Plugins/"

   Windows:
   "%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Workflow Integration Plugins\"


**Supported platforms**

* Plugins: Windows, Mac OS X (not supported on Linux currently)
* Scripts: Windows, Mac OS X, Linux


**Using scriptable JavaScript API**

Scriptable JavaScript API execution happens under HTML environment like any typical website. 
Once HTML page is loaded it can execute scriptable JavaScript API as needed (like clicking on a button, etc.)

This example JavaScript snippet creates a simple project in DaVinci Resolve Studio:

..  code-block:: javascript

    const WorkflowIntegration = require('./WorkflowIntegration.node');
    isInitialized = WorkflowIntegration.Initialize('com.blackmagicdesign.resolve.sampleplugin');
    if (isInitialized) {
        resolve = WorkflowIntegration.GetResolve();
        resolve.GetProjectManager().CreateProject("Hello World");
    }

The resolve object is the fundamental starting point for scripting via Resolve. 
As a native object, it can be inspected for further scriptable properties and functions in JavaScript.


**WorkflowIntegration module API**

To interact with Resolve you need to use 'WorkflowIntegration.node' Node.js module file in your plugin app. Below are the WorkflowIntegration (module) JavaScript API functions to communicate with Resolve.


**WorkflowIntegration**

* Initialize(<pluginId>)                          --> Bool               # Returns true if initialization is successful, false otherwise. <pluginId> is the unique plugin id string configured in the manifest.xml file.
* GetResolve()                                    --> Resolve            # Returns Resolve object.
* RegisterCallback(callbackName, callbackFunc)    --> Bool               
  
  * Returns true if input callback name/function is registered successfully, false otherwise.
  * 'callbackName' should be a valid supported callback string name (refer to the below section 'Supported callbacks').
  * 'callbackFunc' should be a valid JavaScript function without any arguments.

* DeregisterCallback(callbackName)                --> Bool               # Returns true if input callback name is deregistered successfully, false otherwise.
* CleanUp()                                       --> Bool               # Returns true if cleanup is successful, false otherwise. This should be called during plugin app quit.
* SetAPITimeout(valueInSecs)                      --> Bool
  
  * By default, apis dont timeout. In order to enable timeout, set a non-zero positive integer value in the arg 'valueInSecs'.
  * Setting it to 0 will disable timeout. This function will return true if the timeout is set/reset successfully.


**Supported callbacks**

* 'RenderStart'
* 'RenderStop'

Please note that there is no console based support for JavaScript API.


**Sample Workflow Integration Script**

A sample Workflow Integration Python script is also available in the "Examples" directory. In order for Resolve to register this script, it needs to be copied to the 'Workflow Integration Plugins' root directory (mentioned in the above section).

Once a script is registered, it can be also loaded from the 'Workspace' menu, under 'Workflow Integrations'. 
This will invoke the script and show the sample UIManager window.

Workflow Integration scripts work similarly to other scripts in Resolve, and use the same scripting API. 
This example script provides a basic introduction into creating a popup Workflow application using a UIManager window, with simple layout of text fields and buttons, and event handlers to dispatch functions for integration with the user's facility. 
Alternatively, third-party UI managers such PyQt may be used instead, or no GUI at all.

When launched by Resolve, plugin scripts are automatically provided with 'resolve' and 'project' variables for immediate and easy access to Resolve's scripting API. 
Additional third-party modules may be imported for access to asset-management systems as desired.


**UIManager Introduction**

There are two main objects needed to manage a window, the UIManager that handles layout, and the UIDispatcher that manages interaction events, accessed as follows:

..  code-block:: python

	ui = fusion.UIManager()
	dispatcher = bmd.UIDispatcher(ui)

Windows are created with the the UIDispatcher, passing a dictionary of attributes like ID and Text, with GUI elements in nested layouts all created with the UIManager.
