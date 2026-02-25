# 🇨🇦 Canada Data Science Jobs Analysis Pipeline
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)

## 📌 Project Overview
This project is an end-to-end **Data Engineering & BI pipeline**. The goal was to analyze the Data Science job market in Canada by processing raw data from **Kaggle**, extracting insights using **NLP**, and storing/visualizing the results.

---

## 🛠️ The Pipeline Stages

### 1. Data Cleaning & Preprocessing
The raw dataset was messy. Using **Pandas**, I performed:
* **Normalization:** Fixed city names (e.g., merging "Toronto, ON" and "Toronto").
* **Data Sanitization:** Handled missing values and removed duplicates.
* **Feature Engineering:** Standardized job titles and contract types.

### 2. Advanced NLP Task (Skills Extraction) 🧠
The biggest challenge was the `description` column (unstructured and very long text). 
* **Tool:** `spaCy` (Natural Language Processing).
* **The Task:** Built a custom **EntityRuler** to scan descriptions and extract technical skills.
* **Why?** To transform "messy text" into a structured list of the **Top 10 Technical Skills** demanded by Canadian employers.

### 3. Database Management (ETL) 🗄️
After cleaning, I moved the data from a local environment to a production-like environment:
* **Database:** `PostgreSQL`.
* **Method:** Used `SQLAlchemy` to automate the **Load** process from Python to SQL.

### 4. Data Visualization 📊
Instead of basic charts, I used **Pandas Plotting** to generate business insights:
* **Market Trends:** Distribution of Remote vs. On-site work.
* **Seniority Analysis:** Percentage of Junior vs. Senior roles.
* **Geographic Focus:** Bar charts of the most active cities in Canada.

---

## 📂 Project Structure
```text
├── data/                   # Raw and Cleaned CSV files
├── notebooks/              # Jupyter Notebook with the full code
├── README.md               # Project documentation
