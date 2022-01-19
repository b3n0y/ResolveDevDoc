Basic Resolve API
=================

| Some commonly used API functions are described below (*). 
| As with the resolve object, each object is inspectable for properties and functions.

Resolve
-------

Fusion()
^^^^^^^^

..  topic:: Description

	  Returns the Fusion object. Starting point for Fusion scripts.

    **Type:** Fusion


GetMediaStorage()
^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Returns the media storage object to query and act on media locations.

    **Type:** MediaStorage


GetProjectManager()
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Returns the project manager object for currently open database.

    **Type:** ProjectManager


OpenPage(pageName)
^^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Switches to indicated page in DaVinci Resolve. Input can be one of ("media", "cut", "edit", "fusion", "color", "fairlight", "deliver").

    **Type:** Bool


GetCurrentPage()
^^^^^^^^^^^^^^^^
..  topic:: Description
    
    Returns the page currently displayed in the main window. Returned value can be one of ("media", "cut", "edit", "fusion", "color", "fairlight", "deliver", None).

    **Type:** String            

GetProductName()
^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns product name.

    **Type:** String

GetVersion()
^^^^^^^^^^^^

..  topic:: Description

    Returns list of product version fields in [major, minor, patch, build, suffix] format.

    **Type:** [version fields]

GetVersionString()  
^^^^^^^^^^^^^^^^^^  

..  topic:: Description

	  Returns product version in "major.minor.patch[suffix].build" format. 

    **Type:** string

LoadLayoutPreset(presetName) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Loads UI layout from saved preset named 'presetName'. 

    **Type:** Bool 

UpdateLayoutPreset(presetName)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Overwrites preset named 'presetName' with current UI layout. 

    **Type:** Bool

ExportLayoutPreset(presetName, presetFilePath)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Exports preset named 'presetName' to path 'presetFilePath'. 

**Type:** Bool

DeleteLayoutPreset(presetName)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Deletes preset named 'presetName'. 

**Type:** Bool

SaveLayoutPreset(presetName)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Saves current UI layout as a preset named 'presetName'. 

**Type:** Bool

ImportLayoutPreset(presetFilePath, presetName)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

	  Imports preset from path 'presetFilePath'. The optional argument 'presetName' specifies how the preset shall be named. If not specified, the preset is named based on the filename. 

**Type:** Bool

Quit()     
^^^^^^

..  topic:: Description

	  Quits the Resolve App. 

    **Type:** None


ProjectManager
--------------

CreateProject(projectName)
^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates and returns a project if projectName (string) is unique, and None if it is not.
    
    **Returns** Project            

DeleteProject(projectName)                      
^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete project in the current folder if not currently loaded

    **Returns** Bool   

LoadProject(projectName)
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description
    
    Loads and returns the project with name = projectName (string) if there is a match found, and None if there is no matching Project.

    **Returns** Project

GetCurrentProject()
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the currently loaded Resolve project.

    **Returns** Project

SaveProject()
^^^^^^^^^^^^^

..  topic:: Description

    Saves the currently loaded project with its own name. Returns True if successful.

    **Returns** Bool   
    
CloseProject(project)
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Closes the specified project without saving.

    **Returns** Bool 

CreateFolder(folderName)
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates a folder if folderName (string) is unique.

    **Returns** Bool  

DeleteFolder(folderName)
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes the specified folder if it exists. Returns True in case of success.

    **Returns** Bool

GetProjectListInCurrentFolder()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of project names in current folder.

    **Returns** [project names...] 

GetFolderListInCurrentFolder()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of folder names in current folder.

    **Returns** [folder names...]

GotoRootFolder()
^^^^^^^^^^^^^^^^
                                            
..  topic:: Description

    Opens root folder in database.

    **Returns** Bool   

GotoParentFolder()
^^^^^^^^^^^^^^^^^^
                                        
..  topic:: Description

    Opens parent folder of current folder in database if current folder has parent.

    **Returns** Bool

GetCurrentFolder()
^^^^^^^^^^^^^^^^^^
..  topic:: Description

    Returns the current folder name.

    **Returns** string

OpenFolder(folderName)
^^^^^^^^^^^^^^^^^^^^^^
..  topic:: Description

    Opens folder under given name.

    **Returns** Bool  

ImportProject(filePath)
^^^^^^^^^^^^^^^^^^^^^^^
                                      
..  topic:: Description

    Imports a project from the file path provided. Returns True if successful.

    **Returns** Bool  

