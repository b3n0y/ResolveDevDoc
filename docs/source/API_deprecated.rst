Deprecated Resolve API Functions
--------------------------------

The following API functions are deprecated.

* ProjectManager
  
  * GetProjectsInCurrentFolder()                    --> {project names...} # Returns a dict of project names in current folder.
  * GetFoldersInCurrentFolder()                     --> {folder names...}  # Returns a dict of folder names in current folder* .

* Project
  
  * GetPresets()                                    --> {presets...}       # Returns a dict of presets and their information.
  * GetRenderJobs()                                 --> {render jobs...}   # Returns a dict of render jobs and their information.
  * GetRenderPresets()                              --> {presets...}       # Returns a dict of render presets and their information.

* MediaStorage
  
  * GetMountedVolumes()                             --> {paths...}         # Returns a dict of folder paths corresponding to mounted volumes displayed in Resolve’s Media Storage.
  * GetSubFolders(folderPath)                       --> {paths...}         # Returns a dict of folder paths in the given absolute folder path.
  * GetFiles(folderPath)                            --> {paths...}         # Returns a dict of media and file listings in the given absolute folder path. Note that media listings may be logically consolidated entries.
  * AddItemsToMediaPool(item1, item2, ...)          --> {clips...}         # Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is one or more file/folder paths. Returns a dict of the MediaPoolItems created.
  * AddItemsToMediaPool([items...])                 --> {clips...}         # Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is an array of file/folder paths. Returns a dict of the MediaPoolItems created.

* Folder
  
  * GetClips()                                      --> {clips...}         # Returns a dict of clips (items) within the folder.
  * GetSubFolders()                                 --> {folders...}       # Returns a dict of subfolders in the folder.

* MediaPoolItem
  
  * GetFlags()                                      --> {colors...}        # Returns a dict of flag colors assigned to the item* .

* Timeline
  
  * GetItemsInTrack(trackType, index)               --> {items...}         # Returns a dict of Timeline items on the video or audio track (based on trackType) at specified

* TimelineItem
  
  * GetFusionCompNames()                            --> {names...}         # Returns a dict of Fusion composition names associated with the timeline item.
  * GetFlags()                                      --> {colors...}        # Returns a dict of flag colors assigned to the item.
  * GetVersionNames(versionType)                    --> {names...}         # Returns a dict of version names by provided versionType: 0 - local, 1 - remote.


Unsupported Resolve API Functions
---------------------------------

The following API (functions and parameters) are no longer supported. Use job IDs instead of indices.

Project
-------

* StartRendering(index1, index2, ...)             --> Bool               # Please use unique job ids (string) instead of indices.
* StartRendering([idxs...])                       --> Bool               # Please use unique job ids (string) instead of indices.
* DeleteRenderJobByIndex(idx)                     --> Bool               # Please use unique job ids (string) instead of indices.
* GetRenderJobStatus(idx)                         --> {status info}      # Please use unique job ids (string) instead of indices.
* GetSetting and SetSetting                       --> {}                 # settingName videoMonitorUseRec601For422SDI is now replaced with videoMonitorUseMatrixOverrideFor422SDI and videoMonitorMatrixOverrideFor422SDI.
*                                                                        # settingName perfProxyMediaOn is now replaced with perfProxyMediaMode which takes values 0 - disabled, 1 - when available, 2 - when source not available.
