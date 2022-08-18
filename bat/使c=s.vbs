dim a,b,c
a=inputbox("长:")
b=inputbox("宽:")
c=a*b
if c="16" then
msgbox("聪敏")
else
CreateObject("SAPI.SpVoice").Speak"你是猪么，这都不会，哈哈"
end if