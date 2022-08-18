@echo off
set /p val=ÊıÄ¿:
set /a num=val
for /l %%i in (1, 1, %num%) do mkdir %%i
pause