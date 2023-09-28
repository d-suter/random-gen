@echo off
echo Installing requirements...
python -m pip install -r requirements.txt

echo Starting server...
start python app.py

echo Opening website...
timeout /t 2 /nobreak >nul
start http://127.0.0.1:5000/

@echo on
