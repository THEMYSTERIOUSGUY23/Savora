@echo off
title Savora Kitchen AI - Standalone PyInstaller Freezer
echo ============================================================
echo   SAVORA KITCHEN AI - STANDALONE EXE COMPILER (GPU READY)
echo ============================================================
echo.
echo [1/3] Installing / Verifying required packages...
pip install customtkinter xgboost scikit-learn pandas openpyxl pyinstaller
echo.
echo [2/3] Freezing Python + CUDA XGBoost + Dataset into single EXE...
pyinstaller --noconfirm --onefile --windowed --name Savora_Kitchen_AI_Standalone --add-data "Food_Waste_Prediction_Dataset.xlsx;." --collect-all customtkinter --collect-all xgboost savora_app.py
echo.
echo [3/3] Copying standalone executable to current folder...
if exist "dist\Savora_Kitchen_AI_Standalone.exe" (
    copy /Y "dist\Savora_Kitchen_AI_Standalone.exe" ".\Savora_Kitchen_AI_Standalone.exe" >nul
    echo SUCCESS! Created Savora_Kitchen_AI_Standalone.exe
) else (
    echo Build finished. Check the dist folder for output.
)
pause
