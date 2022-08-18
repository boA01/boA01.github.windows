On Error Resume Next
Dim wsh,ye
set wsh=createobject("wscript.shell")
for i=1 to 10
wscript.sleep 200
wsh.AppActivate("‡‡¿≤¿≤¿≤")
wsh.sendKeys "^v"
rem wsh.sendKeys i
wsh.sendKeys "%s"
next
wscript.quit