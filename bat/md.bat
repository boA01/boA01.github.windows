@echo off
set /p val=��Ŀ:
set /a num=val
for /l %%i in (1, 1, %num%) do mkdir %%i
pause