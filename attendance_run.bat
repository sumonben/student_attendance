	@echo off
    cd /d "D:\Django Project\attendance\attendance"  REM Replace with your project's path
    call "D:\Django Project\attendance\.env\Scripts\activate.bat" REM Replace with your virtual environment's activate script
    start  "chrome.exe"  "http://127.0.0.1:8000/"        
	python manage.py runserver 0.0.0.0:8000
    @pause