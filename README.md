# 📊 Machine Learning Based City-Wise Crime Analysis and Forecasting 

A machine learning powered crime analytics system that analyzes historical crime patterns across multiple cities and forecasts future crime trends using time-series modeling and ensemble learning.

The project combines data preprocessing, statistical analysis, machine learning forecasting, risk modeling, and interactive visualization to create a complete crime analysis pipeline.

The system also includes an interactive Streamlit dashboard for exploring crime trends, forecasting results, and crime risk indicators.

## 🤖 The Process
I downloaded a dataset from kaggle containing approximately 40,000 records. I cleaned it into a monthly-aggregated dataset for each city and month. There were total 29 cities across 55 months, giving almost 1600 records which would be useful for feature engineering and temporal machine learning modelling. 
I performed Exploratory Data Analysis and extracted some key insights about crime trends including how crime volume did not alone dictate crime risk. It had to be paired with trend slopes and overall volatility to ascertain which cities were an emerging risk, which ones were stabilizing and which ones had a downward trend. 

I used these insights to train my benchmark SARIMA model which could not give me satisfactory results because it assumed linear, stable data contrary to my volatile and non-linear crime data. So I trained a Rolling Random Forest model which gave me better results overall.
I, then, created an interactive dashboard to evaluate all the forecasts that were generated and provide insights into crime data using structural trend analysis metrics like Moving Averages, Deltas and trend slopes.

## Future Improvements
- The current dataset contained historical data which was more or less stable and static and did not replicate real life crime statistics. In the future, we could gain access to APIs that provide live data to the model which can be continuously retrained to give better results.
- The model only took into account historical crime data without accounting for exogenous factors such as economic conditions, political situations, population density, etc, which significantly affects how crime data can fluctuate. We could train the model on such factors to ensure a more accurate and real-world ready model for implementation. 

## Technology Stack
Programming Language: Python <br />
Data Analysis: Pandas <br />
Data Visualization: Matplotlib <br />
Forecast Models: Scikit-Learn <br />
Interactive Plot: Plotly <br />
Dashboard: Streamlit

## Installation

Clone the repository:
```
git clone https://github.com/yourusername/crime-forecasting-project.git
cd crime-forecasting-project
```

Install required dependencies:

```
pip install -r requirements.txt
Running the Dashboard
```

Launch the Streamlit dashboard:

```
streamlit run dashboard/app.py
```

The dashboard will open in your browser. 
