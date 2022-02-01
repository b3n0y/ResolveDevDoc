#!/usr/local/bin/python3

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
    Workpage to test GUI elements

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
    media_storage = resolve.GetMediaStorage()
    
    
    currentProject = projectManager.GetCurrentProject()
    gallery = currentProject.GetGallery()
    media_pool = currentProject.GetMediaPool()
    current_timeline = currentProject.GetCurrentTimeline()
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
            # ui.Tree({'ID':'tree_1', 'ColumnCount': 2}),
            ui.Tree({ 'ID':'tree_1', 'IconSize': [20,20] }),

            # ui.Button({'ID': 'ok_btn',  'Icon': ui.Icon({'File': r"UserData:/Scripts/images/csv.png"}), 'IconSize': [40, 40]})
        ])      
    )
    
    # 'Events': {'ItemEntered': True} 
        
    win_items = win.GetItems()


    # Event handlers
    def OnClose(ev):
        dispatcher.ExitLoop()
         

    def OnClicked(ev):
        root_folder = media_pool.GetRootFolder()
        folder_list = root_folder.GetSubFolderList()
        clip_list = root_folder.GetClipList()
        # media_pool.CreateTimelineFromClips('My Amazing Timeline', [{"mediaPoolItem":clip_list[0], "startFrame": 0, "endFrame": 10}, {"mediaPoolItem":clip_list[1], "startFrame": 0, "endFrame": 10}])

        # first_timeline =  currentProject.GetTimelineByIndex(1)
        # second_timeline = currentProject.GetTimelineByIndex(2)
        timeline_items = current_timeline.GetItemListInTrack("video", 1)
        mediapool_item = timeline_items[0].GetMediaPoolItem()

        current_still_album = gallery.GetCurrentStillAlbum()
        stills = current_still_album.GetStills()
        current_still_album.ExportStills([stills[0], stills[1]], '/Users/benbro/Desktop/', 'stills_ProjectA_', 'dpx')

        
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

    # item2 = win.Find('tree_1').NewItem()
    # item2.Text[0] = 'My 2'
    # item2.Text[1] = 'Myff 2'
    
    # item.AddChild(item2)
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