ExportProject(projectName, filePath, withStillsAndLUTs=True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Exports project to provided file path, including stills and LUTs if withStillsAndLUTs is True (enabled by default). Returns True in case of success.

    **Returns** Bool  

RestoreProject(filePath)
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Restores a project from the file path provided. Returns True if successful.

    **Returns** Bool

GetCurrentDatabase()
^^^^^^^^^^^^^^^^^^^^
                                      
..  topic:: Description

    Returns a dictionary (with keys 'DbType', 'DbName' and optional 'IpAddress') corresponding to the current database connection

    **Returns** {dbInfo} 
    
GetDatabaseList()
^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of dictionary items (with keys 'DbType', 'DbName' and optional 'IpAddress') corresponding to all the databases added to Resolve

    **Returns** [{dbInfo}]  

SetCurrentDatabase({dbInfo})
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Switches current database connection to the database specified by the keys below, and closes any open project.

    * **'DbType':** 'Disk' or 'PostgreSQL' (string)
    * **'DbName':** database name (string)
    * **'IpAddress':** IP address of the PostgreSQL server (string, optional key - defaults to '127.0.0.1')

    **Returns** Bool


Project
-------

GetMediaPool()
^^^^^^^^^^^^^^
   
..  topic:: Description

    Returns the Media Pool object.

    **Returns** MediaPool

GetTimelineCount()
^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the number of timelines currently present in the project.

    **Returns** int

GetTimelineByIndex(idx) 
^^^^^^^^^^^^^^^^^^^^^^^
                                   
..  topic:: Description

    Returns timeline at the given index, 1 <= idx <= project.GetTimelineCount()

    **Returns** Timeline

GetCurrentTimeline()   
^^^^^^^^^^^^^^^^^^^^
                                   
..  topic:: Description

    Returns the currently loaded timeline.

    **Returns** Timeline  

SetCurrentTimeline(timeline)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                   
..  topic:: Description

    Sets given timeline as current timeline for the project. Returns True if successful.

    **Returns** Bool

GetGallery()                                                
^^^^^^^^^^^^

..  topic:: Description

    Returns the Gallery object.

    **Returns** Gallery

GetName()                                                    
^^^^^^^^^

..  topic:: Description

    Returns project name.

    **Returns** string

SetName(projectName)                                           
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets project name if given projectname (string) is unique.

    **Returns** Bool

GetPresetList()                                 
^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of presets and their information.

    **Returns** [presets...]       

SetPreset(presetName)                                        
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets preset by given presetName (string) into project.

    **Returns** Bool  

AddRenderJob()                                             
^^^^^^^^^^^^^^

..  topic:: Description

    Adds a render job based on current render settings to the render queue. Returns a unique job id (string) for the new render job.

    **Returns** string  

DeleteRenderJob(jobId)                                      
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes render job for input job id (string).

    **Returns** Bool  

DeleteAllRenderJobs()                                         
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes all render jobs in the queue.

    **Returns** Bool 

GetRenderJobList()                              
^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of render jobs and their information.

    **Returns** [render jobs...]   

GetRenderPresetList()                             
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of render presets and their information.

    **Returns** [presets...]    

StartRendering(jobId1, jobId2, ...)                        
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Starts rendering jobs indicated by the input job ids.

    **Returns** Bool    

StartRendering([jobIds...], isInteractiveMode=False)    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Starts rendering jobs indicated by the input job ids.

    **Returns** Bool       
                                                                      
..  note:: 

    The optional "isInteractiveMode", when set, enables error feedback in the UI during rendering.

StartRendering(isInteractiveMode=False)                       
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Starts rendering all queued render jobs. 

    **Returns** Bool

..  note:: 

    The optional "isInteractiveMode", when set, enables error feedback in the UI during rendering.

StopRendering()
^^^^^^^^^^^^^^^
                                                
..  topic:: Description

    Stops any current render processes.

    **Returns** None

IsRenderingInProgress()                                        
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns True if rendering is in progress.

    **Returns** Bool

LoadRenderPreset(presetName)                                   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets a preset as current preset for rendering if presetName (string) exists.

    **Returns** Bool

SaveAsNewRenderPreset(presetName)                              

..  topic:: Description

    Creates new render preset by given name if presetName(string) is unique.

    **Returns** Bool

SetRenderSettings({settings})                                  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets given settings for rendering. Settings is a dict, with support for the keys:

    **Returns** Bool
                                                                        
..  note:: 

    Refer to :ref: `"Looking up render settings <api_render>"` section for information for supported settings

GetRenderJobStatus(jobId)                            
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a dict with job status and completion percentage of the job by given jobId (string).

    **Returns** {status info} 

GetSetting(settingName)                                      
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns value of project setting (indicated by settingName, string). Check the section below for more information.

    **Returns** string

SetSetting(settingName, settingValue)                          
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the project setting (indicated by settingName, string) to the value (settingValue, string). Check the section below for more information.

    **Returns** Bool

GetRenderFormats()                               
^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a dict (format -> file extension) of available render formats.

    **Returns** {render formats..}

GetRenderCodecs(renderFormat)                   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a dict (codec description -> codec name) of available codecs for given render format (string).

    **Returns** {render codecs...} 

GetCurrentRenderFormatAndCodec()                 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a dict with currently selected format 'format' and render codec 'codec'.

    **Returns** {format, codec}   

SetCurrentRenderFormatAndCodec(format, codec)                  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets given render format (string) and render codec (string) as options for rendering.

    **Returns** Bool

GetCurrentRenderMode()                                     
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the render mode: 0 - Individual clips, 1 - Single clip.

    **Returns** int    

SetCurrentRenderMode(renderMode)                              
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the render mode. Specify renderMode = 0 for Individual clips, 1 for Single clip.

    **Returns** Bool 

GetRenderResolutions(format, codec)              
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns list of resolutions applicable for the given render format (string) and render codec (string). Returns full list of resolutions if no argument is provided. Each element in the list is a dictionary with 2 keys "Width" and "Height".

    **Returns** [{Resolution}]    

RefreshLUTList()                                              
^^^^^^^^^^^^^^^^

..  topic:: Description

    Refreshes LUT List

    **Returns** Bool 


MediaStorage
------------

GetMountedVolumeList()
^^^^^^^^^^^^^^^^^^^^^^
                                 
..  topic:: Description

    Returns list of folder paths corresponding to mounted volumes displayed in Resolve's Media Storage.

    **Returns** [paths...]  

GetSubFolderList(folderPath)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns list of folder paths in the given absolute folder path.

    **Returns** [paths...]  

GetFileList(folderPath)                                 
^^^^^^^^^^^^^^^^^^^^^^^
..  topic:: Description

    Returns list of media and file listings in the given absolute folder path. Note that media listings may be logically consolidated entries.

    **Returns** [paths...] 

RevealInStorage(path)                                         
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Expands and displays given file/folder path in Resolve’s Media Storage.

    **Returns** Bool 

AddItemListToMediaPool(item1, item2, ...)              
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Adds specified file/folder paths from Media Storage into current Media Pool folder. 
    Input is one or more file/folder paths. Returns a list of the MediaPoolItems created.

    **Returns** [clips...]  

AddItemListToMediaPool([items...])                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is an array of file/folder paths. 
    Returns a list of the MediaPoolItems created.

    **Returns** [clips...] 

AddClipMattesToMediaPool(MediaPoolItem, [paths], stereoEye) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Adds specified media files as mattes for the specified MediaPoolItem. 
    StereoEye is an optional argument for specifying which eye to add the matte to for stereo clips ("left" or "right"). Returns True if successful.

    **Returns** Bool   

AddTimelineMattesToMediaPool([paths])             
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Adds specified media files as timeline mattes in current media pool folder. Returns a list of created MediaPoolItems.

    **Returns** [MediaPoolItems] 


MediaPool
---------

GetRootFolder()
^^^^^^^^^^^^^^^
                                              
..  topic:: Description

    Returns root Folder of Media Pool
    
    **Returns** Folder

AddSubFolder(folder, name)
^^^^^^^^^^^^^^^^^^^^^^^^^^
                                   
..  topic:: Description

    Adds new subfolder under specified Folder object with the given name.

    **Returns** Folder

CreateEmptyTimeline(name)                                  
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Adds new timeline with given name.

    **Returns** Timeline

AppendToTimeline(clip1, clip2, ...)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                
..  topic:: Description

    Appends specified MediaPoolItem objects in the current timeline. Returns the list of appended timelineItems.

    **Returns** [TimelineItem]  

AppendToTimeline([clips])                            
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Appends specified MediaPoolItem objects in the current timeline. Returns the list of appended timelineItems.

    **Returns** [TimelineItem]

AppendToTimeline([{clipInfo}, ...])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 
..  topic:: Description

    Appends list of clipInfos specified as dict of "mediaPoolItem", "startFrame" (int), "endFrame" (int), (optional) "mediaType" (int; 1 - Video only, 2 - Audio only). Returns the list of appended timelineItems.

    **Returns** [TimelineItem]  

CreateTimelineFromClips(name, clip1, clip2,...)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            
..  topic:: Description

    Creates new timeline with specified name, and appends the specified MediaPoolItem objects.

    **Returns** Timeline

CreateTimelineFromClips(name, [clips])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates new timeline with specified name, and appends the specified MediaPoolItem objects.

    **Returns** Timeline 

CreateTimelineFromClips(name, [{clipInfo}])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates new timeline with specified name, appending the list of clipInfos specified as a dict of "mediaPoolItem", "startFrame" (int), "endFrame" (int).

    **Returns** Timeline

ImportTimelineFromFile(filePath, {importOptions}) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates timeline based on parameters within given file and optional importOptions dict, with support for the keys:
                                                                          
    * "timelineName": string, specifies the name of the timeline to be created
    * "importSourceClips": Bool, specifies whether source clips should be imported, True by default
    * "sourceClipsPath": string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if "importSourceClips" is True
    * "sourceClipsFolders": List of Media Pool folder objects to search for source clips if the media is not present in current folder and if "importSourceClips" is False
    * "interlaceProcessing": Bool, specifies whether to enable interlace processing on the imported timeline being created. valid only for AAF import

    **Returns** Timeline

DeleteTimelines([timeline])                                   
^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes specified timelines in the media pool.

    **Returns** Bool 

GetCurrentFolder()                                           
^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns currently selected Folder.

    **Returns** Folder

SetCurrentFolder(Folder)                                       
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets current folder by given Folder.
    
    **Returns** Bool

DeleteClips([clips])                                           
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes specified clips or timeline mattes in the media pool

    **Returns** Bool

DeleteFolders([subfolders])                                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes specified subfolders in the media pool

    **Returns** Bool

MoveClips([clips], targetFolder)                               
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Moves specified clips to target folder.

    **Returns** Bool

MoveFolders([folders], targetFolder)                           
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Moves specified folders to target folder.

    **Returns** Bool

GetClipMatteList(MediaPoolItem)                             
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Get mattes for specified MediaPoolItem, as a list of paths to the matte files.

    **Returns** [paths]

GetTimelineMatteList(Folder)                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Get mattes in specified Folder, as list of MediaPoolItems.

    **Returns** [MediaPoolItems] 

DeleteClipMattes(MediaPoolItem, [paths])                       
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete mattes based on their file paths, for specified MediaPoolItem. Returns True on success.

    **Returns** Bool

RelinkClips([MediaPoolItem], folderPath)                       
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Update the folder location of specified media pool clips with the specified folder path.

    **Returns** Bool

UnlinkClips([MediaPoolItem])                                   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Unlink specified media pool clips.

    **Returns** Bool

ImportMedia([items...])                           
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Imports specified file/folder paths into current Media Pool folder. Input is an array of file/folder paths. Returns a list of the MediaPoolItems created.

    **Returns** [MediaPoolItems] 

ImportMedia([{clipInfo}])                          
^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Imports file path(s) into current Media Pool folder as specified in list of clipInfo dict. Returns a list of the MediaPoolItems created.
    Each clipInfo gets imported as one MediaPoolItem unless 'Show Individual Frames' is turned on.
    
    Example: ImportMedia([{"FilePath":"file_%03d.dpx", "StartIndex":1, "EndIndex":100}]) would import clip "file_[001-100].dpx".

    **Returns** [MediaPoolItems]              


ExportMetadata(fileName, [clips])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Exports metadata of specified clips to 'fileName' in CSV format.
    If no clips are specified, all clips from media pool will be used.

    **Returns** Bool

Folder
------

GetClipList()                                            
^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of clips (items) within the folder.

    **Returns** [clips...]

GetName()                                                    
^^^^^^^^^

..  topic:: Description

    Returns the media folder name.

    **Returns** string

GetSubFolderList()                                     
^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of subfolders in the folder.

    **Returns** [folders...]

MediaPoolItem
-------------

GetName()                                                    
^^^^^^^^^

..  topic:: Description

    Returns the clip name.

    **Returns** string

GetMetadata(metadataType=None)                         
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the metadata value for the key 'metadataType'.
    If no argument is specified, a dict of all set metadata properties is returned.

    **Returns** string|dict 

SetMetadata(metadataType, metadataValue)                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the given metadata to metadataValue (string). Returns True if successful.

    **Returns** Bool 

SetMetadata({metadata})                                       
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the item metadata with specified 'metadata' dict. Returns True if successful.

    **Returns** Bool 

GetMediaId()                                               
^^^^^^^^^^^^

..  topic:: Description

    Returns the unique ID for the MediaPoolItem.

    **Returns** string  

AddMarker(frameId, color, name, note, duration,customData)               
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates a new marker at given frameId position and with given marker information. 
    'customData' is optional and helps to attach user specific data to the marker.
          
    **Returns** Bool

GetMarkers()                                           
^^^^^^^^^^^^

..  topic:: Description

    Returns a dict (frameId -> {information}) of all markers and dicts with their information.
                                                                          
    Example of output format: {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...}
    In the above example - there is one 'Green' marker at offset 96 (position of the marker)

    **Returns** {markers...}

GetMarkerByCustomData(customData)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns marker {information} for the first matching marker with specified customData.

    **Returns** {markers...} 

UpdateMarkerCustomData(frameId, customData)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Updates customData (string) for the marker at given frameId position. 
    CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.

    **Returns** Bool

GetMarkerCustomData(frameId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns customData string for the marker at given frameId position.

    **Returns** string

DeleteMarkersByColor(color)                                   
^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete all markers of the specified color from the media pool item. "All" as argument deletes all color markers.

    **Returns** Bool 

DeleteMarkerAtFrame(frameNum)                                  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete marker at frame number from the media pool item.

    **Returns** Bool

DeleteMarkerByCustomData(customData)                           
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete first matching marker with specified customData.

    **Returns** Bool

AddFlag(color)                                               
^^^^^^^^^^^^^^

..  topic:: Description

    Adds a flag with given color (string).

    **Returns** Bool  

GetFlagList()                                          
^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of flag colors assigned to the item.

    **Returns** [colors...] 

ClearFlags(color)                                              
^^^^^^^^^^^^^^^^^

..  topic:: Description

    Clears the flag of the given color if one exists. An "All" argument is supported and clears all flags.

    **Returns** Bool

GetClipColor()                                               
^^^^^^^^^^^^^^

..  topic:: Description

    Returns the item color as a string.

    **Returns** string

SetClipColor(colorName)                                       
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the item color based on the colorName (string).
    
    **Returns** Bool 

ClearClipColor()                                              
^^^^^^^^^^^^^^^^

..  topic:: Description

    Clears the item color.

    **Returns** Bool 

GetClipProperty(propertyName=None)                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the property value for the key 'propertyName'. 

    If no argument is specified, a dict of all clip properties is returned. Check the section below for more information.

    **Returns** string|dict


SetClipProperty(propertyName, propertyValue)               
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the given property to propertyValue (string). Check the section below for more information.

    **Returns** Bool    

LinkProxyMedia(proxyMediaFilePath)                             
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Links proxy media located at path specified by arg 'proxyMediaFilePath' with the current clip. 'proxyMediaFilePath' should be absolute clip path.

    **Returns** Bool

UnlinkProxyMedia()                                             
^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Unlinks any proxy media associated with clip.

    **Returns** Bool

ReplaceClip(filePath)                                          
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Replaces the underlying asset and metadata of MediaPoolItem with the specified absolute clip path.

    **Returns** Bool


Timeline
--------

GetName()                                                    
^^^^^^^^^

..  topic:: Description

    Returns the timeline name.

    **Returns** string

SetName(timelineName)                                          
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the timeline name if timelineName (string) is unique. Returns True if successful.

    **Returns** Bool

GetStartFrame()                                                 
^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the frame number at the start of timeline.

    **Returns** int

GetEndFrame()                                                  
^^^^^^^^^^^^^

..  topic:: Description

    Returns the frame number at the end of timeline.

    **Returns** int 

GetTrackCount(trackType)                                        
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the number of tracks for the given track type ("audio", "video" or "subtitle").

    **Returns** int

GetItemListInTrack(trackType, index)                     
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of timeline items on that track (based on trackType and index). 1 <= index <= GetTrackCount(trackType).

    **Returns** [items...]

AddMarker(frameId, color, name, note, duration, customData)               
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates a new marker at given frameId position and with given marker information. 
    'customData' is optional and helps to attach user specific data to the marker.
         

    **Returns** Bool 

GetMarkers()                                           
^^^^^^^^^^^^

..  topic:: Description

    Returns a dict (frameId -> {information}) of all markers and dicts with their information.                                                                

    Example: a value of {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...} indicates a single green marker at timeline offset 96

    **Returns** {markers...}

GetMarkerByCustomData(customData)                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns marker {information} for the first matching marker with specified customData.

    **Returns** {markers...}

UpdateMarkerCustomData(frameId, customData)                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.

    **Returns** Bool

GetMarkerCustomData(frameId)                                 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns customData string for the marker at given frameId position.

    **Returns** string

DeleteMarkersByColor(color)                                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes all timeline markers of the specified color. An "All" argument is supported and deletes all timeline markers.

    **Returns** Bool

DeleteMarkerAtFrame(frameNum)                                  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes the timeline marker at the given frame number.

    **Returns** Bool

DeleteMarkerByCustomData(customData)                           
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete first matching marker with specified customData.

    **Returns** Bool

ApplyGradeFromDRX(path, gradeMode, item1, item2, ...)           
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Loads a still from given file path (string) and applies grade to Timeline Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames aligned".

    **Returns** Bool

ApplyGradeFromDRX(path, gradeMode, [items])                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Loads a still from given file path (string) and applies grade to Timeline Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames aligned".

    **Returns** Bool

GetCurrentTimecode()                                         
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a string timecode representation for the current playhead position, while on Cut, Edit, Color, Fairlight and Deliver pages.

    **Returns** string

SetCurrentTimecode(timecode)                                  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets current playhead position from input timecode for Cut, Edit, Color, Fairlight and Deliver pages.

    **Returns** Bool 

GetCurrentVideoItem()                                          
^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the current video timeline item.

    **Returns** item

GetCurrentClipThumbnailImage()                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a dict (keys "width", "height", "format" and "data") with data containing raw thumbnail image data (RGB 8-bit image data encoded in base64 format) for current media in the Color Page.
    An example of how to retrieve and interpret thumbnails is provided in 6_get_current_media_thumbnail.py in the Examples folder.

    **Returns** {thumbnailData}

GetTrackName(trackType, trackIndex)                          
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the track name for track indicated by trackType ("audio", "video" or "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType).

    **Returns** string

SetTrackName(trackType, trackIndex, name)                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the track name (string) for track indicated by trackType ("audio", "video" or "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType).

    **Returns** Bool

DuplicateTimeline(timelineName)                            
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Duplicates the timeline and returns the created timeline, with the (optional) timelineName, on success.

    **Returns** timeline

CreateCompoundClip([timelineItems], {clipInfo})        
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates a compound clip of input timeline items with an optional clipInfo map: {"startTimecode" : "00:00:00:00", "name" : "Compound Clip 1"}. It returns the created timeline item.

    **Returns** timelineItem

CreateFusionClip([timelineItems])                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates a Fusion clip of input timeline items. It returns the created timeline item.

    **Returns** timelineItem

ImportIntoTimeline(filePath, {importOptions})                
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Imports timeline items from an AAF file and optional importOptions dict into the timeline, with support for the keys:

    * "autoImportSourceClipsIntoMediaPool": Bool, specifies if source clips should be imported into media pool, True by default
    * "ignoreFileExtensionsWhenMatching": Bool, specifies if file extensions should be ignored when matching, False by default
    * "linkToSourceCameraFiles": Bool, specifies if link to source camera files should be enabled, False by default
    * "useSizingInfo": Bool, specifies if sizing information should be used, False by default
    * "importMultiChannelAudioTracksAsLinkedGroups": Bool, specifies if multi-channel audio tracks should be imported as linked groups, False by default
    * "insertAdditionalTracks": Bool, specifies if additional tracks should be inserted, True by default
    * "insertWithOffset": string, specifies insert with offset value in timecode format - defaults to "00:00:00:00", applicable if "insertAdditionalTracks" is False
    * "sourceClipsPath": string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if "ignoreFileExtensionsWhenMatching" is True
    * "sourceClipsFolders": string, list of Media Pool folder objects to search for source clips if the media is not present in current folder

    **Returns** Bool

Export(fileName, exportType, exportSubtype)                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Exports timeline to 'fileName' as per input exportType & exportSubtype format.

    **Returns** Bool

    Refer to section :ref:`"Looking up timeline exports properties"<API_timeline_export>` for information on the parameters.

GetSetting(settingName)                                      
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns value of timeline setting (indicated by settingName : string). Check the section below for more information.

    **Returns** string

SetSetting(settingName, settingValue)                          
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets timeline setting (indicated by settingName : string) to the value (settingValue : string). Check the section below for more information.

    **Returns** Bool

InsertGeneratorIntoTimeline(generatorName)             
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Inserts a generator (indicated by generatorName : string) into the timeline.

    **Returns** TimelineItem

InsertFusionGeneratorIntoTimeline(generatorName)       
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Inserts a Fusion generator (indicated by generatorName : string) into the timeline.

    **Returns** TimelineItem

InsertOFXGeneratorIntoTimeline(generatorName)          
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Inserts an OFX generator (indicated by generatorName : string) into the timeline.

    **Returns** TimelineItem

InsertTitleIntoTimeline(titleName)                     
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Inserts a title (indicated by titleName : string) into the timeline.

    **Returns** TimelineItem

InsertFusionTitleIntoTimeline(titleName)              
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Inserts a Fusion title (indicated by titleName : string) into the timeline.

    **Returns** TimelineItem 

GrabStill()                                            
^^^^^^^^^^^

..  topic:: Description

    Grabs still from the current video clip. Returns a GalleryStill object.

    **Returns** galleryStill

GrabAllStills(stillFrameSource)                      
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Grabs stills from all the clips of the timeline at 'stillFrameSource' (1 - First frame, 2 - Middle frame). Returns the list of GalleryStill objects.

    **Returns** [galleryStill]


TimelineItem
------------

GetName()                                                   
^^^^^^^^^

..  topic:: Description

    Returns the item name.

    **Returns** string 

GetDuration()                                                   
^^^^^^^^^^^^^

..  topic:: Description

    Returns the item duration.

    **Returns** int
    
GetEnd()                                                       
^^^^^^^^

..  topic:: Description

    Returns the end frame position on the timeline.

    **Returns** int 

GetFusionCompCount()                                            
^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns number of Fusion compositions associated with the timeline item.

    **Returns** int

GetFusionCompByIndex(compIndex)                          
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the Fusion composition object based on given index. 1 <= compIndex <= timelineItem.GetFusionCompCount()

    **Returns** fusionComp

GetFusionCompNameList()                                  
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of Fusion composition names associated with the timeline item.

    **Returns** [names...]

GetFusionCompByName(compName)                            
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the Fusion composition object based on given name.

    **Returns** fusionComp

GetLeftOffset()                                                
^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the maximum extension by frame for clip from left side.

    **Returns** int 

GetRightOffset()                                                
^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the maximum extension by frame for clip from right side.

    **Returns** int

GetStart()                                                     
^^^^^^^^^^

..  topic:: Description

    Returns the start frame position on the timeline.

    **Returns** int 

SetProperty(propertyKey, propertyValue)                        
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the value of property "propertyKey" to value "propertyValue"

    Refer to "Looking up Timeline item properties" for more information

    **Returns** Bool


GetProperty(propertyKey)                            
^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    returns the value of the specified key
    if no key is specified, the method returns a dictionary(python) or table(lua) for all supported keys

    **Returns** int/[key:value]

AddMarker(frameId, color, name, note, duration,customData)            
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Creates a new marker at given frameId position and with given marker information. 'customData' is optional and helps to attach user specific data to the marker.
          
    **Returns** Bool   

GetMarkers()                                          
^^^^^^^^^^^^

..  topic:: Description

    Returns a dict (frameId -> {information}) of all markers and dicts with their information.

    **Returns** {markers...} 

..  topic:: Description

  Example: a value of {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...} indicates a single green marker at clip offset 96

GetMarkerByCustomData(customData)                     
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns marker {information} for the first matching marker with specified customData.

    **Returns** {markers...} 

UpdateMarkerCustomData(frameId, customData)                   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.

    **Returns** Bool 

GetMarkerCustomData(frameId)                                 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns customData string for the marker at given frameId position.

    **Returns** string

DeleteMarkersByColor(color)                                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete all markers of the specified color from the timeline item. "All" as argument deletes all color markers.

    **Returns** Bool

DeleteMarkerAtFrame(frameNum)                                  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete marker at frame number from the timeline item.

    **Returns** Bool

DeleteMarkerByCustomData(customData)                           
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Delete first matching marker with specified customData.

    **Returns** Bool

AddFlag(color)                                                
^^^^^^^^^^^^^^

..  topic:: Description

    Adds a flag with given color (string).

    **Returns** Bool 

GetFlagList()                                           
^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of flag colors assigned to the item.

    **Returns** [colors...]

ClearFlags(color)                                              
^^^^^^^^^^^^^^^^^

..  topic:: Description

    Clear flags of the specified color. An "All" argument is supported to clear all flags. 

    **Returns** Bool

GetClipColor()                                              
^^^^^^^^^^^^^^

..  topic:: Description

    Returns the item color as a string.

    **Returns** string 

SetClipColor(colorName)                                        
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the item color based on the colorName (string).

    **Returns** Bool
    
ClearClipColor()                                               
^^^^^^^^^^^^^^^^

..  topic:: Description

    Clears the item color.

    **Returns** Bool

AddFusionComp()                                          
^^^^^^^^^^^^^^^

..  topic:: Description

    Adds a new Fusion composition associated with the timeline item.

    **Returns** fusionComp

ImportFusionComp(path)                                   
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Imports a Fusion composition from given file path by creating and adding a new composition for the item.

    **Returns** fusionComp

ExportFusionComp(path, compIndex)                              
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Exports the Fusion composition based on given index to the path provided.

    **Returns** Bool

DeleteFusionCompByName(compName)                               
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes the named Fusion composition.

    **Returns** Bool

LoadFusionCompByName(compName)                           
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Loads the named Fusion composition as the active composition.

    **Returns** fusionComp

RenameFusionCompByName(oldName, newName)                       
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Renames the Fusion composition identified by oldName.

    **Returns** Bool

AddVersion(versionName, versionType)                           
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Adds a new color version for a video clipbased on versionType (0 - local, 1 - remote).

    **Returns** Bool

GetCurrentVersion()                                
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the current version of the video clip. The returned value will have the keys versionName and versionType(0 - local, 1 - remote).

    **Returns** {versionName...}

DeleteVersionByName(versionName, versionType)                  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes a color version by name and versionType (0 - local, 1 - remote).

    **Returns** Bool

LoadVersionByName(versionName, versionType)                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Loads a named color version as the active version. versionType: 0 - local, 1 - remote.

    **Returns** Bool

RenameVersionByName(oldName, newName, versionType)             
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Renames the color version identified by oldName and versionType (0 - local, 1 - remote).

    **Returns** Bool

GetVersionNameList(versionType)                          
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a list of all color versions for the given versionType (0 - local, 1 - remote).

    **Returns** [names...]

GetMediaPoolItem()                                    
^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the media pool item corresponding to the timeline item if one exists.

    **Returns** MediaPoolItem

GetStereoConvergenceValues()                         
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a dict (offset -> value) of keyframe offsets and respective convergence values.

    **Returns** {keyframes...}

GetStereoLeftFloatingWindowParams()                 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    For the LEFT eye -> returns a dict (offset -> dict) of keyframe offsets and respective floating window params. Value at particular offset includes the left, right, top and bottom floating window values.

    **Returns** {keyframes...} 

GetStereoRightFloatingWindowParams()              
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    For the RIGHT eye -> returns a dict (offset -> dict) of keyframe offsets and respective floating window params. Value at particular offset includes the left, right, top and bottom floating window values.

    **Returns** {keyframes...}   

SetLUT(nodeIndex, lutPath)                                     
^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets LUT on the node mapping the node index provided, 1 <= nodeIndex <= total number of nodes.
    The lutPath can be an absolute path, or a relative path (based off custom LUT paths or the master LUT path).
    The operation is successful for valid lut paths that Resolve has already discovered (see Project.RefreshLUTList).

    **Returns** Bool

SetCDL([CDL map])                                              
^^^^^^^^^^^^^^^^^

..  topic:: Description

    Keys of map are: "NodeIndex", "Slope", "Offset", "Power", "Saturation", where 1 <= NodeIndex <= total number of nodes.
    
    Example python code - SetCDL({"NodeIndex" : "1", "Slope" : "0.5 0.4 0.2", "Offset" : "0.4 0.3 0.2", "Power" : "0.6 0.7 0.8", "Saturation" : "0.65"})

    **Returns** Bool

AddTake(mediaPoolItem, startFrame, endFrame)                  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Adds mediaPoolItem as a new take. Initializes a take selector for the timeline item if needed. By default, the full clip extents is added. startFrame (int) and endFrame (int) are optional arguments used to specify the extents.

    **Returns** Bool 

GetSelectedTakeIndex()                                         
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the index of the currently selected take, or 0 if the clip is not a take selector.

    **Returns** int 

GetTakesCount()                                                 
^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the number of takes in take selector, or 0 if the clip is not a take selector.

    **Returns** int

GetTakeByIndex(idx)                                   
^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns a dict (keys "startFrame", "endFrame" and "mediaPoolItem") with take info for specified index.

    **Returns** {takeInfo...}

DeleteTakeByIndex(idx)                                         
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes a take by index, 1 <= idx <= number of takes.

    **Returns** Bool

SelectTakeByIndex(idx)                                        
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Selects a take by index, 1 <= idx <= number of takes.

    **Returns** Bool 

FinalizeTake()                                                 
^^^^^^^^^^^^^^

..  topic:: Description

    Finalizes take selection.

    **Returns** Bool

CopyGrades([tgtTimelineItems])                                
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Copies the current grade to all the items in tgtTimelineItems list. Returns True on success and False if any error occured.

    **Returns** Bool 


Gallery
-------

GetAlbumName(galleryStillAlbum)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the name of the GalleryStillAlbum object 'galleryStillAlbum'.

    **Returns** string

SetAlbumName(galleryStillAlbum, albumName)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the name of the GalleryStillAlbum object 'galleryStillAlbum' to 'albumName'.

    **Returns** Bool

GetCurrentStillAlbum()
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns current album as a GalleryStillAlbum object.

    **Returns** galleryStillAlbum

SetCurrentStillAlbum(galleryStillAlbum)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..  topic:: Description

    Sets current album to GalleryStillAlbum object 'galleryStillAlbum'.

    **Returns** Bool

GetGalleryStillAlbums()
^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the gallery albums as a list of GalleryStillAlbum objects.

    **Returns** [galleryStillAlbum]


GalleryStillAlbum
-----------------

GetStills()
^^^^^^^^^^^

..  topic:: Description

    Returns the list of GalleryStill objects in the album.

    **Returns** [galleryStill]
    
GetLabel(galleryStill)
^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Returns the label of the galleryStill.

    **Returns** string

SetLabel(galleryStill, label)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Sets the new 'label' to GalleryStill object 'galleryStill'.

    **Returns** Bool 

ExportStills([galleryStill], folderPath, filePrefix, format)   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Exports list of GalleryStill objects '[galleryStill]' to directory 'folderPath', with filename prefix 'filePrefix', using file format 'format' (supported formats: dpx, cin, tif, jpg, png, ppm, bmp, xpm).

    **Returns** Bool

DeleteStills([galleryStill])                                   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  topic:: Description

    Deletes specified list of GalleryStill objects '[galleryStill]'.


GalleryStill                                                             
------------

..  topic:: Description

    This class does not provide any API functions but the object type is used by functions in other classes.

    **Returns** Bool
