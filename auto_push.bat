@echo off
title Auto Push Campus Finder AI to GitHub
echo ==========================================================
echo   Creating GitHub Repository & Pushing All Code...
echo ==========================================================
echo.
"C:\Program Files\GitHub CLI\gh.exe" repo create campus-finder-ai --public --source=. --push
echo.
pause
