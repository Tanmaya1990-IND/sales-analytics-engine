@echo off
REM Sales Analytics Engine - Test Runner
REM This script runs the pytest test suite

echo.
echo ========================================
echo Running Unit Tests
echo ========================================
echo.

REM Run pytest
C:\Users\misra\AppData\Local\Python\bin\python.exe -m pytest tests/ -v

echo.
echo ========================================
echo Press any key to exit...
echo ========================================
pause
