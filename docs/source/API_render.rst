Render Settings
---------------

This section covers the supported settings for the method SetRenderSettings({settings})

The parameter setting is a dictionary containing the following keys:

- "SelectAllFrames": Bool (when set True, the settings MarkIn and MarkOut are ignored)
- "MarkIn": int
- "MarkOut": int
- "TargetDir": string
- "CustomName": string
- "UniqueFilenameStyle": 0 - Prefix, 1 - Suffix.
- "ExportVideo": Bool
- "ExportAudio": Bool
- "FormatWidth": int
- "FormatHeight": int
- "FrameRate": float (examples: 23.976, 24)
- "PixelAspectRatio": string (for SD resolution: "16_9" or "4_3") (other resolutions: "square" or "cinemascope")
- "VideoQuality" possible values for current codec (if applicable):

  - 0 (int) - will set quality to automatic
  - [1 -> MAX] (int) - will set input bit rate
  - ["Least", "Low", "Medium", "High", "Best"] (String) - will set input quality level
  
- "AudioCodec": string (example: "aac")
- "AudioBitDepth": int
- "AudioSampleRate": int
- "ColorSpaceTag" : string (example: "Same as Project", "AstroDesign")
- "GammaTag" : string (example: "Same as Project", "ACEScct")
- "ExportAlpha": Bool
- "EncodingProfile": string (example: "Main10"). Can only be set for H.264 and H.265.
- "MultiPassEncode": Bool. Can only be set for H.264.
- "AlphaMode": 0 - Premultipled, 1 - Straight. Can only be set if "ExportAlpha" is true.
- "NetworkOptimization": Bool. Only supported by QuickTime and MP4 formats.