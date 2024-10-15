import pandas as pd

# Load your data
df = pd.read_csv('datasets/aus_extreme_temp.csv')

# Convert the 'Date' column from 'DD/MM/YYYY' to 'YYYY-MM-DD'
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

# Save the modified CSV
df.to_csv('datasets/aus_extreme_temp_fixed.csv', index=False)
