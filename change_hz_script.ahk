; Bind this script to a specific key, for example, F10
F10::
; Change to 60 Hz
Run, nircmd.exe setdisplay 1920 1080 32 60
return

; Bind another key, for example, F11, to switch to 144 Hz
F11::
; Change to 144 Hz
Run, nircmd.exe setdisplay 1920 1080 32 144
return
