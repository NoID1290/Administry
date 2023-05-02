Set WshShell = WScript.CreateObject("WScript.Shell")
WshShell.SendKeys "%{F12}"
WScript.Sleep 3000
WshShell.SendKeys "%{F10}"
