# Find the index of rows where there are missing values in 'PurchaseAmountUSD' or 'Location' columns
missing_indices = df_Copy.index[df_Copy['PurchaseAmountUSD'].isnull() | df_Copy['Location'].isnull()]

# Create a list to store the indices of the rows to be displayed
rows_to_display = []
# Loop through the missing indices and add the ten cells above and below each missing index
for index in missing_indices:
    rows_to_display.extend(range(max(0, index - 10), min(len(df_Copy), index + 11)))

# Select only the 'PurchaseAmountUSD' and 'Location' columns for the selected rows
selected_data = df_Copy[['PurchaseAmountUSD', 'Location']].iloc[rows_to_display]
print(selected_data)                