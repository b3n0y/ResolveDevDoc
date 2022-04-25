.. versionadded:: Updated as of 29 March 2022


API Introduction
----------------


In this package, you will find a brief introduction to the Scripting API for DaVinci Resolve Studio. Apart from this README.txt file, this package contains folders containing the basic import
modules for scripting access (DaVinciResolve.py) and some representative examples.

From v16.2.0 onwards, the nodeIndex parameters accepted by SetLUT() and SetCDL() are 1-based instead of 0-based, i.e. 1 <= nodeIndex <= total number of nodes.

**Overview**

As with Blackmagic Design Fusion scripts, user scripts written in Lua and Python programming languages are supported. By default, scripts can be invoked from the Console window in the Fusion page,
or via command line. This permission can be changed in Resolve Preferences, to be only from Console, or to be invoked from the local network. Please be aware of the security implications when
allowing scripting access from outside of the Resolve application.


**Prerequisites**

DaVinci Resolve scripting requires one of the following to be installed (for all users):

- Lua 5.1
- Python 2.7 64-bit
- Python 3.6 64-bit


**Using a script**

DaVinci Resolve needs to be running for a script to be invoked.

For a Resolve script to be executed from an external folder, the script needs to know of the API location. 
You may need to set the these environment variables to allow for your Python installation to pick up the appropriate dependencies as shown below:

  * Mac OS X:
    RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
    RESOLVE_SCRIPT_LIB="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
    PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"

  * Windows:
    RESOLVE_SCRIPT_API="%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting"
    RESOLVE_SCRIPT_LIB="C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll"
    PYTHONPATH="%PYTHONPATH%;%RESOLVE_SCRIPT_API%\Modules\"

  * Linux:
    RESOLVE_SCRIPT_API="/opt/resolve/Developer/Scripting"
    RESOLVE_SCRIPT_LIB="/opt/resolve/libs/Fusion/fusionscript.so"
    PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
    (Note: For standard ISO Linux installations, the path above may need to be modified to refer to /home/resolve instead of /opt/resolve)

As with Fusion scripts, Resolve scripts can also be invoked via the menu and the Console.

On startup, DaVinci Resolve scans the subfolders in the directories shown below and enumerates the scripts found in the Workspace application menu under Scripts. 
Place your script under Utility to be listed in all pages, under Comp or Tool to be available in the Fusion page or under folders for individual pages (Edit, Color or Deliver). Scripts under Deliver are additionally listed under render jobs.
Placing your script here and invoking it from the menu is the easiest way to use scripts. 

  * Mac OS X:
  
    - All users: /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts
    - Specific user:  /Users/<UserName>/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts

  * Windows:

    - All users: %PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts
    - Specific user: %APPDATA%\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts
  
  * Linux:

    - All users: /opt/resolve/Fusion/Scripts  (or /home/resolve/Fusion/Scripts/ depending on installation)
    - Specific user: $HOME/.local/share/DaVinciResolve/Fusion/Scripts

The interactive Console window allows for an easy way to execute simple scripting commands, to query or modify properties, and to test scripts. The console accepts commands in Python 2.7, Python 3.6
and Lua and evaluates and executes them immediately. 
For more information on how to use the Console, please refer to the DaVinci Resolve User Manual.

This example Python script creates a simple project:

..  code-block:: python

    #!/usr/bin/env python
    import DaVinciResolveScript as dvr_script
    resolve = dvr_script.scriptapp("Resolve")
    fusion = resolve.Fusion()
    projectManager = resolve.GetProjectManager()
    projectManager.CreateProject("Hello World")


The resolve object is the fundamental starting point for scripting via Resolve. As a native object, it can be inspected for further scriptable properties - using table iteration and "getmetatable"
in Lua and dir, help etc in Python (among other methods). A notable scriptable object above is fusion - it allows access to all existing Fusion scripting functionality.


**Running DaVinci Resolve in headless mode**

DaVinci Resolve can be launched in a headless mode without the user interface using the -nogui command line option. When DaVinci Resolve is launched using this option, the user interface is disabled.
However, the various scripting APIs will continue to work as expected.


**List and Dict Data Structures**

Beside primitive data types, Resolve's Python API mainly uses list and dict data structures. 

Lists are denoted by [ ... ] and dicts are denoted by { ... } above.

As Lua does not support list and dict data structures, the Lua API implements "list" as a table with indices

* e.g. { [1] = listValue1, [2] = listValue2, ... }.

Similarly the Lua API implements "dict" as a table with the dictionary key as first element

* e.g. { [dictKey1] = dictValue1, [dictKey2] = dictValue2, ... }.
