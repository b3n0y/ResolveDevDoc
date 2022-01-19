Deprecated Resolve API Functions
--------------------------------

The following API functions are deprecated.

ProjectManager
  GetProjectsInCurrentFolder()                    --> {project names...} # Returns a dict of project names in current folder.
  GetFoldersInCurrentFolder()                     --> {folder names...}  # Returns a dict of folder names in current folder.

Project
  GetPresets()                                    --> {presets...}       # Returns a dict of presets and their information.
  GetRenderJobs()                                 --> {render jobs...}   # Returns a dict of render jobs and their information.
  GetRenderPresets()                              --> {presets...}       # Returns a dict of render presets and their information.

MediaStorage
  GetMountedVolumes()                             --> {paths...}         # Returns a dict of folder paths corresponding to mounted volumes displayed in Resolve’s Media Storage.
  GetSubFolders(folderPath)                       --> {paths...}         # Returns a dict of folder paths in the given absolute folder path.
  GetFiles(folderPath)                            --> {paths...}         # Returns a dict of media and file listings in the given absolute folder path. Note that media listings may be logically consolidated entries.
  AddItemsToMediaPool(item1, item2, ...)          --> {clips...}         # Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is one or more file/folder paths. Returns a dict of the MediaPoolItems created.
  AddItemsToMediaPool([items...])                 --> {clips...}         # Adds specified file/folder paths from Media Storage into current Media Pool folder. Input is an array of file/folder paths. Returns a dict of the MediaPoolItems created.

Folder
  GetClips()                                      --> {clips...}         # Returns a dict of clips (items) within the folder.
  GetSubFolders()                                 --> {folders...}       # Returns a dict of subfolders in the folder.

MediaPoolItem
  GetFlags()                                      --> {colors...}        # Returns a dict of flag colors assigned to the item.

Timeline
  GetItemsInTrack(trackType, index)               --> {items...}         # Returns a dict of Timeline items on the video or audio track (based on trackType) at specified

TimelineItem
  GetFusionCompNames()                            --> {names...}         # Returns a dict of Fusion composition names associated with the timeline item.
  GetFlags()                                      --> {colors...}        # Returns a dict of flag colors assigned to the item.
  GetVersionNames(versionType)                    --> {names...}         # Returns a dict of version names by provided versionType: 0 - local, 1 - remote.

