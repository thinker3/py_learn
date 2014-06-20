#z::
temp_txt = C:\Users\ken.chen\git\py_learn\windows\word.txt
tempClipboard = %ClipboardAll%
Clipboard =
Send, ^c
;ClipWait  ; if no time limit, it crashes when there is no selection
ClipWait, 1
if (Clipboard == "") {
    Clipboard = %tempClipboard%
    tempClipboard =
    return
}
FileDelete, %temp_txt%
FileAppend, %Clipboard%, %temp_txt%
Clipboard = %tempClipboard%
tempClipboard =
return
