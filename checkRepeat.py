import pandas as pd

def check_duplicates(file_path):
    df = pd.read_excel(file_path)
    duplicates = df[df.duplicated()]

    if duplicates.empty:
        print("There are no duplicates in the table.")
    else:
        print("There are duplicate items in the table. The specific duplicate rows are as follows:")
        print(duplicates)

if __name__ == "__main__":
    excel_file_path = 'your_file_path'

    check_duplicates(excel_file_path)
