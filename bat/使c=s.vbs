dim a,b,c
a=inputbox("��:")
b=inputbox("��:")
c=a*b
if c="16" then
msgbox("����")
else
CreateObject("SAPI.SpVoice").Speak"������ô���ⶼ���ᣬ����"
end if