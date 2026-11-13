# Exploratory Data Analysis (EDA) – Step by Step

## 📌 About This Project

Exploratory Data Analysis (EDA) is an important part of the Data Analysis and Machine Learning workflow. Before building a Machine Learning model, it is necessary to understand the dataset, identify data quality issues, explore patterns, and discover relationships between different features.

In this project, I have explored **Exploratory Data Analysis using Python** through a Jupyter Notebook.

For practical implementation, I used a Student Performance Dataset containing information such as study hours, attendance, previous scores, and final scores.

The notebook follows a step-by-step approach, starting with basic dataset inspection and gradually moving towards data cleaning, statistical analysis, visualization, correlation analysis, and outlier detection.

The main objective is to understand the data through practical exploration rather than simply applying Python functions.

---

## 📚 Topics Covered

The `Exploratory_Data_Analysis_EDA.ipynb` notebook covers the following concepts:

**01. Importing Libraries**

Started by importing the required Python libraries, including Pandas, NumPy, Matplotlib, and Seaborn. These libraries are used for data manipulation, numerical operations, statistical analysis, and visualization.

**02. Loading the Dataset**

Loaded the Student Performance Dataset from a CSV file using Pandas. Used Python's `Path` module to manage file paths and created an output directory to store the generated visualizations.

**03. Understanding the Dataset**

Explored the dataset using different Pandas functions.

- `head()` – Displays the first five records.
- `shape` – Returns the total number of rows and columns.
- `columns` – Displays all column names.
- `info()` – Provides information about data types and non-null values.
- `describe()` – Generates statistical summaries of numerical columns.

**04. Missing Value Analysis**

Checked missing values using `isnull().sum()` and calculated the percentage of missing data in each column.

Practiced handling missing numerical values by replacing them with the median using `fillna()`. This helps maintain the available records while addressing missing numerical entries.

**05. Duplicate Analysis**

Checked duplicate records using `duplicated()` and removed repeated rows using `drop_duplicates()`. This step helps avoid repeated observations affecting the analysis.

**06. Distribution Analysis**

Used histograms to understand how student final scores are distributed. Explored the frequency of different score ranges and observed how numerical values are spread across the dataset.

**07. Correlation Analysis**

Calculated correlations between numerical features using the `corr()` function.

Explored relationships between study hours, attendance, previous scores, and final scores to understand how these variables move in relation to each other.

**08. Correlation Heatmap**

Created a correlation heatmap using Seaborn to visualize relationships between numerical features. Used annotations and colour variations to make correlation values easier to interpret.

**09. Outlier Detection Using IQR**

Applied the Interquartile Range (IQR) method to identify potential outliers.

Calculated:
- First Quartile (Q1)
- Third Quartile (Q3)
- Interquartile Range (IQR)
- Lower and Upper Bounds

Values outside the calculated boundaries were flagged for further investigation.

**10. Box Plot Visualization**

Created box plots using Seaborn to understand the spread of numerical features and visually identify potential outliers. Explored the median, quartiles, and unusual observations.

**11. Final EDA Summary**

Reviewed the dataset after completing the analysis. Checked the total number of records, columns, remaining missing values, and duplicate records to get an overview of the dataset's condition.

---

## 🛠️ Technologies & Libraries Used

The following tools and libraries were used in this project:

- **Python:** Main programming language used for the analysis.
- **Jupyter Notebook:** Used to write and execute the analysis step by step.
- **Pandas:** Used for loading, cleaning, inspecting, and analyzing the dataset.
- **NumPy:** Used for numerical operations and handling numerical data.
- **Matplotlib:** Used for creating histograms and data visualizations.
- **Seaborn:** Used for statistical visualizations, correlation heatmaps, and box plots.
- **Pathlib:** Used for handling dataset and output file paths.

---

## 📂 Project Structure

```text
Exploratory-Data-Analysis-EDA/
│
├── data/
│   └── student_performance.csv
│
├── outputs/
│   ├── marks_distribution.png
│   ├── correlation_heatmap.png
│   └── outlier_boxplot.png
│
├── Exploratory_Data_Analysis_EDA.ipynb
│
└── README.md
```

**Folder and file description:**

- `data/` – Contains the dataset used for the analysis.
- `student_performance.csv` – Sample dataset containing student performance information.
- `outputs/` – Stores the visualizations generated during the notebook execution.
- `Exploratory_Data_Analysis_EDA.ipynb` – Main Jupyter Notebook containing the complete step-by-step EDA implementation.
- `README.md` – Provides project details, concepts covered, and execution instructions.

---

## 📊 Visualizations

The notebook generates three visualizations to make the analysis easier to understand.

**1. Student Marks Distribution – Histogram**

Displays the distribution of student final scores and helps understand where most scores are concentrated.

**2. Correlation Heatmap**

Shows the correlation between numerical features and helps identify positive and negative relationships between variables.

**3. Outlier Detection – Box Plot**

Visualizes the spread of numerical data and highlights potential outliers using quartiles and the IQR method.

---

## ▶️ How to Run This Project

Follow these steps to run the notebook on your local machine.

**Step 1: Clone the Repository**

```bash
git clone <your-repository-link>
```

**Step 2: Navigate to the Project Directory**

```bash
cd Exploratory-Data-Analysis-EDA
```

**Step 3: Install Required Libraries**

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

**Step 4: Launch Jupyter Notebook**

```bash
jupyter notebook
```

**Step 5: Open the Notebook**

Open `Exploratory_Data_Analysis_EDA.ipynb` and execute the cells one by one.

Make sure the `student_performance.csv` file is available inside the `data` folder before running the notebook.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Understanding dataset structure and statistical summaries.
- Working with CSV datasets using Pandas.
- Identifying and handling missing values.
- Finding and removing duplicate records.
- Exploring numerical data distributions using histograms.
- Understanding relationships between numerical features through correlation analysis.
- Creating correlation heatmaps using Seaborn.
- Identifying potential outliers using the IQR method.
- Visualizing data distributions using box plots.
- Performing step-by-step Exploratory Data Analysis using Jupyter Notebook.

---

## 💡 Key Takeaway

This project helped me understand why EDA is an important step before building Machine Learning models.

I learned that analyzing a dataset is not just about checking values or creating visualizations. It is about understanding the information, identifying possible problems, exploring patterns, and making informed decisions about the data.

One important lesson was that unusual values should not automatically be removed. They need to be investigated to understand whether they are incorrect or represent genuine observations.

---

**Part of my Python & Machine Learning Journey.**