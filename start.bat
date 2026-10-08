@echo off
chcp 65001 > nul
echo ========================================================
echo       LeetCode Hot 100 原子化突破体系 (Hot100 Mastery)
echo ========================================================
echo.
echo [1/2] 正在启动后端与本地数据库服务...

cd /d "%~dp0backend"

start "" http://127.0.0.1:8765

if exist "C:\Users\menger\AppData\Local\Programs\Python\Python313\python.exe" (
    "C:\Users\menger\AppData\Local\Programs\Python\Python313\python.exe" server.py
) else (
    python server.py
)

pause
