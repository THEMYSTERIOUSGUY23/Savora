========================================================================
SAVORA KITCHEN INTELLIGENCE - OFFLINE GPU DESKTOP APP PACKAGE
========================================================================

INCLUDED FILES IN THIS ZIP ARCHIVE:
1. Savora_Kitchen_AI.exe
   - Native 64-bit Windows GUI Executable Launcher (Windowed Mode).
   - Double-click to launch the dark-themed app directly using your
     installed Windows Python environment (with embedded dataset backup).
   - Automatically uses CustomTkinter if installed, or falls back to a
     zero-dependency Dark Tkinter UI out of the box.

2. Savora_Kitchen_AI_Console.exe
   - 64-bit Windows Console Executable Launcher (shows terminal logs and
     model validation metrics on startup).

3. Food_Waste_Prediction_Dataset.xlsx
   - Your 1,000-row historical kitchen dataset. You can edit or append
     new rows to this Excel file and restart the app to retrain on the fly.

4. savora_app.py
   - Full Python source script with NVIDIA CUDA GPU acceleration
     (XGBRegressor tree_method="hist", device="cuda") and 80/20 holdout
     validation metrics.

5. Build_Standalone_Frozen_EXE.bat
   - Optional one-click compiler script if you want PyInstaller to bundle
     your entire Conda/Python DLL tree into a 200+ MB standalone binary
     for PCs without Python installed.
========================================================================
