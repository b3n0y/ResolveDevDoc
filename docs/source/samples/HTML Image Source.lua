-- HTML Image Source v1.0 2017-08-15 6.20 PM
-- by Andrew Hazelden <andrew@andrewhazelden.com>
-- www.andrewhazelden.com

-- Overview:
-- This script is a Fusion Lua based example that works in Fusion 8.2.1 and Fusion 9 that uses the HTML loading capacity of the ui:textField to display an image.

-- This example is based upon a tip from the WSL User "Dunn". The basic idea is that you are able to use the codebeautify webpage translator tool to convert a PNG, or JPEG image from a binary image format into a base64 encoded inline HTML "Image Source" element that can be placed as HTML code inside of a ui:textField control.

-- Installation:
-- Step 1. Copy the "HTML Image Source.lua" script and the "fusion-logo.png.base64" image to your Fusion user preferences "Scripts/Comp/" folder.

-- Step 2. Once the script is copied into the "Scripts/Comp/" folder you can then run it from inside Fusion's GUI by going to the Script menu and selecting the "HTML Image Source" item.

-- How to Generate a base64 Image Resource:
-- Step 1. Go to this webpage (https://codebeautify.org/image-to-base64-converter) and process your photo or logo image from a JPEG/PNG/GIF image format into a "Source Image" based inline html code format.

-- Note: In theory you could also look into using the Mac/Linux/Cygwin "base64" encoding tool to do the same process if you added the html header tag "<img src='data:image/png;base64," and a footer tag of "'/>" to the base64 encoded image. Type "man base64" in a terminal window for more details on the conversion tool. 

-- Step 2. Save the "Source Image" output from the Codebeautify conversion tool into a new textfile that is placed in the same folder as your UI Manager based .lua script. It is a good idea to give this converted image a unique name like "my-image.base64" so you can remember later on this media was encoded in the base64 format.

-- Step 3. Update the "base64Imagename" variable in the "HTML Image Source.lua" script to use the Fusion relative "Pathmap" based location where you copied the "fusion-logo.png.base64" image.


local ui = fu.UIManager
local disp = bmd.UIDispatcher(ui)
local width,height = 400,200

win = disp:AddWindow({
  ID = 'MyWin',
  WindowTitle = 'HTML Image Source',
  Geometry = { 0, 0, width, height },
  Margin = 10,
  Spacing = 10,
  
	ui:VGroup{
	  ID = 'root',
	  
	  -- Add your GUI elements here:
    ui:HGroup{
      Weight = 1,
      ui:TextEdit{ ID = 'HTMLPreview', ReadOnly = true },
    },
  },
})

-- The window was closed
function win.On.MyWin.Close(ev)
    disp:ExitLoop()
end

-- Add your GUI element based event functions here:
itm = win:GetItems()

-- Resolve the base64 encoded image location on disk using a Fusion Pathmap:
base64Imagename = comp:MapPath('Scripts:\\comp\\fusion-logo.png.base64')
-- base64Imagename = comp:MapPath('Config:\\fusion-logo.png.base64')

-- Load the image resource into the textfield:
itm.HTMLPreview.HTML = io.open(base64Imagename, "r"):read("*all")

win:Show()
disp:RunLoop()
win:Hide()
