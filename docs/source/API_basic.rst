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

  GetMediaPool()                                  **Returns** MediaPool          ..  topic:: Description

	  Returns the Media Pool object.
  GetTimelineCount()                              **Returns** int                ..  topic:: Description

	  Returns the number of timelines currently present in the project.
  GetTimelineByIndex(idx)                         **Returns** Timeline           ..  topic:: Description

	  Returns timeline at the given index, 1 <= idx <= project.GetTimelineCount()
  GetCurrentTimeline()                            **Returns** Timeline           ..  topic:: Description

	  Returns the currently loaded timeline.
  SetCurrentTimeline(timeline)                    **Returns** Bool               ..  topic:: Description

	  Sets given timeline as current timeline for the project. Returns True if successful.
  GetGallery()                                    **Returns** Gallery            ..  topic:: Description

	  Returns the Gallery object.
  GetName()                                       **Returns** string             ..  topic:: Description

	  Returns project name.
  SetName(projectName)                            **Returns** Bool               ..  topic:: Description

	  Sets project name if given projectname (string) is unique.
  GetPresetList()                                 **Returns** [presets...]       ..  topic:: Description

	  Returns a list of presets and their information.
  SetPreset(presetName)                           **Returns** Bool               ..  topic:: Description

	  Sets preset by given presetName (string) into project.
  AddRenderJob()                                  **Returns** string             ..  topic:: Description

	  Adds a render job based on current render settings to the render queue. Returns a unique job id (string) for the new render job.
  DeleteRenderJob(jobId)                          **Returns** Bool               ..  topic:: Description

	  Deletes render job for input job id (string).
  DeleteAllRenderJobs()                           **Returns** Bool               ..  topic:: Description

	  Deletes all render jobs in the queue.
  GetRenderJobList()                              **Returns** [render jobs...]   ..  topic:: Description

	  Returns a list of render jobs and their information.
  GetRenderPresetList()                           **Returns** [presets...]       ..  topic:: Description

	  Returns a list of render presets and their information.
  StartRendering(jobId1, jobId2, ...)             **Returns** Bool               ..  topic:: Description

	  Starts rendering jobs indicated by the input job ids.
  StartRendering([jobIds...], isInteractiveMode=False)    **Returns** Bool       ..  topic:: Description

	  Starts rendering jobs indicated by the input job ids.
                                                                         ..  topic:: Description

	  The optional "isInteractiveMode", when set, enables error feedback in the UI during rendering.
  StartRendering(isInteractiveMode=False)                 **Returns** Bool       ..  topic:: Description

	  Starts rendering all queued render jobs. 
                                                                         ..  topic:: Description

	  The optional "isInteractiveMode", when set, enables error feedback in the UI during rendering.
  StopRendering()                                 **Returns** None               ..  topic:: Description

	  Stops any current render processes.
  IsRenderingInProgress()                         **Returns** Bool               ..  topic:: Description

	  Returns True if rendering is in progress.
  LoadRenderPreset(presetName)                    **Returns** Bool               ..  topic:: Description

	  Sets a preset as current preset for rendering if presetName (string) exists.
  SaveAsNewRenderPreset(presetName)               **Returns** Bool               ..  topic:: Description

	  Creates new render preset by given name if presetName(string) is unique.
  SetRenderSettings({settings})                   **Returns** Bool               ..  topic:: Description

	  Sets given settings for rendering. Settings is a dict, with support for the keys:
                                                                         ..  topic:: Description

	  Refer to "Looking up render settings" section for information for supported settings
  GetRenderJobStatus(jobId)                       **Returns** {status info}      ..  topic:: Description

	  Returns a dict with job status and completion percentage of the job by given jobId (string).
  GetSetting(settingName)                         **Returns** string             ..  topic:: Description

	  Returns value of project setting (indicated by settingName, string). Check the section below for more information.
  SetSetting(settingName, settingValue)           **Returns** Bool               ..  topic:: Description

	  Sets the project setting (indicated by settingName, string) to the value (settingValue, string). Check the section below for more information.
  GetRenderFormats()                              **Returns** {render formats..} ..  topic:: Description

	  Returns a dict (format -> file extension) of available render formats.
  GetRenderCodecs(renderFormat)                   **Returns** {render codecs...} ..  topic:: Description

	  Returns a dict (codec description -> codec name) of available codecs for given render format (string).
  GetCurrentRenderFormatAndCodec()                **Returns** {format, codec}    ..  topic:: Description

	  Returns a dict with currently selected format 'format' and render codec 'codec'.
  SetCurrentRenderFormatAndCodec(format, codec)   **Returns** Bool               ..  topic:: Description

	  Sets given render format (string) and render codec (string) as options for rendering.
  GetCurrentRenderMode()                          **Returns** int                ..  topic:: Description

	  Returns the render mode: 0 - Individual clips, 1 - Single clip.
  SetCurrentRenderMode(renderMode)                **Returns** Bool               ..  topic:: Description

	  Sets the render mode. Specify renderMode = 0 for Individual clips, 1 for Single clip.
  GetRenderResolutions(format, codec)             **Returns** [{Resolution}]     ..  topic:: Description

	  Returns list of resolutions applicable for the given render format (string) and render codec (string). Returns full list of resolutions if no argument is provided. Each element in the list is a dictionary with 2 keys "Width" and "Height".
  RefreshLUTList()                                **Returns** Bool               ..  topic:: Description

	  Refreshes LUT List

