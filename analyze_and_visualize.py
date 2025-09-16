import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("📊 Welcome to Iris Dataset Analysis with Pandas & Matplotlib\n")

    # Load the dataset
    try:
        column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
        df = pd.read_csv("iris.data", header=None, names=column_names)
        print("Dataset Loaded Successfully!\n")
    except FileNotFoundError:
        print("File not found. Please make sure 'iris.data' is in the same directory.")
        return

    # Preview data
    print("🔍 First 5 Rows:\n", df.head(), "\n")

    # Dataset info
    print("📋 Data Info:")
    print(df.info(), "\n")

    # Check missing values
    print("💡 Missing Values:\n", df.isnull().sum(), "\n")

    # Statistical summary
    print("🔢 Statistical Summary:\n", df.describe(), "\n")

    # Grouping: average petal length per species
    avg_petal = df.groupby("species")["petal_length"].mean()
    print("🌸 Average Petal Length per Species:\n", avg_petal, "\n")

    # ---------- Visualizations ----------
    # 1. Line chart (Petal length trend across dataset index)
    plt.figure(figsize=(8,5))
    plt.plot(df.index, df["petal_length"], label="Petal Length", color="green")
    plt.title("Petal Length Trend")
    plt.xlabel("Index")
    plt.ylabel("Petal Length (cm)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 2. Bar chart (Average petal length per species)
    plt.figure(figsize=(8,5))
    avg_petal.plot(kind="bar", color="skyblue")
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length (cm)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    # 3. Histogram (Sepal width distribution)
    plt.figure(figsize=(8,5))
    df["sepal_width"].plot(kind="hist", bins=10, color="salmon", edgecolor="black")
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4. Scatter plot (Sepal length vs Petal length)
    plt.figure(figsize=(8,5))
    plt.scatter(df["sepal_length"], df["petal_length"], alpha=0.7, c="purple")
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
