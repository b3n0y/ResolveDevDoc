Looking up Timeline item properties
-----------------------------------

This section covers additional notes for the function "TimelineItem:SetProperty" and "TimelineItem:GetProperty". These functions are used to get and set properties mentioned.

The supported keys with their accepted values are:
  "Pan" : floating point values from -4.0*width to 4.0*width
  "Tilt" : floating point values from -4.0*height to 4.0*height
  "ZoomX" : floating point values from 0.0 to 100.0
  "ZoomY" : floating point values from 0.0 to 100.0
  "ZoomGang" : a boolean value
  "RotationAngle" : floating point values from -360.0 to 360.0
  "AnchorPointX" : floating point values from -4.0*width to 4.0*width
  "AnchorPointY" : floating point values from -4.0*height to 4.0*height
  "Pitch" : floating point values from -1.5 to 1.5
  "Yaw" : floating point values from -1.5 to 1.5
  "FlipX" : boolean value for flipping horizonally
  "FlipY" : boolean value for flipping vertically
  "CropLeft" : floating point values from 0.0 to width
  "CropRight" : floating point values from 0.0 to width
  "CropTop" : floating point values from 0.0 to height
  "CropBottom" : floating point values from 0.0 to height
  "CropSoftness" : floating point values from -100.0 to 100.0
  "CropRetain" : boolean value for "Retain Image Position" checkbox
  "DynamicZoomEase" : A value from the following constants
     - DYNAMIC_ZOOM_EASE_LINEAR = 0
     - DYNAMIC_ZOOM_EASE_IN
     - DYNAMIC_ZOOM_EASE_OUT
     - DYNAMIC_ZOOM_EASE_IN_AND_OUT
  "CompositeMode" : A value from the following constants
     - COMPOSITE_NORMAL = 0
     - COMPOSITE_ADD
     - COMPOSITE_SUBTRACT
     - COMPOSITE_DIFF
     - COMPOSITE_MULTIPLY
     - COMPOSITE_SCREEN
     - COMPOSITE_OVERLAY
     - COMPOSITE_HARDLIGHT
     - COMPOSITE_SOFTLIGHT
     - COMPOSITE_DARKEN
     - COMPOSITE_LIGHTEN
     - COMPOSITE_COLOR_DODGE
     - COMPOSITE_COLOR_BURN
     - COMPOSITE_HUE
     - COMPOSITE_SATURATE
     - COMPOSITE_COLORIZE
     - COMPOSITE_LUMA_MASK
     - COMPOSITE_DIVIDE
     - COMPOSITE_LINEAR_DODGE
     - COMPOSITE_LINEAR_BURN
     - COMPOSITE_LINEAR_LIGHT
     - COMPOSITE_VIVID_LIGHT
     - COMPOSITE_PIN_LIGHT
     - COMPOSITE_HARD_MIX
     - COMPOSITE_LIGHTER_COLOR
     - COMPOSITE_DARKER_COLOR
     - COMPOSITE_FOREGROUND
     - COMPOSITE_ALPHA
     - COMPOSITE_INVERTED_ALPHA
     - COMPOSITE_LUM
     - COMPOSITE_INVERTED_LUM
  "Opacity" : floating point value from 0.0 to 100.0
  "Distortion" : floating point value from -1.0 to 1.0
  "RetimeProcess" : A value from the following constants
     - RETIME_USE_PROJECT = 0
     - RETIME_NEAREST
     - RETIME_FRAME_BLEND
     - RETIME_OPTICAL_FLOW
  "MotionEstimation" : A value from the following constants
     - MOTION_EST_USE_PROJECT = 0
     - MOTION_EST_STANDARD_FASTER
     - MOTION_EST_STANDARD_BETTER
     - MOTION_EST_ENHANCED_FASTER
     - MOTION_EST_ENHANCED_BETTER
     - MOTION_EST_SPEED_WRAP
  "Scaling" : A value from the following constants
     - SCALE_USE_PRODUCT = 0
     - SCALE_CROP
     - SCALE_FIT
     - SCALE_FILL
     - SCALE_STRETCH
  "ResizeFilter" : A value from the following constants
     - RESIZE_FILTER_USE_FILTER = 0
     - RESIZE_FILTER_SHARPER
     - RESIZE_FILTER_SMOOTHER
     - RESIZE_FILTER_BICUBIC
     - RESIZE_FILTER_BILINEAR
     - RESIZE_FILTER_BESSEL
     - RESIZE_FILTER_BOX
     - RESIZE_FILTER_CATMULL_ROM
     - RESIZE_FILTER_CUBIC
     - RESIZE_FILTER_GAUSSIAN
     - RESIZE_FILTER_LANCZOS
     - RESIZE_FILTER_MITCHELL
     - RESIZE_FILTER_NEAREST_NEIGHBOR
     - RESIZE_FILTER_QUADRATIC
     - RESIZE_FILTER_SINC
     - RESIZE_FILTER_LINEAR
Values beyond the range will be clipped
width and height are same as the UI max limits

The arguments can be passed as a key and value pair or they can be grouped together into a dictionary (for python) or table (for lua) and passed
as a single argument.

Getting the values for the keys that uses constants will return the number which is in the constant