MediaStorage
------------

  GetMountedVolumeList()                          **Returns** [paths...]         ..  topic:: Description

	  Returns list of folder paths corresponding to mounted volumes displayed in Resolve’s Media Storage.
  GetSubFolderList(folderPath)                    **Returns** [paths...]         ..  topic:: Description

	  Returns list of folder paths in the given absolute folder path.
  GetFileList(folderPath)                         **Returns** [paths...]         ..  topic:: Description

	  Returns list of media and file listings in the given absolute folder path. Note that media listings may be logically consolidated entries.
  RevealInStorage(path)                           **Returns** Bool               ..  topic:: Description

	  Expands and displays given file/folder path in Resolve’s Media Storage.
  AddItemListToMediaPool(item1, item2, ...)       **Returns** [clips...]         ..  topic:: Description

	  Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is one or more file/folder paths. Returns a list of the MediaPoolItems created.
  AddItemListToMediaPool([items...])              **Returns** [clips...]         ..  topic:: Description

	  Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is an array of file/folder paths. Returns a list of the MediaPoolItems created.
  AddClipMattesToMediaPool(MediaPoolItem, [paths], stereoEye) **Returns** Bool   ..  topic:: Description

	  Adds specified media files as mattes for the specified MediaPoolItem. StereoEye is an optional argument for specifying which eye to add the matte to for stereo clips ("left" or "right"). Returns True if successful.
  AddTimelineMattesToMediaPool([paths])           **Returns** [MediaPoolItems]   ..  topic:: Description

	  Adds specified media files as timeline mattes in current media pool folder. Returns a list of created MediaPoolItems.

