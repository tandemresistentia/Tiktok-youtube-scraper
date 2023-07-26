powershell -command "Start-Sleep -s 5"

Start /WAIT /B "" "C:\Users\Death\Desktop\Main Uploader\NBAChannel\main.bat - Acceso directo"

Start /WAIT /B "" "C:\Users\Death\Desktop\Main Uploader\EuropeanFootballChannel\main.bat - Acceso directo"

Start /WAIT /B "" "C:\Users\Death\Desktop\Main Uploader\NFLChannel\main.bat - Acceso directo"

Start /WAIT /B "" "C:\Users\Death\Desktop\Main Uploader\DogChannel\maindog.bat - Acceso directo"

Start /WAIT /B "" "C:\Users\Death\Desktop\Main Uploader\CatChannel\main.bat - Acceso directo"

Start /WAIT /B "" "C:\Users\Death\Desktop\Main Uploader\TwitchDownloader\maintwitch.bat - Acceso directo"


call C:\Users\Death\anaconda3/Scripts/activate.bat C:\Users\Death\anaconda3
C:\Users\Death\anaconda3\python.exe "C:\Users\Death\Desktop\Main Uploader/delete.py"

exit
exit

