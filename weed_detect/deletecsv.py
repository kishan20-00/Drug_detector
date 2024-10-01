import pandas as pd

# Load the CSV file
csv_file = 'labels.csv'  # Path to your CSV file
df = pd.read_csv(csv_file)

# Filter out rows where 'Weed_Variety' is 'negative'
df_filtered = df[df['Species'] != 'Negative']

# Save the cleaned dataset to a new CSV file (or overwrite the original file)
cleaned_csv_file = 'labels.csv'  # Path to save the cleaned CSV
df_filtered.to_csv(cleaned_csv_file, index=False)

print(f"Records with 'negative' weed variety removed. Cleaned CSV saved to: {cleaned_csv_file}")