MediaPool
---------

  GetRootFolder()                                 **Returns** Folder             
  ..  topic:: Description

	    Returns root Folder of Media Pool
  
  AddSubFolder(folder, name)                      **Returns** Folder             
  ..  topic:: Description

	  Adds new subfolder under specified Folder object with the given name.
  
  CreateEmptyTimeline(name)                       **Returns** Timeline           
  ..  topic:: Description

	  Adds new timeline with given name.
  AppendToTimeline(clip1, clip2, ...)             **Returns** [TimelineItem]     
  ..  topic:: Description

	  Appends specified MediaPoolItem objects in the current timeline. Returns the list of appended timelineItems.
  AppendToTimeline([clips])                       **Returns** [TimelineItem]     
  ..  topic:: Description

	  Appends specified MediaPoolItem objects in the current timeline. Returns the list of appended timelineItems.
  AppendToTimeline([{clipInfo}, ...])             **Returns** [TimelineItem]     
  ..  topic:: Description

	  Appends list of clipInfos specified as dict of "mediaPoolItem", "startFrame" (int), "endFrame" (int), (optional) "mediaType" (int; 1 - Video only, 2 - Audio only). Returns the list of appended timelineItems.
  CreateTimelineFromClips(name, clip1, clip2,...) **Returns** Timeline           
  ..  topic:: Description

	  Creates new timeline with specified name, and appends the specified MediaPoolItem objects.
  CreateTimelineFromClips(name, [clips])          **Returns** Timeline           
  ..  topic:: Description

	  Creates new timeline with specified name, and appends the specified MediaPoolItem objects.
  CreateTimelineFromClips(name, [{clipInfo}])     **Returns** Timeline           
  ..  topic:: Description

	  Creates new timeline with specified name, appending the list of clipInfos specified as a dict of "mediaPoolItem", "startFrame" (int), "endFrame" (int).
  ImportTimelineFromFile(filePath, {importOptions}) **Returns** Timeline         
  ..  topic:: Description

	  Creates timeline based on parameters within given file and optional importOptions dict, with support for the keys:
                                                                         
                                                                         ..  topic:: Description

	  "timelineName": string, specifies the name of the timeline to be created
                                                                         ..  topic:: Description

	  "importSourceClips": Bool, specifies whether source clips should be imported, True by default
                                                                         ..  topic:: Description

	  "sourceClipsPath": string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if "importSourceClips" is True
                                                                         ..  topic:: Description

	  "sourceClipsFolders": List of Media Pool folder objects to search for source clips if the media is not present in current folder and if "importSourceClips" is False
                                                                         ..  topic:: Description

	  "interlaceProcessing": Bool, specifies whether to enable interlace processing on the imported timeline being created. valid only for AAF import
  DeleteTimelines([timeline])                     **Returns** Bool               ..  topic:: Description

	  Deletes specified timelines in the media pool.
  GetCurrentFolder()                              **Returns** Folder             ..  topic:: Description

	  Returns currently selected Folder.
  SetCurrentFolder(Folder)                        **Returns** Bool               ..  topic:: Description

	  Sets current folder by given Folder.
  DeleteClips([clips])                            **Returns** Bool               ..  topic:: Description

	  Deletes specified clips or timeline mattes in the media pool
  DeleteFolders([subfolders])                     **Returns** Bool               ..  topic:: Description

	  Deletes specified subfolders in the media pool
  MoveClips([clips], targetFolder)                **Returns** Bool               ..  topic:: Description

	  Moves specified clips to target folder.
  MoveFolders([folders], targetFolder)            **Returns** Bool               ..  topic:: Description

	  Moves specified folders to target folder.
  GetClipMatteList(MediaPoolItem)                 **Returns** [paths]            ..  topic:: Description

	  Get mattes for specified MediaPoolItem, as a list of paths to the matte files.
  GetTimelineMatteList(Folder)                    **Returns** [MediaPoolItems]   ..  topic:: Description

	  Get mattes in specified Folder, as list of MediaPoolItems.
  DeleteClipMattes(MediaPoolItem, [paths])        **Returns** Bool               ..  topic:: Description

	  Delete mattes based on their file paths, for specified MediaPoolItem. Returns True on success.
  RelinkClips([MediaPoolItem], folderPath)        **Returns** Bool               ..  topic:: Description

	  Update the folder location of specified media pool clips with the specified folder path.
  UnlinkClips([MediaPoolItem])                    **Returns** Bool               ..  topic:: Description

	  Unlink specified media pool clips.
  ImportMedia([items...])                         **Returns** [MediaPoolItems]   ..  topic:: Description

	  Imports specified file/folder paths into current Media Pool folder. Input is an array of file/folder paths. Returns a list of the MediaPoolItems created.
  ImportMedia([{clipInfo}])                       **Returns** [MediaPoolItems]   ..  topic:: Description

	  Imports file path(s) into current Media Pool folder as specified in list of clipInfo dict. Returns a list of the MediaPoolItems created.
                                                                         ..  topic:: Description

	  Each clipInfo gets imported as one MediaPoolItem unless 'Show Individual Frames' is turned on.
                                                                         ..  topic:: Description

	  Example: ImportMedia([{"FilePath":"file_%03d.dpx", "StartIndex":1, "EndIndex":100}]) would import clip "file_[001-100].dpx".
  ExportMetadata(fileName, [clips])               **Returns** Bool               ..  topic:: Description

	  Exports metadata of specified clips to 'fileName' in CSV format.
                                                                         ..  topic:: Description

	  If no clips are specified, all clips from media pool will be used.

Folder
------

  GetClipList()                                   **Returns** [clips...]         ..  topic:: Description

	  Returns a list of clips (items) within the folder.
  GetName()                                       **Returns** string             ..  topic:: Description

	  Returns the media folder name.
  GetSubFolderList()                              **Returns** [folders...]       ..  topic:: Description

	  Returns a list of subfolders in the folder.

