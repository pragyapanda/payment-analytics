import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(input_file):
    # Load preprocessed data
    df = pd.read_csv(input_file)
    
    # Analysis: Number of transactions per platform
    platform_counts = df['platform'].value_counts()
    
    # Analysis: Total amount per currency
    amount_per_currency = df.groupby('currency')['amount'].sum()
    
    # Analysis: Status distribution
    status_counts = df['status'].value_counts()
    
    # Plotting
    sns.set(style="whitegrid")
    
    # Plot number of transactions per platform
    plt.figure(figsize=(10, 6))
    sns.barplot(x=platform_counts.index, y=platform_counts.values, palette="viridis")
    plt.title('Number of Transactions per Platform')
    plt.xlabel('Platform')
    plt.ylabel('Number of Transactions')
    plt.show()
    
    # Plot total amount per currency
    plt.figure(figsize=(10, 6))
    sns.barplot(x=amount_per_currency.index, y=amount_per_currency.values, palette="viridis")
    plt.title('Total Amount per Currency')
    plt.xlabel('Currency')
    plt.ylabel('Total Amount')
    plt.show()
    
    # Plot status distribution
    plt.figure(figsize=(10, 6))
    sns.barplot(x=status_counts.index, y=status_counts.values, palette="viridis")
    plt.title('Status Distribution of Transactions')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    analyze_data('data/payments_preprocessed.csv')
