import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# --- CONFIGURATION ---
# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')
# Set visual style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

def create_dummy_dataset(n_rows=1000):
    """
    Generates a synthetic Employee Churn dataset for demonstration.
    """
    np.random.seed(42)
    
    data = {
        'EmployeeID': range(1001, 1001 + n_rows),
        'Age': np.random.normal(35, 8, n_rows).astype(int),
        'Department': np.random.choice(['Sales', 'HR', 'IT', 'Engineering', 'Marketing'], n_rows),
        'Salary': np.random.normal(60000, 15000, n_rows),
        'YearsAtCompany': np.random.randint(1, 20, n_rows),
        'JobSatisfaction': np.random.choice([1, 2, 3, 4, 5], n_rows, p=[0.1, 0.2, 0.4, 0.2, 0.1]),
        'Attrition': np.random.choice(['Yes', 'No'], n_rows, p=[0.2, 0.8])
    }
    
    df = pd.DataFrame(data)
    
    # Intentionally introduce some missing values (Dirty Data)
    df.loc[np.random.choice(df.index, 20), 'Salary'] = np.nan
    df.loc[np.random.choice(df.index, 10), 'Department'] = np.nan
    
    return df

def step_1_data_overview(df):
    """Prints basic information about the dataset."""
    print("\n" + "="*40)
    print("STEP 1: DATA OVERVIEW")
    print("="*40)
    print(f"Shape: {df.shape}")
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nFirst 5 Rows:")
    print(df.head())

def step_2_data_cleaning(df):
    """Handles missing values and duplicates."""
    print("\n" + "="*40)
    print("STEP 2: DATA CLEANING")
    print("="*40)
    
    # 1. Fill missing numerical values with Median
    salary_median = df['Salary'].median()
    df['Salary'].fillna(salary_median, inplace=True)
    print(f"Filled missing 'Salary' with median: {salary_median:.2f}")

    # 2. Fill missing categorical values with Mode
    dept_mode = df['Department'].mode()[0]
    df['Department'].fillna(dept_mode, inplace=True)
    print(f"Filled missing 'Department' with mode: {dept_mode}")

    # 3. Drop Duplicates (if any)
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_rows - df.shape[0]} duplicate rows.")
    
    return df

def step_3_univariate_analysis(df):
    """Analyzes single variables."""
    print("\n" + "="*40)
    print("STEP 3: UNIVARIATE ANALYSIS (Generating Plots...)")
    print("="*40)

    # Plot 1: Distribution of Salary
    plt.figure()
    sns.histplot(df['Salary'], kde=True, color='skyblue')
    plt.title('Distribution of Salary')
    plt.xlabel('Salary (Rs. )')
    plt.show()

    # Plot 2: Count of Attrition (Target Variable)
    plt.figure()
    sns.countplot(x='Attrition', data=df, palette='viridis')
    plt.title('Attrition Count (Yes vs No)')
    plt.show()

def step_4_bivariate_analysis(df):
    """Analyzes relationships between two variables."""
    print("\n" + "="*40)
    print("STEP 4: BIVARIATE ANALYSIS (Generating Plots...)")
    print("="*40)

    # Plot 1: Salary vs Attrition (Boxplot)
    plt.figure()
    sns.boxplot(x='Attrition', y='Salary', data=df, palette='coolwarm')
    plt.title('Salary Distribution by Attrition Status')
    plt.show()

    # Plot 2: Job Satisfaction vs Department
    plt.figure()
    sns.barplot(x='Department', y='JobSatisfaction', data=df, estimator=np.mean, ci=None, palette='mako')
    plt.title('Average Job Satisfaction by Department')
    plt.xticks(rotation=45)
    plt.show()

    # Plot 3: Correlation Heatmap (Numerical columns only)
    plt.figure()
    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

def step_5_generate_report(df):
    """Prints a summary of findings."""
    print("\n" + "="*40)
    print("STEP 5: FINAL INSIGHTS")
    print("="*40)
    
    avg_salary_leavers = df[df['Attrition'] == 'Yes']['Salary'].mean()
    avg_salary_stayers = df[df['Attrition'] == 'No']['Salary'].mean()
    
    print(f"1. Average Salary of Leavers: Rs. {avg_salary_leavers:,.2f}")
    print(f"2. Average Salary of Stayers: Rs. {avg_salary_stayers:,.2f}")
    
    diff = avg_salary_stayers - avg_salary_leavers
    print(f"3. Insight: Employees who stayed earn Rs. {diff:,.2f} more on average.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Load Data
    df = create_dummy_dataset()
    
    # 2. Overview
    step_1_data_overview(df)
    
    # 3. Clean
    df_clean = step_2_data_cleaning(df)
    
    # 4. Analyze (Univariate)
    step_3_univariate_analysis(df_clean)
    
    # 5. Analyze (Bivariate)
    step_4_bivariate_analysis(df_clean)
    
    # 6. Conclusion
    step_5_generate_report(df_clean)