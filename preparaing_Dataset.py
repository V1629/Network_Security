import pandas as pd
import os

def remove_last_column_and_save(input_csv, output_folder, output_name):
    # Step 1: Read dataset
    df = pd.read_csv(input_csv)

    # Step 2: Remove last column
    df_updated = df.iloc[:, :-1]   # keep all rows, all columns except last one

    # Step 3: Create folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Step 4: Save updated CSV
    output_path = os.path.join(output_folder, output_name)
    df_updated.to_csv(output_path, index=False)

    print(f"Updated dataset saved to: {output_path}")


# Example usage:
remove_last_column_and_save(
    input_csv="valid_path/test.csv",
    output_folder="valid_path",
    output_name="valid_test_dataset.csv"
)
