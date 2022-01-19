#!/usr/local/bin/python3

import imp
import os
import sys
import platform
import subprocess

##################################################
__author__ = "Ben"
__version__ = "1.3"
__status__ = "Dev"
"""
- 1.3: added get_desktop_path
- 1.2: Added variables for requirements
- 1.1 Added check_requirements function
"""
##################################################


v, _, _ = platform.mac_ver()
macOSversion = '.'.join(v.split('.')[:3])

appstore_path = r"/Applications/DaVinci Resolve Studio.app"
dongle_app_path = r"/Applications/DaVinci Resolve/DaVinci Resolve.app"

# Requirement check and installation variables:
required_pkg = ["PyAutoGUI"]
python3path = "/Library/Frameworks/Python.framework/Versions/3.6/bin/python3"


def resolve_from_appstore():
    if os.path.exists(appstore_path):
        print("APP STORE VERSION DETECTED")
        return True
    elif os.path.exists(dongle_app_path):
        print("DONGLE VERSION DETECTED")
        return False

def check_requirements():
    # run a command and grab formatted output in a variable
    print("Checking packages list requirements...")
    installed_pkg = subprocess.check_output(
        [python3path, "-m", "pip", "freeze"], universal_newlines=True)
    for package in required_pkg:
        if package in installed_pkg:
            print(package + " is installed")
        else:
            print(package + " is not installed. Starting installation")
            subprocess.check_call(
                [python3path, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([python3path, '-m', 'pip', 'install',
                                   package])

def get_desktop_path():
    # Adapt to testing platform OSX-WINDOWS
    if sys.platform.startswith("darwin"):
        home_dir = os.path.expanduser("~")
        home_user = home_dir.split("/")[2]
    elif sys.platform.startswith("win") or sys.platform.startswith("win32"):
        home_dir = os.path.expanduser("~")
        home_user = home_dir.split("\\")[2]
    elif sys.platform.startswith("linux"):
        home_dir = os.path.expanduser("~")
        home_user = home_dir.split("\\")[2]
    desktop_path = f"{home_dir}/Desktop/"
    return desktop_path


def GetApp(app_name="Resolve"):
    lib_path = os.getenv("RESOLVE_SCRIPT_LIB")

    try:
        import fusionscript as script_module
    except ImportError:
        print(
            "ImportError... lib_path not found, script might run from outside Resolve GUI")

        if lib_path:
            try:
                script_module = imp.load_dynamic("fusionscript", lib_path)
                print("module loaded")
            except ImportError:
                print(
                    "ERROR with lib_path and script_module...trying to search for fusionscript")
        else:
            # Look for default install locations:
            ext = ".so"
            print("lib_path not found: checking platform")
            if sys.platform.startswith("darwin"):
                print("MacOSX Platform detected. Version: " + str(macOSversion))
                if resolve_from_appstore():
                    path = "/Applications/DaVinci Resolve Studio.app/Contents/Libraries/Fusion/"
                else:
                    path = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/"
            elif sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
                ext = ".dll"
                path = "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\"
            elif sys.platform.startswith("linux"):
                path = "/opt/resolve/libs/Fusion/"

            try:
                # then retry to load fusionscript using path from OS
                print("Loading module...")
                script_module = imp.load_dynamic(
                    "fusionscript", path + "fusionscript" + ext)
            except ImportError:
                print("ERROR IMPORT on all platform")

    return script_module.scriptapp(app_name)


def GetModule_fusionscript():
    # this module often called bmd is needed for ui function like UIDispatcher(ui)
    path = "/Applications/DaVinci Resolve Studio.app/Contents/Libraries/Fusion/"
    ext = ".so"

    print("checking platform")
    if sys.platform.startswith("darwin"):
        print("MacOSX Platform detected. Version: " + str(macOSversion))
        if resolve_from_appstore():
            path = "/Applications/DaVinci Resolve Studio.app/Contents/Libraries/Fusion/"
        else:
            path = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/"
    elif sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
        ext = ".dll"
        path = "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\"
    elif sys.platform.startswith("linux"):
        path = "/opt/resolve/libs/Fusion/"

    bmd = script_module = imp.load_dynamic(
        "fusionscript", path + "fusionscript" + ext)
    return bmd
