# Load and inspect the dataset structure
df_inspect = pd.read_csv('/content/food_wastage_data.csv')
print("Columns:", df_inspect.columns.tolist())
display(df_inspect.head(3))

mport pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from xgboost import XGBRegressor

# 1. Load the actual dataset
df_history = pd.read_csv('/content/food_wastage_data.csv')

# 2. Preprocess and define features
# Since the dataset does not have a separate 'day_of_week' column, we will use 'Seasonality' and 'Event Type'
# as environmental conditions, and add a custom Day input to train our model.
categorical_features = ['Type of Food', 'Event Type', 'Storage Conditions', 'Seasonality', 'Preparation Method', 'Geographical Location']
numerical_features = ['Number of Guests']

encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
df_encoded = df_history.copy()
df_encoded[categorical_features] = encoder.fit_transform(df_history[categorical_features].astype(str))

X = df_encoded[categorical_features + numerical_features]
y_qty = df_encoded['Quantity of Food']
y_waste = df_encoded['Wastage Food Amount']

# 3. Train the machine learning models
qty_model = XGBRegressor(n_estimators=100, max_depth=4, learning_rate=0.1)
waste_model = XGBRegressor(n_estimators=100, max_depth=4, learning_rate=0.1)

qty_model.fit(X, y_qty)
waste_model.fit(X, y_waste)
print("Model trained successfully on your dataset!")

# @title 🔮 Enter Upcoming Event Conditions
# @markdown Change these inputs to predict new event requirements based on the historical training data.

Type_of_Food = "Vegetables" # @param ["Meat", "Vegetables", "Dairy", "Bakery"] {type:"string"}
Number_of_Guests = 500 # @param {type:"integer"}
Event_Type = "Wedding" # @param ["Corporate", "Birthday", "Wedding", "Social Share"] {type:"string"}
Storage_Conditions = "Room Temperature" # @param ["Refrigerated", "Room Temperature"] {type:"string"}
Seasonality = "Summer" # @param ["Summer", "Winter", "All Seasons"] {type:"string"}
Preparation_Method = "Buffet" # @param ["Buffet", "Fingering", "Sit-down"] {type:"string"}
Geographical_Location = "Urban" # @param ["Urban", "Rural", "Suburbs"] {type:"string"}

# Create input dataframe
input_dict = {
    'Type of Food': Type_of_Food,
    'Number of Guests': Number_of_Guests,
    'Event Type': Event_Type,
    'Storage Conditions': Storage_Conditions,
    'Seasonality': Seasonality,
    'Preparation Method': Preparation_Method,
    'Geographical Location': Geographical_Location
}

input_df = pd.DataFrame([input_dict])
input_df[categorical_features] = encoder.transform(input_df[categorical_features].astype(str))

# Make predictions
pred_qty = max(0, float(qty_model.predict(input_df[categorical_features + numerical_features])[0]))
pred_waste = max(0, float(waste_model.predict(input_df[categorical_features + numerical_features])[0]))

# Display predictions
print("============================================")
print("       PREDICTED EVENT REQUIREMENTS         ")
print("============================================")
print(f"Target Event conditions: {Type_of_Food} for {Number_of_Guests} guests during a {Event_Type} event.")
print(f"\n• Predicted Total Quantity of Food Required: {round(pred_qty, 1)} kg")
print(f"• Anticipated Food Wastage Amount: {round(pred_waste, 1)} kg")
print("============================================")