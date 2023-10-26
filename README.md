## Description

This Python script provides a modular approach to read, preprocess, and explore CSV data files. It is particularly useful for data engineers and analysts who are looking to automate and standardize their data preparation steps.

## Features

- Optimally reads CSV files
- Data exploration functions to understand shape, data types, unique values, etc.
- Logs missing and duplicate values
- Optional data imputation

## Requirements

- Python 3.x
- Pandas
- scikit-learn

## Usage

1. Update the `file_path` variable with the path to your CSV file.
2. Optionally, specify data types and impute strategies.
3. Run the script.

## Configuration

- `file_path`: The path to the input CSV file.
- `dtypes`: Dictionary specifying column data types (optional).
- `impute_strategy`: Strategy for data imputation (optional).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
