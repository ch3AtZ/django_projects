import matplotlib.pyplot as plt
import pandas as pd
def display_chart(data, chart_type):
    if chart_type == '1':
        # Bar graph
        x = input("Enter the column name for X-axis: ")
        y = input("Enter the column name for Y-axis: ")
        plt.figure(figsize=(12, 6))  # Increase the figure size
        plt.bar(data[x], data[y], color='blue')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title('Bar Graph')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.show()
    elif chart_type == '2':
        # Line chart
        x = input("Enter the column name for X-axis: ")
        y = input("Enter the column name for Y-axis: ")
        plt.figure(figsize=(12, 6))  # Increase the figure size
        plt.plot(data[x], data[y], marker='o', color='red')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title('Line Chart')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.show()
    elif chart_type == '3':
        # Histogram
        column = input("Enter the column name for the histogram: ")
        bins = int(input("Enter the number of bins: "))
        plt.figure(figsize=(12, 6))  # Increase the figure size
        plt.hist(data[column], bins=bins, color='green', edgecolor='black')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.show()
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    # Load the dataset
    file_path = '/Users/dhruvbharara/Downloads/IP PROJECT.csv'
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        print("Columns available: ", list(data.columns))

        print("\nChoose the type of chart to display:")
        print("1. Bar Graph")
        print("2. Line Chart")
        print("3. Histogram")
        choice = input("Enter your choice (1/2/3): ")

        display_chart(data, choice)
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