MediaPoolItem
-------------

  GetName()                                       **Returns** string             ..  topic:: Description

	  Returns the clip name.
  GetMetadata(metadataType=None)                  **Returns** string|dict        ..  topic:: Description

	  Returns the metadata value for the key 'metadataType'.
                                                                         ..  topic:: Description

	  If no argument is specified, a dict of all set metadata properties is returned.
  SetMetadata(metadataType, metadataValue)        **Returns** Bool               ..  topic:: Description

	  Sets the given metadata to metadataValue (string). Returns True if successful.
  SetMetadata({metadata})                         **Returns** Bool               ..  topic:: Description

	  Sets the item metadata with specified 'metadata' dict. Returns True if successful.
  GetMediaId()                                    **Returns** string             ..  topic:: Description

	  Returns the unique ID for the MediaPoolItem.
  AddMarker(frameId, color, name, note, duration, **Returns** Bool               ..  topic:: Description

	  Creates a new marker at given frameId position and with given marker information. 'customData' is optional and helps to attach user specific data to the marker.
            customData)
  GetMarkers()                                    **Returns** {markers...}       ..  topic:: Description

	  Returns a dict (frameId -> {information}) of all markers and dicts with their information.
                                                                         ..  topic:: Description

	  Example of output format: {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...}
                                                                         ..  topic:: Description

	  In the above example - there is one 'Green' marker at offset 96 (position of the marker)
  GetMarkerByCustomData(customData)               **Returns** {markers...}       ..  topic:: Description

	  Returns marker {information} for the first matching marker with specified customData.
  UpdateMarkerCustomData(frameId, customData)     **Returns** Bool               ..  topic:: Description

	  Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.
  GetMarkerCustomData(frameId)                    **Returns** string             ..  topic:: Description

	  Returns customData string for the marker at given frameId position.
  DeleteMarkersByColor(color)                     **Returns** Bool               ..  topic:: Description

	  Delete all markers of the specified color from the media pool item. "All" as argument deletes all color markers.
  DeleteMarkerAtFrame(frameNum)                   **Returns** Bool               ..  topic:: Description

	  Delete marker at frame number from the media pool item.
  DeleteMarkerByCustomData(customData)            **Returns** Bool               ..  topic:: Description

	  Delete first matching marker with specified customData.
  AddFlag(color)                                  **Returns** Bool               ..  topic:: Description

	  Adds a flag with given color (string).
  GetFlagList()                                   **Returns** [colors...]        ..  topic:: Description

	  Returns a list of flag colors assigned to the item.
  ClearFlags(color)                               **Returns** Bool               ..  topic:: Description

	  Clears the flag of the given color if one exists. An "All" argument is supported and clears all flags.
  GetClipColor()                                  **Returns** string             ..  topic:: Description

	  Returns the item color as a string.
  SetClipColor(colorName)                         **Returns** Bool               ..  topic:: Description

	  Sets the item color based on the colorName (string).
  ClearClipColor()                                **Returns** Bool               ..  topic:: Description

	  Clears the item color.
  GetClipProperty(propertyName=None)              **Returns** string|dict        ..  topic:: Description

	  Returns the property value for the key 'propertyName'. 
                                                                         ..  topic:: Description

	  If no argument is specified, a dict of all clip properties is returned. Check the section below for more information.
  SetClipProperty(propertyName, propertyValue)    **Returns** Bool               ..  topic:: Description

	  Sets the given property to propertyValue (string). Check the section below for more information.
  LinkProxyMedia(proxyMediaFilePath)              **Returns** Bool               ..  topic:: Description

	  Links proxy media located at path specified by arg 'proxyMediaFilePath' with the current clip. 'proxyMediaFilePath' should be absolute clip path.
  UnlinkProxyMedia()                              **Returns** Bool               ..  topic:: Description

	  Unlinks any proxy media associated with clip.
  ReplaceClip(filePath)                           **Returns** Bool               ..  topic:: Description

	  Replaces the underlying asset and metadata of MediaPoolItem with the specified absolute clip path.

