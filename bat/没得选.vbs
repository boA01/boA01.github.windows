do
p=inputbox("you're a pig?yes or no")
if p="yes" then
msgbox("你有自知之明")
CreateObject("SAPI.SpVoice").Speak"you are a pig,哈哈"
exit do
end if
loop


