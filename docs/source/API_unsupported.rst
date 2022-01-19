Unsupported Resolve API Functions
---------------------------------

The following API (functions and paraameters) are no longer supported. Use job IDs instead of indices.

Project
  StartRendering(index1, index2, ...)             --> Bool               # Please use unique job ids (string) instead of indices.
  StartRendering([idxs...])                       --> Bool               # Please use unique job ids (string) instead of indices.
  DeleteRenderJobByIndex(idx)                     --> Bool               # Please use unique job ids (string) instead of indices.
  GetRenderJobStatus(idx)                         --> {status info}      # Please use unique job ids (string) instead of indices.
  GetSetting and SetSetting                       --> {}                 # settingName "videoMonitorUseRec601For422SDI" is no longer supported. 
                                                                         # Please use "videoMonitorUseMatrixOverrideFor422SDI" and "videoMonitorMatrixOverrideFor422SDI" instead.