Timeline
--------

  GetName()                                       **Returns** string             ..  topic:: Description

	  Returns the timeline name.
  SetName(timelineName)                           **Returns** Bool               ..  topic:: Description

	  Sets the timeline name if timelineName (string) is unique. Returns True if successful.
  GetStartFrame()                                 **Returns** int                ..  topic:: Description

	  Returns the frame number at the start of timeline.
  GetEndFrame()                                   **Returns** int                ..  topic:: Description

	  Returns the frame number at the end of timeline.
  GetTrackCount(trackType)                        **Returns** int                ..  topic:: Description

	  Returns the number of tracks for the given track type ("audio", "video" or "subtitle").
  GetItemListInTrack(trackType, index)            **Returns** [items...]         ..  topic:: Description

	  Returns a list of timeline items on that track (based on trackType and index). 1 <= index <= GetTrackCount(trackType).
  AddMarker(frameId, color, name, note, duration, **Returns** Bool               ..  topic:: Description

	  Creates a new marker at given frameId position and with given marker information. 'customData' is optional and helps to attach user specific data to the marker.
            customData)
  GetMarkers()                                    **Returns** {markers...}       ..  topic:: Description

	  Returns a dict (frameId -> {information}) of all markers and dicts with their information.
                                                                         ..  topic:: Description

	  Example: a value of {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...} indicates a single green marker at timeline offset 96
  GetMarkerByCustomData(customData)               **Returns** {markers...}       ..  topic:: Description

	  Returns marker {information} for the first matching marker with specified customData.
  UpdateMarkerCustomData(frameId, customData)     **Returns** Bool               ..  topic:: Description

	  Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.
  GetMarkerCustomData(frameId)                    **Returns** string             ..  topic:: Description

	  Returns customData string for the marker at given frameId position.
  DeleteMarkersByColor(color)                     **Returns** Bool               ..  topic:: Description

	  Deletes all timeline markers of the specified color. An "All" argument is supported and deletes all timeline markers.
  DeleteMarkerAtFrame(frameNum)                   **Returns** Bool               ..  topic:: Description

	  Deletes the timeline marker at the given frame number.
  DeleteMarkerByCustomData(customData)            **Returns** Bool               ..  topic:: Description

	  Delete first matching marker with specified customData.
  ApplyGradeFromDRX(path, gradeMode, item1, item2, ...)**Returns** Bool          ..  topic:: Description

	  Loads a still from given file path (string) and applies grade to Timeline Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames aligned".
  ApplyGradeFromDRX(path, gradeMode, [items])     **Returns** Bool               ..  topic:: Description

	  Loads a still from given file path (string) and applies grade to Timeline Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames aligned".
  GetCurrentTimecode()                            **Returns** string             ..  topic:: Description

	  Returns a string timecode representation for the current playhead position, while on Cut, Edit, Color, Fairlight and Deliver pages.
  SetCurrentTimecode(timecode)                    **Returns** Bool               ..  topic:: Description

	  Sets current playhead position from input timecode for Cut, Edit, Color, Fairlight and Deliver pages.
  GetCurrentVideoItem()                           **Returns** item               ..  topic:: Description

	  Returns the current video timeline item.
  GetCurrentClipThumbnailImage()                  **Returns** {thumbnailData}    ..  topic:: Description

	  Returns a dict (keys "width", "height", "format" and "data") with data containing raw thumbnail image data (RGB 8-bit image data encoded in base64 format) for current media in the Color Page.
                                                                         ..  topic:: Description

	  An example of how to retrieve and interpret thumbnails is provided in 6_get_current_media_thumbnail.py in the Examples folder.
  GetTrackName(trackType, trackIndex)             **Returns** string             ..  topic:: Description

	  Returns the track name for track indicated by trackType ("audio", "video" or "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType).
  SetTrackName(trackType, trackIndex, name)       **Returns** Bool               ..  topic:: Description

	  Sets the track name (string) for track indicated by trackType ("audio", "video" or "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType).
  DuplicateTimeline(timelineName)                 **Returns** timeline           ..  topic:: Description

	  Duplicates the timeline and returns the created timeline, with the (optional) timelineName, on success.
  CreateCompoundClip([timelineItems], {clipInfo}) **Returns** timelineItem       ..  topic:: Description

	  Creates a compound clip of input timeline items with an optional clipInfo map: {"startTimecode" : "00:00:00:00", "name" : "Compound Clip 1"}. It returns the created timeline item.
  CreateFusionClip([timelineItems])               **Returns** timelineItem       ..  topic:: Description

	  Creates a Fusion clip of input timeline items. It returns the created timeline item.
  ImportIntoTimeline(filePath, {importOptions})   **Returns** Bool               ..  topic:: Description

	  Imports timeline items from an AAF file and optional importOptions dict into the timeline, with support for the keys:
                                                                         ..  topic:: Description

	  "autoImportSourceClipsIntoMediaPool": Bool, specifies if source clips should be imported into media pool, True by default
                                                                         ..  topic:: Description

	  "ignoreFileExtensionsWhenMatching": Bool, specifies if file extensions should be ignored when matching, False by default
                                                                         ..  topic:: Description

	  "linkToSourceCameraFiles": Bool, specifies if link to source camera files should be enabled, False by default
                                                                         ..  topic:: Description

	  "useSizingInfo": Bool, specifies if sizing information should be used, False by default
                                                                         ..  topic:: Description

	  "importMultiChannelAudioTracksAsLinkedGroups": Bool, specifies if multi-channel audio tracks should be imported as linked groups, False by default
                                                                         ..  topic:: Description

	  "insertAdditionalTracks": Bool, specifies if additional tracks should be inserted, True by default
                                                                         ..  topic:: Description

	  "insertWithOffset": string, specifies insert with offset value in timecode format - defaults to "00:00:00:00", applicable if "insertAdditionalTracks" is False
                                                                         ..  topic:: Description

	  "sourceClipsPath": string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if "ignoreFileExtensionsWhenMatching" is True
                                                                         ..  topic:: Description

	  "sourceClipsFolders": string, list of Media Pool folder objects to search for source clips if the media is not present in current folder

  Export(fileName, exportType, exportSubtype)     **Returns** Bool               ..  topic:: Description

	  Exports timeline to 'fileName' as per input exportType & exportSubtype format.
                                                                         ..  topic:: Description

	  Refer to section "Looking up timeline exports properties" for information on the parameters.
  GetSetting(settingName)                         **Returns** string             ..  topic:: Description

	  Returns value of timeline setting (indicated by settingName : string). Check the section below for more information.
  SetSetting(settingName, settingValue)           **Returns** Bool               ..  topic:: Description

	  Sets timeline setting (indicated by settingName : string) to the value (settingValue : string). Check the section below for more information.
  InsertGeneratorIntoTimeline(generatorName)      **Returns** TimelineItem       ..  topic:: Description

	  Inserts a generator (indicated by generatorName : string) into the timeline.
  InsertFusionGeneratorIntoTimeline(generatorName) **Returns** TimelineItem      ..  topic:: Description

	  Inserts a Fusion generator (indicated by generatorName : string) into the timeline.
  InsertOFXGeneratorIntoTimeline(generatorName)   **Returns** TimelineItem       ..  topic:: Description

	  Inserts an OFX generator (indicated by generatorName : string) into the timeline.
  InsertTitleIntoTimeline(titleName)              **Returns** TimelineItem       ..  topic:: Description

	  Inserts a title (indicated by titleName : string) into the timeline.
  InsertFusionTitleIntoTimeline(titleName)        **Returns** TimelineItem       ..  topic:: Description

	  Inserts a Fusion title (indicated by titleName : string) into the timeline.
  GrabStill()                                     **Returns** galleryStill       ..  topic:: Description

	  Grabs still from the current video clip. Returns a GalleryStill object.
  GrabAllStills(stillFrameSource)                 **Returns** [galleryStill]     ..  topic:: Description

	  Grabs stills from all the clips of the timeline at 'stillFrameSource' (1 - First frame, 2 - Middle frame). Returns the list of GalleryStill objects.

TimelineItem
------------

  GetName()                                       **Returns** string             ..  topic:: Description

	  Returns the item name.
  GetDuration()                                   **Returns** int                ..  topic:: Description

	  Returns the item duration.
  GetEnd()                                        **Returns** int                ..  topic:: Description

	  Returns the end frame position on the timeline.
  GetFusionCompCount()                            **Returns** int                ..  topic:: Description

	  Returns number of Fusion compositions associated with the timeline item.
  GetFusionCompByIndex(compIndex)                 **Returns** fusionComp         ..  topic:: Description

	  Returns the Fusion composition object based on given index. 1 <= compIndex <= timelineItem.GetFusionCompCount()
  GetFusionCompNameList()                         **Returns** [names...]         ..  topic:: Description

	  Returns a list of Fusion composition names associated with the timeline item.
  GetFusionCompByName(compName)                   **Returns** fusionComp         ..  topic:: Description

	  Returns the Fusion composition object based on given name.
  GetLeftOffset()                                 **Returns** int                ..  topic:: Description

	  Returns the maximum extension by frame for clip from left side.
  GetRightOffset()                                **Returns** int                ..  topic:: Description

	  Returns the maximum extension by frame for clip from right side.
  GetStart()                                      **Returns** int                ..  topic:: Description

	  Returns the start frame position on the timeline.
  SetProperty(propertyKey, propertyValue)         **Returns** Bool               ..  topic:: Description

	  Sets the value of property "propertyKey" to value "propertyValue"
                                                                         ..  topic:: Description

	  Refer to "Looking up Timeline item properties" for more information
  GetProperty(propertyKey)                        **Returns** int/[key:value]    ..  topic:: Description

	  returns the value of the specified key
                                                                         ..  topic:: Description

	  if no key is specified, the method returns a dictionary(python) or table(lua) for all supported keys
  AddMarker(frameId, color, name, note, duration, **Returns** Bool               ..  topic:: Description

	  Creates a new marker at given frameId position and with given marker information. 'customData' is optional and helps to attach user specific data to the marker.
            customData)
  GetMarkers()                                    **Returns** {markers...}       ..  topic:: Description

	  Returns a dict (frameId -> {information}) of all markers and dicts with their information.
                                                                         ..  topic:: Description

	  Example: a value of {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...} indicates a single green marker at clip offset 96
  GetMarkerByCustomData(customData)               **Returns** {markers...}       ..  topic:: Description

	  Returns marker {information} for the first matching marker with specified customData.
  UpdateMarkerCustomData(frameId, customData)     **Returns** Bool               ..  topic:: Description

	  Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers.
  GetMarkerCustomData(frameId)                    **Returns** string             ..  topic:: Description

	  Returns customData string for the marker at given frameId position.
  DeleteMarkersByColor(color)                     **Returns** Bool               ..  topic:: Description

	  Delete all markers of the specified color from the timeline item. "All" as argument deletes all color markers.
  DeleteMarkerAtFrame(frameNum)                   **Returns** Bool               ..  topic:: Description

	  Delete marker at frame number from the timeline item.
  DeleteMarkerByCustomData(customData)            **Returns** Bool               ..  topic:: Description

	  Delete first matching marker with specified customData.
  AddFlag(color)                                  **Returns** Bool               ..  topic:: Description

	  Adds a flag with given color (string).
  GetFlagList()                                   **Returns** [colors...]        ..  topic:: Description

	  Returns a list of flag colors assigned to the item.
  ClearFlags(color)                               **Returns** Bool               ..  topic:: Description

	  Clear flags of the specified color. An "All" argument is supported to clear all flags. 
  GetClipColor()                                  **Returns** string             ..  topic:: Description

	  Returns the item color as a string.
  SetClipColor(colorName)                         **Returns** Bool               ..  topic:: Description

	  Sets the item color based on the colorName (string).
  ClearClipColor()                                **Returns** Bool               ..  topic:: Description

	  Clears the item color.
  AddFusionComp()                                 **Returns** fusionComp         ..  topic:: Description

	  Adds a new Fusion composition associated with the timeline item.
  ImportFusionComp(path)                          **Returns** fusionComp         ..  topic:: Description

	  Imports a Fusion composition from given file path by creating and adding a new composition for the item.
  ExportFusionComp(path, compIndex)               **Returns** Bool               ..  topic:: Description

	  Exports the Fusion composition based on given index to the path provided.
  DeleteFusionCompByName(compName)                **Returns** Bool               ..  topic:: Description

	  Deletes the named Fusion composition.
  LoadFusionCompByName(compName)                  **Returns** fusionComp         ..  topic:: Description

	  Loads the named Fusion composition as the active composition.
  RenameFusionCompByName(oldName, newName)        **Returns** Bool               ..  topic:: Description

	  Renames the Fusion composition identified by oldName.
  AddVersion(versionName, versionType)            **Returns** Bool               ..  topic:: Description

	  Adds a new color version for a video clipbased on versionType (0 - local, 1 - remote).
  GetCurrentVersion()                             **Returns** {versionName...}   ..  topic:: Description

	  Returns the current version of the video clip. The returned value will have the keys versionName and versionType(0 - local, 1 - remote).
  DeleteVersionByName(versionName, versionType)   **Returns** Bool               ..  topic:: Description

	  Deletes a color version by name and versionType (0 - local, 1 - remote).
  LoadVersionByName(versionName, versionType)     **Returns** Bool               ..  topic:: Description

	  Loads a named color version as the active version. versionType: 0 - local, 1 - remote.
  RenameVersionByName(oldName, newName, versionType)**Returns** Bool             ..  topic:: Description

	  Renames the color version identified by oldName and versionType (0 - local, 1 - remote).
  GetVersionNameList(versionType)                 **Returns** [names...]         ..  topic:: Description

	  Returns a list of all color versions for the given versionType (0 - local, 1 - remote).
  GetMediaPoolItem()                              **Returns** MediaPoolItem      ..  topic:: Description

	  Returns the media pool item corresponding to the timeline item if one exists.
  GetStereoConvergenceValues()                    **Returns** {keyframes...}     ..  topic:: Description

	  Returns a dict (offset -> value) of keyframe offsets and respective convergence values.
  GetStereoLeftFloatingWindowParams()             **Returns** {keyframes...}     ..  topic:: Description

	  For the LEFT eye -> returns a dict (offset -> dict) of keyframe offsets and respective floating window params. Value at particular offset includes the left, right, top and bottom floating window values.
  GetStereoRightFloatingWindowParams()            **Returns** {keyframes...}     ..  topic:: Description

	  For the RIGHT eye -> returns a dict (offset -> dict) of keyframe offsets and respective floating window params. Value at particular offset includes the left, right, top and bottom floating window values.
  SetLUT(nodeIndex, lutPath)                      **Returns** Bool               ..  topic:: Description

	  Sets LUT on the node mapping the node index provided, 1 <= nodeIndex <= total number of nodes.
                                                                         ..  topic:: Description

	  The lutPath can be an absolute path, or a relative path (based off custom LUT paths or the master LUT path).
                                                                         ..  topic:: Description

	  The operation is successful for valid lut paths that Resolve has already discovered (see Project.RefreshLUTList).
  SetCDL([CDL map])                               **Returns** Bool               ..  topic:: Description

	  Keys of map are: "NodeIndex", "Slope", "Offset", "Power", "Saturation", where 1 <= NodeIndex <= total number of nodes.
                                                                         ..  topic:: Description

	  Example python code - SetCDL({"NodeIndex" : "1", "Slope" : "0.5 0.4 0.2", "Offset" : "0.4 0.3 0.2", "Power" : "0.6 0.7 0.8", "Saturation" : "0.65"})
  AddTake(mediaPoolItem, startFrame, endFrame)    **Returns** Bool               ..  topic:: Description

	  Adds mediaPoolItem as a new take. Initializes a take selector for the timeline item if needed. By default, the full clip extents is added. startFrame (int) and endFrame (int) are optional arguments used to specify the extents.
  GetSelectedTakeIndex()                          **Returns** int                ..  topic:: Description

	  Returns the index of the currently selected take, or 0 if the clip is not a take selector.
  GetTakesCount()                                 **Returns** int                ..  topic:: Description

	  Returns the number of takes in take selector, or 0 if the clip is not a take selector.
  GetTakeByIndex(idx)                             **Returns** {takeInfo...}      ..  topic:: Description

	  Returns a dict (keys "startFrame", "endFrame" and "mediaPoolItem") with take info for specified index.
  DeleteTakeByIndex(idx)                          **Returns** Bool               ..  topic:: Description

	  Deletes a take by index, 1 <= idx <= number of takes.
  SelectTakeByIndex(idx)                          **Returns** Bool               ..  topic:: Description

	  Selects a take by index, 1 <= idx <= number of takes.
  FinalizeTake()                                  **Returns** Bool               ..  topic:: Description

	  Finalizes take selection.
  CopyGrades([tgtTimelineItems])                  **Returns** Bool               ..  topic:: Description

	  Copies the current grade to all the items in tgtTimelineItems list. Returns True on success and False if any error occured.

Gallery
-------

  GetAlbumName(galleryStillAlbum)                 **Returns** string             ..  topic:: Description

	  Returns the name of the GalleryStillAlbum object 'galleryStillAlbum'.
  SetAlbumName(galleryStillAlbum, albumName)      **Returns** Bool               ..  topic:: Description

	  Sets the name of the GalleryStillAlbum object 'galleryStillAlbum' to 'albumName'.
  GetCurrentStillAlbum()                          **Returns** galleryStillAlbum  ..  topic:: Description

	  Returns current album as a GalleryStillAlbum object.
  SetCurrentStillAlbum(galleryStillAlbum)         **Returns** Bool               ..  topic:: Description

	  Sets current album to GalleryStillAlbum object 'galleryStillAlbum'.
  GetGalleryStillAlbums()                         **Returns** [galleryStillAlbum] ..  topic:: Description

	  Returns the gallery albums as a list of GalleryStillAlbum objects.

GalleryStillAlbum
-----------------

  GetStills()                                     **Returns** [galleryStill]     ..  topic:: Description

	  Returns the list of GalleryStill objects in the album.
  GetLabel(galleryStill)                          **Returns** string             ..  topic:: Description

	  Returns the label of the galleryStill.
  SetLabel(galleryStill, label)                   **Returns** Bool               ..  topic:: Description

	  Sets the new 'label' to GalleryStill object 'galleryStill'.
  ExportStills([galleryStill], folderPath, filePrefix, format) **Returns** Bool  ..  topic:: Description

	  Exports list of GalleryStill objects '[galleryStill]' to directory 'folderPath', with filename prefix 'filePrefix', using file format 'format' (supported formats: dpx, cin, tif, jpg, png, ppm, bmp, xpm).
  DeleteStills([galleryStill])                    **Returns** Bool               ..  topic:: Description

	  Deletes specified list of GalleryStill objects '[galleryStill]'.

GalleryStill                                                             ..  topic:: Description

	  This class does not provide any API functions but the object type is used by functions in other classes.
------------
