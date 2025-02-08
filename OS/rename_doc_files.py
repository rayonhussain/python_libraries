import shutil
import os

# Define the input file name (ensure this file exists in the same directory)
input_file = "your_file.docx"  # Change this to the actual file name

# List of biweekly date ranges for file naming
date_ranges = [
    "04-04-2024_04-19-2024",
    "04-22-2024_05-03-2024",
    "05-06-2024_05-17-2024",
    "05-20-2024_05-31-2024",
    "06-03-2024_06-14-2024",
    "06-17-2024_06-28-2024",
    "07-01-2024_07-12-2024",
    "07-15-2024_07-26-2024",
    "07-29-2024_08-09-2024",
    "08-12-2024_08-23-2024",
    "08-26-2024_09-06-2024",
    "09-09-2024_09-20-2024",
    "09-23-2024_10-04-2024",
    "10-07-2024_10-18-2024",
    "10-21-2024_11-01-2024",
    "11-04-2024_11-11-2024"
]

# Check if input file exists
if not os.path.exists(input_file):
    print(f"Error: '{input_file}' not found.")
else:
    for date_range in date_ranges:
        # Create new filename with date appended
        new_filename = f"{os.path.splitext(input_file)[0]}_{date_range}.docx"
        # Copy original file to new file
        shutil.copy(input_file, new_filename)
        print(f"Created: {new_filename}")

print("File duplication completed successfully!")
