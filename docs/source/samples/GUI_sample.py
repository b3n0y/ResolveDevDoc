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
color_dict = {'R':0.3, 'G':0.1, 'B':0}
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


bmd = GetModule_fusionscript()
fusion = GetApp("Fusion")
ui = fusion.UIManager
dispatcher = bmd.UIDispatcher(ui)



##____________________GUI SETUP______________________________
def create_main_window():
    # define the window UI layout
    win = dispatcher.AddWindow({
        'ID': "my_window",
        'Geometry': [ 400,200,250,125 ],
        'WindowTitle': 'My Window'
        },
        ui.VGroup([
 
    ui.Tree({ 'ID':'my_tree', 'ColumnCount': 2 })
        ])
    )
    
        

    
    win_items = win.GetItems()
    
    

    # Event handlers
    def OnClose(ev):
        dispatcher.ExitLoop()


    # assign event handlers
    win.On["my_window"].Close = OnClose


    return win, win_items



def initialize():
    #Create windows and declare global variables
    global win, win_items

    win, win_items = create_main_window()
    
    itm = win.Find('my_tree').NewItem()

    itm.Text[0] = "First column"
    itm.Text[1] = "Second column"

    win.Find('my_tree').AddTopLevelItem(itm)
    win.Find('my_tree').ColumnWidth[0] = 200


    # win.Find('my_tree').AddTopLevelItem(itm2)
    # win.Find('my_tree').AddTopLevelItem(itm3)


def main():
    initialize()
    # Main dispatcher loop
    win.Show()
    dispatcher.RunLoop()
    win.Hide()



if __name__ == "__main__":
    main()