#!/usr/local/bin/python3

from itertools import count
import os
import sys
import time
import json
from time import time
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
        'WindowTitle': 'My Window',
        },
        ui.VGroup([
            ui.Tree({'ID':'tree_1', 'ColumnCount': 2}),
            ui.Button({'ID':'button_1', 'Text': "run func" })
        ])      
    )
    
    # 'Events': {'ItemEntered': True} 
        
    win_items = win.GetItems()


    # Event handlers
    def OnClose(ev):
        dispatcher.ExitLoop()
         

    def OnClicked(ev):
        parent = win.Find('tree_1').NewItem()
        parent.Text[0] = 'Text A'
        child = win.Find('tree_1').NewItem()
        child.Text[0] = 'Text B'

        child2 = win.Find('tree_1').NewItem()
        child2.Text[0] = '123Text'
        child2.Text[1] = '123Text'
        

        parent.AddChildren([child, child2])

        win.Find('tree_1').AddTopLevelItem(parent)
        
        
    win.On["my_window"].Close = OnClose
    win.On["button_1"].Clicked = OnClicked

    return win, win_items



def initialize():
    #Create windows and declare global variables
    global win, win_items

    win, win_items = create_main_window()
    
    
    item = win.Find('tree_1').NewItem()
    item.Text[0] = 'My Text'
    win.Find('tree_1').AddTopLevelItem(item)

    item2 = win.Find('tree_1').NewItem()
    item2.Text[0] = 'My 2'
    item2.Text[1] = 'Myff 2'
    
    item.AddChild(item2)
    # win.Find('tree_1').AddTopLevelItem(item2)
    
    # for i in range(10):
    #     item = win.Find('tree_1').NewItem()
    #     item.Text[0] = str(i) + 'col1'
    #     item.Text[1] = str(i) + 'col2'

    #     win.Find('tree_1').AddTopLevelItem(item)
   
    # win.Find("combo_1").AddItems(["Item 1","Item 2","Item 3"])

    # win.Find("combo_1").AddItems(["Blue","Cyan","Green","Yellow","Red","Pink","Purple","Fuchsia","Rose","Lavender","Sky","Mint","Lemon","Sand","Cocoa","Cream"])

    # win.Find('tabbar_1').AddTab('Tab1')
    # win.Find('tabbar_1').AddTab('Tab2')

    # print(win.Find('tabbar_1').TabText[0])


    # itm = win.Find('tree_1').NewItem()
    # itm2 = win.Find('tree_1').NewItem()
    # itm2.Text[0] = "Child of itm"


    # itm.Text[0] = "First column"
    # itm.Text[1] = "Second column"

    # win.Find('tree_1').AddTopLevelItem(itm)
    # win.Find('tree_1').ColumnWidth[0] = 200
    # itm.AddChild(itm2)


    # win.Find('tree_1').AddTopLevelItem(itm2)


def main():
    initialize()
    # Main dispatcher loop
    win.Show()
    dispatcher.RunLoop()
    win.Hide()



if __name__ == "__main__":
    main()