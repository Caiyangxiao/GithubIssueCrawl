import pandas as pd

def generate_and_sort_numbers():
    random_numbers = random.sample(range(1, 15000), 99)
    sorted_numbers = sorted(random_numbers)

    return sorted_numbers

def extract_and_save_data(input_file, output_file, selected_rows):
    df = pd.read_excel(input_file)

    selected_rows = [idx for idx in selected_rows if idx < len(df)]
    selected_data = df.iloc[selected_rows]

    selected_data.to_excel(output_file, index=False, engine='openpyxl')

if __name__ == "__main__":
    import random

    sorted_numbers = generate_and_sort_numbers()

    input_file = 'input_file_path'
    output_file = 'output_file_path'

    extract_and_save_data(input_file, output_file, sorted_numbers)
