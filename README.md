Canada Data Science Jobs Analysis 🇨🇦 📊
This project focus on building an end-to-end Data Engineering and Analysis pipeline to explore the Data Science job market in Canada (2024). The project covers everything from data cleaning and Natural Language Processing (NLP) to database management and visualization.

  Project Workflow
The project is divided into four main stages:

1. Data Cleaning & Preprocessing
Source: Raw dataset from Kaggle containing job postings.

Tools: Pandas.

Tasks: Handled missing values, formatted dates, and normalized categorical columns like cities and job titles to ensure consistency.

2. Skills Extraction (NLP Task) 🧠
The most challenging part of the project was extracting technical skills from long and unstructured job descriptions.

Library: spaCy (NLP).

Technique: Implemented a custom EntityRuler to identify and extract specific hard skills (e.g., Python, SQL, AWS, Machine Learning) from the description column.

Normalization: Grouped synonyms and handled case sensitivity to provide an accurate count of the most in-demand skills.

3. Data Loading (ETL) 🗄️
After cleaning and processing, the structured data was moved to a relational database for scalability.

Database: PostgreSQL.

Process: Used SQLAlchemy to create a robust connection and load the final DataFrame into a structured table.

4. Data Visualization 📈
Exploratory Data Analysis (EDA) was performed directly using Pandas Plotting to gain insights into the market.

Insights Generated:

Top 10 Cities: Geographic distribution of job opportunities.

Top 10 Skills: The most required technologies extracted via NLP.

Experience Levels: Distribution of Junior vs Senior roles.

Work Type: Analysis of Remote vs. On-site vs. Hybrid trends.

🛠️ Tech Stack
Language: Python 🐍

Data Manipulation: Pandas

NLP: spaCy

Database: PostgreSQL

Visualization: Pandas (Matplotlib backend)

📁 Project Structure
cleaning_nlp.ipynb: Jupyter notebook containing the Python code.

data/: Raw and cleaned datasets.

visualizations/: Exported charts and insights.
