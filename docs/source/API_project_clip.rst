Project and Clip properties
---------------------------

This section covers additional notes for the functions "Project:GetSetting", "Project:SetSetting", "Timeline:GetSetting", "Timeline:SetSetting", "MediaPoolItem:GetClipProperty" and 
"MediaPoolItem:SetClipProperty". These functions are used to get and set properties otherwise available to the user through the Project Settings and the Clip Attributes dialogs.

The functions follow a key-value pair format, where each property is identified by a key (the settingName or propertyName parameter) and possesses a value (typically a text value). Keys and values are
designed to be easily correlated with parameter names and values in the Resolve UI. Explicitly enumerated values for some parameters are listed below.

Some properties may be read only - these include intrinsic clip properties like date created or sample rate, and properties that can be disabled in specific application contexts (e.g. custom colorspaces
in an ACES workflow, or output sizing parameters when behavior is set to match timeline)

Getting values
^^^^^^^^^^^^^^

Invoke "Project:GetSetting", "Timeline:GetSetting" or "MediaPoolItem:GetClipProperty" with the appropriate property key. To get a snapshot of all queryable properties (keys and values), you can call 
"Project:GetSetting", "Timeline:GetSetting" or "MediaPoolItem:GetClipProperty" without parameters (or with a NoneType or a blank property key). Using specific keys to query individual properties will 
be faster. Note that getting a property using an invalid key will return a trivial result.

Setting values
^^^^^^^^^^^^^^

Invoke "Project:SetSetting", "Timeline:SetSetting" or "MediaPoolItem:SetClipProperty" with the appropriate property key and a valid value. When setting a parameter, please check the return value to 
ensure the success of the operation. You can troubleshoot the validity of keys and values by setting the desired result from the UI and checking property snapshots before and after the change.

The following Project properties have specifically enumerated values:
"superScale" - the property value is an enumerated integer between 0 and 3 with these meanings: 0=Auto, 1=no scaling, and 2, 3 and 4 represent the Super Scale multipliers 2x, 3x and 4x.
Affects:
• x = Project:GetSetting('superScale') and Project:SetSetting('superScale', x)

"timelineFrameRate" - the property value is one of the frame rates available to the user in project settings under "Timeline frame rate" option. Drop Frame can be configured for supported frame rates 
                      by appending the frame rate with "DF", e.g. "29.97 DF" will enable drop frame and "29.97" will disable drop frame
Affects:
x = Project:GetSetting('timelineFrameRate') and Project:SetSetting('timelineFrameRate', x)

The following Clip properties have specifically enumerated values:
"superScale" - the property value is an enumerated integer between 1 and 3 with these meanings: 1=no scaling, and 2, 3 and 4 represent the Super Scale multipliers 2x, 3x and 4x.
Affects:
x = MediaPoolItem:GetClipProperty('Super Scale') and MediaPoolItem:SetClipProperty('Super Scale', x)
