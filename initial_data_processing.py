import pandas as pd
from sklearn.impute import SimpleImputer
from datetime import datetime

# Get the current date to append to the log files
current_date = datetime.now().strftime("%m-%d-%y")

# Step 1: Optimally read CSV files
def read_csv_optimally(file_path, dtypes=None):
    """Reads a CSV file and returns a DataFrame."""
    return pd.read_csv(file_path, dtype=dtypes)

# Step 2: Data exploration functions
def get_shape_and_dtypes(df):
    """Prints the shape and data types of the DataFrame."""
    print("Shape:", df.shape)
    print("Data types:\n", df.dtypes)

def get_unique_values(df):
    """Prints the number of unique values for each column."""
    for col in df.columns:
        print(f"{col} unique values: {df[col].nunique()}")

def get_missing_values(df):
    """Prints the number of missing values for each column."""
    missing_values = df.isnull().sum()
    print("Missing values:\n", missing_values)

# Step 3: Data preprocessing
def preprocess_data(df, impute_strategy=None):
    """Preprocesses the DataFrame based on the specified impute strategy."""
    df.drop_duplicates(inplace=True)
    if impute_strategy:
        imputer = SimpleImputer(strategy=impute_strategy)
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
        return df_imputed
    else:
        return df

# Step 4: Logging issues
def log_issues(df, columns_for_duplicates=None):
    """Logs missing values and duplicates to CSV files."""
    missing_values_df = df[df.isnull().any(axis=1)]
    missing_values_df.to_csv(f'/path/to/missing_values_log_{current_date}.csv', index=False)
    
    if columns_for_duplicates:
        grouped = df.groupby(columns_for_duplicates)
        duplicates_df = grouped.filter(lambda x: len(x) > 1)
    else:
        duplicates_df = df[df.duplicated()]

    duplicates_df.to_csv(f'/path/to/duplicate_values_log_{current_date}.csv', index=False)

# Step 5: Generate descriptive statistics
def generate_descriptive_stats(df):
    """Generates descriptive statistics and saves them to a CSV file."""
    desc_stats = df.describe(include='all')
    desc_stats.to_csv(f'/path/to/descriptive_stats_{current_date}.csv')

if __name__ == "__main__":
    file_path = '/path/to/your/csv/file.csv'  # Replace with your actual file path
    dtypes = None
    impute_strategy = None  # Default is None, meaning no imputation will be performed
    
    # Read and explore data
    df = read_csv_optimally(file_path, dtypes)
    get_shape_and_dtypes(df)
    get_unique_values(df)
    get_missing_values(df)

    # Log issues and generate stats
    log_issues(df, columns_for_duplicates=['Date', 'About', 'DOT'])
    generate_descriptive_stats(df)

    # Preprocess data
    df_clean = preprocess_data(df, impute_strategy)
    print("Data preprocessing completed.")
