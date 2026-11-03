@echo off
title Savora Smart Kitchen Planner v3 - RTX 5050 Standalone EXE Builder
echo ====================================================================
echo   SAVORA SMART KITCHEN PLANNER v3 - RTX 5050 STANDALONE BUILDER
echo ====================================================================
echo.
echo [1/3] Verifying UI and GPU packages (CustomTkinter + CUDA XGBoost)...
pip install customtkinter xgboost scikit-learn pandas openpyxl pyinstaller
echo.
echo [2/3] Freezing into a single standalone Windows executable...
pyinstaller --noconfirm --onefile --windowed --name Savora_Smart_Kitchen_RTX5050 --add-data "Food_Waste_Prediction_Dataset.xlsx;." --collect-all customtkinter --collect-all xgboost savora_app.py
echo.
echo [3/3] Copying standalone executable to current folder...
if exist "dist\Savora_Smart_Kitchen_RTX5050.exe" (
    copy /Y "dist\Savora_Smart_Kitchen_RTX5050.exe" ".\Savora_Smart_Kitchen_RTX5050.exe" >nul
    echo SUCCESS! Created Savora_Smart_Kitchen_RTX5050.exe
) else (
    echo Build finished. Check the dist folder for output.
)
pause
