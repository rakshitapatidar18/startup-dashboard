# 📊 Startup Funding Analysis Dashboard

A simple interactive **Startup Funding Analysis Dashboard** built using **Python, Pandas, Matplotlib, and Streamlit**.

The dashboard analyzes startup funding data and provides overall funding and investor-level insights.

## 🚀 Features

### Overall Analysis

The dashboard currently provides:

- Total funding amount
- Maximum funding received by a startup
- Average funding
- Total number of funded startups
- Month-on-Month (MoM) funding analysis
- MoM investment count analysis

The MoM graph can be viewed in two modes:

- **Total** – Total funding amount for each month
- **Count** – Number of investments made each month

### Investor Analysis

The investor section currently provides:

- Investor selection from the dataset
- Most recent investments
- Biggest investments made by the investor
- Sector-wise investment distribution
- Year-wise investment trend

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Matplotlib**
- **Streamlit**

## 📂 Dataset

The project uses startup funding data stored in CSV files.

Main dataset used by the application:

```text
startup_cleaned.csv
```

The application automatically loads the dataset from the project folder.

## 📁 Project Structure

```text
startup-dashboard/
│
├── app.py
├── startup_cleaned.csv
└── startup_funding.csv
```

> The CSV files are currently kept locally and are not uploaded to the GitHub repository.

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rakshitapatidar18/startup-dashboard.git
```

### 2. Open the project folder

```bash
cd startup-dashboard
```

### 3. Install required libraries

```bash
pip install streamlit pandas matplotlib
```

### 4. Add the dataset

Place the `startup_cleaned.csv` file inside the project folder.

### 5. Run the application

```bash
python -m streamlit run app.py
```

The Streamlit dashboard will open in your browser.

## 📊 Current Dashboard Sections

| Section | Available Analysis |
|---|---|
| Overall Analysis | Funding metrics and MoM analysis |
| Startup | Startup selection |
| Investor | Investor investment analysis |

## 👩‍💻 Author

**Rakshita Patidar**

B.Tech – Artificial Intelligence & Data Science

## 📌 Project Status

🚧 **Currently under development**

This project is being developed while learning **Python, Data Analysis, Data Visualization, and Streamlit**.
