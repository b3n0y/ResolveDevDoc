#!/usr/local/bin/python3

import os
import sys
import json
from modules.timecode import Timecode
from modules.get_resolvepm import *


##################################################
__author__ = "Ben"
__version__ = "1.5"
__status__ = "Dev"
"""

- 1.5: add framerate conversion preference, update color in win_prefs
- 1.4: add color preference
- 1.3: add initialize and GUI in main
- 1.2: add stylesheet to label using CSS formatting
- 1.1: add ui.Timer to update timecode each 1000ms
- 1.0: start from recolorize 1.3

"""
##################################################

#STYLESHEETS
default_css_label_color = 'rgb(255, 99, 71)'
# css_label_color = 'Tomato'

home_dir = os.path.expanduser("~")
prefs_file = home_dir + r'/Library/Containers/com.blackmagic-design.DaVinciResolveAppStore/Data/Library/Application Support/Fusion/Settings/timecode_display.json'

def rgb2decimal(rgb_value):
    #255=1.0
    #RGB_value= x
    return rgb_value/255

def decimal2rgb(decimal_value):
    return int(decimal_value * 255)

def update_css_label(css_label_color=default_css_label_color):
    css_label = f"""
    color: {css_label_color}; 
    font-family: Impact; 
    font-weight: bold; 
    font-size: 42px;
    """
    return css_label

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



def convert_tc(target_fps):
    #using the project FPS as source, convert the current timecode to specified target FPS
    source_fps = projectFPS
    current_timecode = currentTimeline.GetCurrentTimecode()
    timecode_obj = Timecode(projectFPS, start_timecode=current_timecode)
    
    timecode_obj.frames = int(timecode_obj.frames * (target_fps/source_fps))
    timecode_obj.framerate = target_fps
    return Timecode.tc_to_string(timecode_obj, timecode_obj.hrs, timecode_obj.mins, timecode_obj.secs, timecode_obj.frs)


##____________________GUI SETUP______________________________
def create_main_window():
    # define the window UI layout
    win_timecode = dispatcher.AddWindow({
        'ID': "tc_display",
        'Geometry': [ 400,200,225,100 ],
        'WindowTitle': "Timecode Display v" + __version__,
        'BackgroundColor': {"R":0.1, "G":0.1, "B":0.2, "A":0.3}
        },
        ui.VGroup([
            ui.Label({ 'ID': 'timecodeID', 'Text': convert_tc(projectFPS),
                'Weight': 0,
                'StyleSheet' : update_css_label()
            }),
            ui.Button({ 'ID': 'open_prefs_btn', 'Text': u"\u2699",
                'Weight': 0,
                'StyleSheet' : css_prefs
            }),
        ])
    )
    win_timecode_items = win_timecode.GetItems()

    # Event handlers
    def OnClose(ev):
        dispatcher.ExitLoop()

    def OnTimer(ev):
        #   win.Find('timecodeID').Text = currentTimeline.GetCurrentTimecode()
        fps_target = fps_list[win_prefs_items["fps_selection"].CurrentText]
        win_timecode.Find('timecodeID').Text = convert_tc(fps_target)
        
    def OnPrefs(ev):
        win_prefs.Show()
        dispatcher.RunLoop()
        win_prefs.Hide()


    # assign event handlers
    win_timecode.On["tc_display"].Close = OnClose
    dispatcher['On']['Timeout'] = OnTimer
    
    win_timecode.On["open_prefs_btn"].Clicked = OnPrefs

    return win_timecode, win_timecode_items

