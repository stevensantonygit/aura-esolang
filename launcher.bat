@echo off
REM AURA Programming Language Launcher

echo.
echo AURA Programming Language Launcher
echo ==================================
echo.

:menu
echo Choose an option:
echo 1. Run example program
echo 2. Run test suite
echo 3. Start web editor
echo 4. Run custom file
echo 5. Show help
echo 6. Exit
echo.

set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" (
    echo.
    echo Running example program...
    py aura.py demo.aura
    pause
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo Running test suite...
    py aura.py test_suite.aura
    pause
    goto menu
)

if "%choice%"=="3" (
    echo.
    echo Starting web editor...
    echo Open http://localhost:5000 in your browser
    py aura_web.py
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    set /p filename="Enter filename (.aura): "
    if exist "%filename%" (
        echo Running %filename%...
        py aura.py "%filename%"
    ) else (
        echo File not found: %filename%
    )
    pause
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo AURA Help:
    echo - Create .aura files with your code
    echo - Use py aura.py filename.aura to run
    echo - Start web editor with py aura_web.py
    echo - Check README.md for full documentation
    echo.
    pause
    goto menu
)

if "%choice%"=="6" (
    echo.
    echo Thanks for using AURA! No cap!
    exit
)

echo Invalid choice. Please try again.
goto menu