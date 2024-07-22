import pandas as pd

def preprocess_data(input_file, output_file):
    # Load data
    df = pd.read_csv(input_file)
    
    # Data cleaning
    df = df.dropna()  # Drop missing values
    
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Save preprocessed data
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data('data/payments.csv', 'data/payments_preprocessed.csv')
