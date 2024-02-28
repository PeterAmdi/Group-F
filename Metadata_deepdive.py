import pandas as pd

# Specify the file path
file_path = 'metadata.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Select specific columns
selected_columns = ['gender', 'skin_cancer_history', 'cancer_history', 'region', 'diagnostic', 'img_id']

# Create a new DataFrame with only the selected columns
new_df = df[selected_columns]

# Filter rows where "gender" is "MALE"
filtered_df_MALE = new_df[new_df["gender"] == "MALE"]

# Filter rows where "gender" is "FEMALE"
filtered_df_FEMALE = new_df[new_df["gender"] == "FEMALE"]

# Filter rows where "gender" is either "MALE" or "FEMALE"
filtered_df = new_df[new_df["gender"].isin(['MALE', 'FEMALE'])]

# Count the occurrences of each diagnostic for Males
filtered_df_MALE_diagnostic = filtered_df_MALE["diagnostic"].value_counts()

# Count the occurrences of each diagnostic for Females
filtered_df_FEMALE_diagnostic = filtered_df_FEMALE["diagnostic"].value_counts()

# Count the occurrences of each diagnostic for both genders
filtered_df_diagnostic = filtered_df["diagnostic"].value_counts()

# Print the results
print("_____________________________________________")
print("This is the spread of prevalence for Males:")
print(filtered_df_MALE_diagnostic)
print("_____________________________________________")
print("This is the spread of prevalence for Females:")
print(filtered_df_FEMALE_diagnostic)
print("_____________________________________________")
print("This is the spread of prevalence for both genders:")
print(filtered_df_diagnostic)
print("_____________________________________________")
print("We clean the data for missing values, as around 804 values are missing in half the columns")
nan_count2 = df.isna().sum()
print(nan_count2)