@echo off
setlocal
title Push Campus Finder AI to GitHub
echo ==========================================================
echo   CAMPUS FINDER AI - Connect to GitHub Repository
echo   TKR College of Engineering & Technology
echo ==========================================================
echo.

set GIT_EXE="C:\Users\Admin\AppData\Local\github-copilot-git-2.53.0-4\cmd\git.exe"

echo Step 1: Please create an empty repository on GitHub (https://github.com/new)
echo Step 2: Copy your repository URL (e.g., https://github.com/your-username/campus-finder-ai.git)
echo.
set /p REPO_URL="Paste your GitHub Repository URL here: "

if "%REPO_URL%"=="" (
    echo.
    echo Error: No URL provided. Please run again and paste your GitHub repository URL.
    pause
    exit /b
)

echo.
echo Connecting to %REPO_URL%...
%GIT_EXE% remote remove origin >nul 2>&1
%GIT_EXE% remote add origin %REPO_URL%
%GIT_EXE% branch -M main

echo.
echo Pushing project to GitHub main branch...
%GIT_EXE% push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ==========================================================
    echo   SUCCESS! Your project has been pushed to GitHub!
    echo ==========================================================
) else (
    echo.
    echo Note: If prompted for GitHub login, please sign in via browser or personal access token.
)

echo.
pause
