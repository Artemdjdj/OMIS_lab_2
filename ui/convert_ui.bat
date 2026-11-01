@echo off
setlocal EnableExtensions
chcp 65001 >nul
title PySide 6 — конвертация .ui в .py


set "UI_DIR=%~dp0"
set "OUT_DIR=%~dp0"
set "MODE=folder"

rem
if "%~1"=="" goto :args_done
if exist "%~1\*" (
    set "UI_DIR=%~f1"
    set "OUT_DIR=%~f1"
    goto :args_done
)
if /i "%~x1"==".ui" if exist "%~1" (
    set "UI_DIR=%~f1"
    set "OUT_DIR=%~dp1"
    set "MODE=file"
    goto :args_done
)
echo.
echo   [ОШИБКА] Папка или .ui файл не найдены: "%~1"
echo.
pause
exit /b 1

:args_done
if not "%~2"=="" set "OUT_DIR=%~f2"
if "%UI_DIR:~-1%"=="\" set "UI_DIR=%UI_DIR:~0,-1%"
if "%OUT_DIR:~-1%"=="\" set "OUT_DIR=%OUT_DIR:~0,-1%"

echo ============================================================
echo    PySide 6:  Qt Designer .ui   ==^>   .py
echo ============================================================
echo.
echo   Конвертируем : %UI_DIR%
echo   Вывод .py    : %OUT_DIR%
echo.

if not exist "%UI_DIR%" (
    echo   [ОШИБКА] Путь не найден: "%UI_DIR%"
    echo.
    pause
    exit /b 1
)

rem
set "PYCMD="
where py >nul 2>&1 && set "PYCMD=py -3"
if not defined PYCMD (
    where python >nul 2>&1 && set "PYCMD=python"
)
if not defined PYCMD (
    echo   [ОШИБКА] Python не найден.
    echo            Установите Python с python.org
    echo            и отметьте галочку "Add Python to PATH".
    echo.
    pause
    exit /b 1
)

call :find_uic

if defined UIC goto :uic_found

echo   [!] PySide6 не найден в системе.
echo       Он необходим для конвертации .ui файлов.
echo.
set "ANS=y"
set /p "ANS=   Установить PySide6 сейчас? [Y/n]: "
if /i "%ANS%"=="n" goto :uic_missing
if /i "%ANS%"=="no" goto :uic_missing

echo.
echo   Установка PySide6, это может занять несколько минут ...
%PYCMD% -m pip install PySide6
if errorlevel 1 goto :uic_missing

call :find_uic
if defined UIC goto :uic_found

:uic_missing
echo.
echo   [ОШИБКА] Не удалось найти pyside6-uic.
echo            Установите PySide6 вручную:
echo                pip install PySide6
echo            и запустите скрипт снова.
echo.
pause
exit /b 1

:uic_found
echo   Утилита конвертации: %UIC%
echo.

if not exist "%OUT_DIR%" mkdir "%OUT_DIR%"

set "PATTERN=%UI_DIR%\*.ui"
if "%MODE%"=="file" set "PATTERN=%UI_DIR%"

set /a OK=0
set /a FAIL=0
set /a COUNT=0

echo   Начинаю конвертацию ...
echo.

for %%F in ("%PATTERN%") do (
    set /a COUNT+=1
    "%UIC%" "%%~fF" -o "%OUT_DIR%\ui_%%~nF.py"
    if errorlevel 1 (
        echo   [ОШИБКА] %%~nxF
        set /a FAIL+=1
    ) else (
        echo   [OK]     %%~nxF   ==^>   ui_%%~nF.py
        set /a OK+=1
    )
)

echo.
if %COUNT%==0 (
    echo   [!] .ui файлы не найдены в "%UI_DIR%"
    echo.
    pause
    exit /b 1
)

echo   Готово!  Успешно: %OK%    С ошибками: %FAIL%
echo   .py файлы сохранены в: %OUT_DIR%
echo.
echo   Подключение в коде, например для mainwindow.ui:
echo       from ui_mainwindow import Ui_MainWindow
echo.
pause
exit /b 0

:find_uic
set "UIC="
where pyside6-uic >nul 2>&1 && set "UIC=pyside6-uic"
if defined UIC goto :eof
for /f "usebackq delims=" %%P in (`%PYCMD% -c "import os,sys,PySide6;c=[os.path.join(os.path.dirname(PySide6.__file__),'uic.exe'),os.path.join(os.path.dirname(sys.executable),'Scripts','pyside6-uic.exe')];print(next((p for p in c if os.path.exists(p)),''))" 2^>nul`) do (
    if exist "%%P" set "UIC=%%P"
)
goto :eof
