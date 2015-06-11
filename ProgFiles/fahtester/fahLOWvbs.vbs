bElevate = False
if WScript.Arguments.Count > 0 Then If WScript.Arguments(WScript.Arguments.Count-1) <> "|" then bElevate = True
if bElevate Or WScript.Arguments.Count = 0 Then ElevateUAC
REM run the following script with admin privilages. start point.

Set fso = CreateObject("Scripting.FileSystemObject")
GetTheParent = fso.GetParentFolderName(Wscript.ScriptFullName)

Set WshShell = WScript.CreateObject ("WScript.Shell")
WshShell.Run GetTheParent & ("\FAHClient.exe --disable-sleep-when-active=true --fold-anon=false --max-slot-errors=10 --max-unit-errors=10 --checkpoint=15 --core-dir=%CD%/FAHClient --core-priority=low --cpu-usage=10 --gpu-usage=5 --cause=Alzheimers --cpus=0 --gpu=true --gui-enabled=false --log-to-screen=false --pause-on-battery=false --power=light --passkey=5a6f57e3783d5e2f493bfcdd6731919f --team=227138 --user=BLDZR"), 0, True
WScript.Sleep 500

REM the above script will be run with admin privilages. end point.
Sub ElevateUAC
    sParms = " |"
    If WScript.Arguments.Count > 0 Then
            For i = WScript.Arguments.Count-1 To 0 Step -1
            sParms = " " & WScript.Arguments(i) & sParms
        Next
    End If
    Set oShell = CreateObject("Shell.Application")
    oShell.ShellExecute "wscript.exe", WScript.ScriptFullName & sParms, , "runas", 1
    WScript.Quit
End Sub