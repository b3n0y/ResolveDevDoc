#!/usr/local/bin/python3

import os
import sys
import json
from get_resolvepm import *


##################################################
__author__ = "Ben"
__version__ = "1.0"
__status__ = "Dev"
"""

- 1.5: add framerate conversion preference, update color in win_prefs

"""
##################################################

#STYLESHEETS
default_css_label_color = 'rgb(255, 99, 71)'
# css_label_color = 'Tomato'

home_dir = os.path.expanduser("~")

css_prefs = f"""
color: rgb(205, 205, 225); 
font-family: Arial; 
font-weight: bold; 
font-size: 14px;
"""

# Get Resolve app to get projet and timeline info
try:
    resolve = GetApp("Resolve")
    projectManager = resolve.GetProjectManager()
    currentProject = projectManager.GetCurrentProject()
    currentTimeline = currentProject.GetCurrentTimeline()
    projectFPS = currentProject.GetSetting('timelineFrameRate')
    project_name = currentProject.GetName()
except AttributeError as e:
    print("Please open a Davinci Resolve")
    sys.exit(0)

try:
    startFrame = currentTimeline.GetStartFrame()
    print("Project name: " + project_name)
    print("Timeline name: " + currentTimeline.GetName())
    print("Start frame is: " + str(startFrame))
    print("Timeline framerate: " + str(projectFPS))

except AttributeError as e:
    print("Please open a project")
    sys.exit(0)

bmd = GetModule_fusionscript()
fusion = GetApp("Fusion")
ui = fusion.UIManager
dispatcher = bmd.UIDispatcher(ui)



##____________________GUI SETUP______________________________
def create_main_window():
    # define the window UI layout
    win = dispatcher.AddWindow({
        'ID': "tc_display",
        'Geometry': [ 400,200,225,100 ],
        'WindowTitle': "Timecode Display v" + __version__,
        'BackgroundColor': {"R":0.1, "G":0.1, "B":0.2, "A":0.3}
        },
        ui.VGroup([
            ui.Label({ 'ID': 'timecodeID', 'Text': 'my text',
                'Weight': 0,
                'StyleSheet' : update_css_label()
            }),
            ui.Button({ 'ID': 'open_prefs_btn', 'Text': u"\u2699",
                'Weight': 0,
                'StyleSheet' : css_prefs
            }),
        ])
    )
    win_items = win.GetItems()

    # Event handlers
    def OnClose(ev):
        dispatcher.ExitLoop()


    # assign event handlers
    win.On["tc_display"].Close = OnClose


    return win, win_items



def initialize():
    #Create windows and declare global variables
    global win, win_items

    win, win_items = create_main_window()
        
    
def main():
    initialize()
    # Main dispatcher loop
    win.Show()
    dispatcher.RunLoop()
    win.Hide()



if __name__ == "__main__":
    main()