def create_prefs_window():
    # define the window UI layout
    win_prefs = dispatcher.AddWindow({
        'ID': "tc_prefs",
        'Geometry': [675,200,430,150 ],
        'WindowTitle': "Timecode Display Preferences",
        'BackgroundColor': {"R":0.1, "G":0.1, "B":0.2, "A":0.3}
        },
        ui.VGroup([
            ui.HGroup([
                ui.Label({ 'ID': 'colorID', 'Text': 'Color',
                    'Weight': 0,
                    'StyleSheet' : css_prefs
                }),
                ui.ColorPicker({ 'ID': 'color_selection',
                    'Weight': 0,
                    'Color': {"R":1.0, "G":0.39, "B":0.28},
                    # 'DoAlpha': True,
                    'StyleSheet' : css_prefs
                }),
                ui.HGap(),
                ui.Label({ 'ID': 'fpsID', 'Text': 'Conversion',
                    'Weight': 0,
                    'StyleSheet' : css_prefs
                }),
                ui.ComboBox({ 'ID': 'fps_selection', 'Text': projectFPS,
                    'StyleSheet' : css_prefs
                })
            ]),
            ui.HGroup([
                    ui.Button({ 'Weight': 0, 'ID': 'cancel_pref_btn', 'Text': 'Cancel'}),
                    ui.HGap(),
                    ui.Button({ 'Weight': 0, 'ID': 'apply_pref_btn', 'Text': 'Save'})
                ]),

        ])
    )
    win_prefs_items = win_prefs.GetItems()

    # Event handlers
    def OnClose(ev):
        dispatcher.ExitLoop()
        
    def OnCancel(ev):
        #reload default StyleSheet
        # win_timecode_items['timecodeID'].StyleSheet = update_css_label(css_label_color=default_css_label_color)
        dispatcher.ExitLoop()

    def OnApply(ev):
        #get the color picker decimal value
        decimal_color = win_prefs_items['color_selection'].Color
        
        #convert color to CSS format rgb(255, 255, 255)
        rgb_label_color = f'rgb({decimal2rgb(decimal_color["R"])}, {decimal2rgb(decimal_color["G"])}, {decimal2rgb(decimal_color["B"])})'

        #update StyleSheet for the timecodeID    
        win_timecode_items['timecodeID'].StyleSheet = update_css_label(css_label_color=rgb_label_color)
        
        #recalculate 
        print(f'FPS VALUE: {fps_list[win_prefs_items["fps_selection"].CurrentText]}')
        win_prefs_items["fps_selection"].CurrentText = fps_list[win_prefs_items["fps_selection"].CurrentText]
        
        save_prefs()
        
        dispatcher.ExitLoop()
    
    def OnColorChange(ev):
        #Live update of the color
        decimal_color = win_prefs_items['color_selection'].Color
        rgb_label_color = f'rgb({decimal2rgb(decimal_color["R"])}, {decimal2rgb(decimal_color["G"])}, {decimal2rgb(decimal_color["B"])})'
        win_timecode_items['timecodeID'].StyleSheet = update_css_label(css_label_color=rgb_label_color)


    # assign event handlers
    win_prefs.On["tc_prefs"].Close = OnClose
    win_prefs.On["cancel_pref_btn"].Clicked = OnCancel
    win_prefs.On["apply_pref_btn"].Clicked = OnApply
    
    # win_prefs.On["color_selection"].ColorChanged = OnColorChange
    
    return win_prefs, win_prefs_items

def save_prefs():
    #get preferences and if pref_file exists, overwrite

    StyleSheet_value = win_timecode_items['timecodeID'].StyleSheet
    
    fps_target = win_prefs_items["fps_selection"].CurrentText
    prefs = {
            'StyleSheet': StyleSheet_value,
            'fps_target': fps_target 
        }
    
    with open(prefs_file, mode='w') as outfile:
        json.dump(prefs, outfile)
    print(f"PREFERENCES SAVED to {prefs_file}")
      
def read_prefs():
    #read the preference file and return StyleSheet with color and the fps_target
    with open(prefs_file, mode='r') as openfile:
        json_object = json.load(openfile)
    return json_object['StyleSheet'], json_object['fps_target']

def initialize():
    #Create windows and declare global variables
    #TODO maybe separate win_done, win_error with create_error_window()...
    global win_timecode, win_timecode_items
    global win_prefs, win_prefs_items

    win_timecode, win_timecode_items = create_main_window()
    win_prefs, win_prefs_items = create_prefs_window()
        
    # conversion_factor = {'24to30':30/24, '30to24':24/30, '25to30': 30/25, '24to29': (30.000/1.001)/24, '23to29':29.97/23.976}
    global fps_list
    fps_list = {'to23.976':23.976, 'to29.97':29.97, 'to25': 25, 'to24': 24}
    win_prefs_items["fps_selection"].AddItems(list(fps_list.keys()))
    
    #if preferences were saved, retrieve the settings
    if os.path.exists(prefs_file):
        StyleSheet, target_fps = read_prefs()
        win_timecode_items['timecodeID'].StyleSheet = StyleSheet
        win_prefs_items["fps_selection"].CurrentText = target_fps
        
        # convert format rgb(255, 99, 71) to {"R":1.0, "G":0.39, "B":0.28}
        color_in_stylesheet = StyleSheet.strip().split(';')[0].split(':')[1].strip()[3:].replace('(', '').replace(')', '').split(',')
        converted_color = {'R': float(color_in_stylesheet[0])/255, 'G': float(color_in_stylesheet[1])/255, 'B': float(color_in_stylesheet[2])/255}
        
        #update color value in the pref windows
        win_prefs_items['color_selection'].Color = converted_color #found in json prefs StyleSheet
    
def main():
    initialize()
    # Main dispatcher loop
    mytimer = ui.Timer({ 'ID': 'MyTimer', 'Interval': 1000 })  # 1000 millisecs
    mytimer.Start()
    
    win_timecode.Show()
    dispatcher.RunLoop()
    win_timecode.Hide()



if __name__ == "__main__":
    main()