import pandas as pd
import matplotlib.pyplot as plt


# Creating a simple dataset
data = {
    'Table_ID': [1, 2, 3, 1, 2, 3, 1, 2, 4, 4, 5, 5],
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'Check_In_Time': ['12:00', '12:15', '12:30', '13:30', '14:00', '14:15', '15:30', '16:00', '12:00', '14:00', '18:00', '20:00'],
    'Check_Out_Time': ['13:00', '13:45', '13:15', '15:00', '15:30', '15:00', '16:45', '17:30', '13:30', '15:15', '19:30', '21:15']
}

df = pd.DataFrame(data)
df.to_csv('restaurant_data.csv', index=False)
print("Dataset created successfully!")




# --- Task 1: Load the dataset ---
df = pd.read_csv('restaurant_data.csv')

# --- Task 2: Calculate dining duration ---
# We convert the time strings to "datetime" objects so Python can do math with them
df['Check_In_Time'] = pd.to_datetime(df['Check_In_Time'])
df['Check_Out_Time'] = pd.to_datetime(df['Check_Out_Time'])

# Calculate duration in minutes
df['Duration_Minutes'] = (df['Check_Out_Time'] - df['Check_In_Time']).dt.total_seconds() / 60

# --- Task 3: Find average dining time ---
avg_time = df['Duration_Minutes'].mean()

print()
print("-" * 30)
print(f"RESTAURANT ANALYSIS REPORT")
print("-" * 30)
print(f"Total Customers: {len(df)}")
print(f"Average Dining Time: {avg_time:.2f} minutes")
print("-" * 30)

# --- Task 4: Count how many times each table is used ---
table_counts = df['Table_ID'].value_counts().sort_index()
print("\nTable Usage Counts:")
print(table_counts)

# --- Task 5: Simple Visualizations ---

# Histogram for Dining Duration
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1) # 1 row, 2 columns, index 1
plt.hist(df['Duration_Minutes'], bins=5, color='blue', edgecolor='black')
plt.title('Distribution of Dining Times')
plt.xlabel('Minutes')
plt.ylabel('Number of Customers')

# Bar Chart for Table Usage
plt.subplot(1, 2, 2) # index 2
table_counts.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Usage Frequency per Table')
plt.xlabel('Table ID')
plt.ylabel('Times Used')

plt.tight_layout()
plt.show()