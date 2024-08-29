import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Load the data from the CSV file
file_path = 'F:\Documents\Hackathon\My own\Queue Based Management System\Data Collection and Prediction of Peak Times\data.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Convert 'timestamp' to datetime and extract the hour
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour

# Train a simple linear regression model to predict customers based on time of day
X = df[['hour']]
y = df['customers']
model = LinearRegression().fit(X, y)

# Input time from the user
time_input = input("Enter the time in HH:MM format (e.g., 12:00): ")
input_hour = datetime.strptime(time_input, '%H:%M').hour0

# Predict number of customers for the given hour
predicted_customers = model.predict([[input_hour]])
print(f"Predicted number of customers at {time_input}: {int(predicted_customers[0])}")
