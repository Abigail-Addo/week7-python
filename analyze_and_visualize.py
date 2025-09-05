import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("📊 Welcome to Data Analysis with Pandas & Visualization with Matplotlib\n")

    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
        'Age': [25, 30, 35, 40, 28, 33],
        'Salary': [50000, 60000, 70000, 80000, 55000, 65000],
        'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance']
    }

    df = pd.DataFrame(data)
    print("✅ Data Loaded:\n", df, "\n")

    print("🔍 Data Info:")
    print(df.info(), "\n")
    
    print("🔢 Statistical Summary:")
    print(df.describe(), "\n")

    print("💡 Check for missing values:")
    print(df.isnull().sum(), "\n")

    avg_salary = df.groupby('Department')['Salary'].mean()
    print("💰 Average Salary by Department:\n", avg_salary, "\n")

    plt.figure(figsize=(8,5))
    avg_salary.plot(kind='bar', color='skyblue')
    plt.title('Average Salary by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Salary ($)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=(8,5))
    df['Age'].plot(kind='hist', bins=5, color='salmon', edgecolor='black')
    plt.title('Distribution of Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
