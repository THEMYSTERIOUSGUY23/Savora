 # Savora — Smart Kitchen & Crowd Planner

Savora is an offline, GPU-accelerated desktop application that forecasts restaurant customer footfall, optimal dish preparation quantities, and unavoidable kitchen waste using gradient-boosted decision trees (XGBoost). Built with a high-contrast dark UI in CustomTkinter, it translates machine learning predictions into actionable split-batch cooking plans for kitchen staff and restaurant managers.

## Key Features

* **Two-Stage Cascaded AI Pipeline:**
  * **Stage 1 (Crowd Forecaster):** Predicts expected customer footfall from restaurant branch, city, cuisine, dish item, weather, weekend/holiday status, outdoor temperature, and promotional discount percentage.
  * **Stage 2 (Prep & Waste Forecaster):** Combines the predicted customer count with environmental conditions to forecast exact preparation targets (in portions) and anticipated food waste (in kilograms).
* **NVIDIA CUDA GPU Acceleration:** Configured with XGBoost histogram tree building (`tree_method="hist"`, `device="cuda:0"`) to run training and real-time inference on local NVIDIA RTX GPUs, with automatic fallback to CPU execution.
* **Smart Split-Batch Cooking Plan:** Automatically divides the recommended preparation quantity into an upfront pre-service batch (80%) and an on-demand buffer batch (20%) to minimize leftover food waste.
* **Consumer-Friendly Visual Dashboard:** Features color-coded waste risk indicators, interactive scenario presets, progress meters, and plain-English kitchen guidance.
* **Self-Healing Offline Dataset:** Reads historical records from Food_Waste_Prediction_Dataset.xlsx and includes an embedded backup payload so the executable runs even if the external spreadsheet is moved.

## Dataset Structure

The model trains on 1,000 historical kitchen service records stored in Food_Waste_Prediction_Dataset.xlsx:

* **Categorical Features:** Restaurant_Name, City, Cuisine, Food_Item, Weather, Weekend, Holiday
* **Numerical Features:** Temperature_C, Discount_Percent
* **Predicted Targets:** Customers, Prepared_Quantity, Waste_Amount_kg

## Project Structure

* `Savora_Kitchen_AI.exe` — Windowed 64-bit Windows desktop application launcher.
* `Savora_Kitchen_AI_Console.exe` — Console-enabled 64-bit Windows launcher for viewing startup logs and diagnostics.
* `savora_app.py` — Complete Python source code with CustomTkinter UI, Tkinter fallback UI, and two-stage GPU XGBoost engine.
* `Food_Waste_Prediction_Dataset.xlsx` — Historical restaurant sales, footfall, and food waste dataset.
* `Build_Standalone_Frozen_EXE.bat` — One-click PyInstaller build script to bundle the Python environment and CUDA libraries into a single standalone executable.

## Quick Start

### Option 1: Run the Windows Executable
1. Extract the release archive to any local folder.
2. Double-click `Savora_Kitchen_AI.exe` to launch the application.

### Option 2: Run from Python Source
1. Activate your local Python or Conda environment:
   ```bash
   conda activate AI_env
