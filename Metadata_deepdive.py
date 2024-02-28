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
#OUTPUT
_____________________________________________
This is the spread of prevalence for Males:
diagnostic
BCC    439
ACK    130
SCC    102
NEV     26
MEL     24
SEK     20
Name: count, dtype: int64
_____________________________________________
This is the spread of prevalence for Females:
diagnostic
BCC    406
ACK    153
SCC     90
NEV     49
MEL     28
SEK     27
Name: count, dtype: int64
_____________________________________________
This is the spread of prevalence for both genders:
diagnostic
BCC    845
ACK    283
SCC    192
NEV     75
MEL     52
SEK     47
Name: count, dtype: int64
_____________________________________________
We clean the data for missing values, as around 804 values are missing in half the columns
patient_id               0
lesion_id                0
smoke                  804
drink                  804
background_father      818
background_mother      822
age                      0
pesticide              804
gender                 804
skin_cancer_history    804
cancer_history         804
has_piped_water        804
has_sewage_system      804
fitspatrick            804
region                   0
diameter_1             804
diameter_2             804
diagnostic               0
itch                     0
grew                     0
hurt                     0
changed                  0
bleed                    0
elevation                0
img_id                   0
biopsed                  0
