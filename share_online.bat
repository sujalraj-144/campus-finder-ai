@echo off
title TKR College - Campus Finder AI (Public Access)
echo ==========================================================
echo   TKR COLLEGE OF ENGINEERING & TECHNOLOGY (AUTONOMOUS)
echo   Campus Finder AI - Server & Global Public Access
echo ==========================================================
echo.
echo 1. Starting Local Streamlit Engine on port 8501...
start "Streamlit Server" /b python -m streamlit run app.py --server.headless true --server.port 8501
timeout /t 3 >nul
echo.
echo 2. Establishing Public Secure Tunnel...
echo Share the generated https://...trycloudflare.com link with everyone!
echo.
.\cloudflared.exe tunnel --protocol http2 --url http://localhost:8501
pause
