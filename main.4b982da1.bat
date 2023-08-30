@echo off
setlocal

set "filename=main.4b982da1.txt"

:: Check if the file exists
if not exist "%filename%" (
    echo 0 > "%filename%"
)

:: Read the current number from the file
set /p number=<"%filename%"

:: Add 1 to the number
set /a number+=1

:: Write the updated number back to the file
echo %number% > "%filename%"

echo Number increased to %number%

cd /d "C:\Users\Death\Desktop\Projects\Main Uploader"

git init

git add .

git commit -m "final"
git push
pause
endlocal
