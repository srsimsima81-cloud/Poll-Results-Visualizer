# 📊 Poll Results Visualizer

## 📌 Overview

Poll Results Visualizer is a data analysis project that transforms raw poll/survey data into meaningful insights using Python.

It generates:

* Visualizations
* Summary reports
* Interactive analysis

This helps understand voting patterns across categories like **region and age group**.

---

## 🎯 Problem Statement

Raw poll or survey data is difficult to interpret directly.

This project solves that by converting raw responses into:

* Clear visual charts
* Statistical summaries
* Insightful reports

---

## 💡 Solution

A Python-based data pipeline that:

* Generates or loads poll data
* Cleans and processes it
* Performs statistical analysis
* Creates visualizations
* Produces summary reports
* Displays insights through a Streamlit dashboard

---

## ⚙️ Features

* Synthetic poll data generation
* Vote count and percentage analysis
* Region-wise and age-wise comparison
* Automated summary report generation (`summary.txt`)
* Visual charts saved as images
* Interactive Streamlit dashboard
* Jupyter Notebook for EDA

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* Jupyter Notebook

---

## 📁 Project Structure

```id="poll02"
Poll-Results-Visualizer/
│
├── data/            # Raw/generated dataset
├── outputs/         # Summary report (summary.txt)
├── images/          # Visualization charts
├── notebooks/       # EDA notebook
├── src/             # Modular Python scripts
│
├── main.py          # CLI execution file
├── app.py           # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```id="poll03"
git clone <your-repo-link>
cd Poll-Results-Visualizer
```

### 2️⃣ Create Virtual Environment

```id="poll04"
python -m venv venv
```

**Activate:**

```id="poll05"
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```id="poll06"
pip install -r requirements.txt
```

---

### 4️⃣ Run CLI Version

```id="poll07"
python main.py
```

---

### 5️⃣ Run Streamlit Dashboard

```id="poll08"
streamlit run app.py
```

---

## 📊 Outputs

After execution:

* Charts saved in `images/`
* Summary report in `outputs/summary.txt`
* Interactive dashboard opens in browser

---

## 📸 Sample Visuals


* Bar Chart → `images/bar_chart.png`
* Pie Chart → `images/pie_chart.png`
* Region Analysis → `images/region_chart.png`
* Age Analysis → `images/age_chart.png`

---

## 📈 Key Insights Generated

* Most preferred poll option
* Region-wise voting behavior
* Age group preferences
* Percentage distribution of responses

---

## 🧪 Jupyter Notebook (EDA)

The `notebooks/EDA.ipynb` contains:

* Data exploration
* Statistical analysis
* Visualization experiments
* Crosstab analysis

---

## 🔮 Future Improvements

* Real-time live polling system
* Database integration (MySQL / MongoDB)
* Power BI dashboard integration
* Sentiment analysis for open-ended responses
* API-based data collection

---

## 👨‍💻 Author

End-to-end Data Analytics project built for demonstrating skills in data analysis, visualization, and reporting



