# Machine Learning Based City-Wise Crime Analysis and Forecasting

A machine learning powered crime analytics system that analyzes historical crime patterns across multiple cities and forecasts future crime trends using time-series modeling and ensemble learning.

The project combines data preprocessing, statistical analysis, machine learning forecasting, risk modeling, and interactive visualization to create a complete crime analysis pipeline.

The system also includes an interactive Streamlit dashboard for exploring crime trends, forecasting results, and crime risk indicators.

## Project Overview

Urban crime patterns often evolve over time due to social, economic, and environmental factors. Understanding these patterns and forecasting future trends can assist in proactive decision-making and resource allocation.

This project develops a city-wise crime forecasting framework that:

analyzes historical crime trends

measures structural crime risk

predicts future monthly crime levels

identifies cities with increasing crime risk

provides an interactive visualization dashboard.

The system uses machine learning and time-series techniques to transform raw crime records into actionable insights.

## Dataset

The dataset used in this project contains approximately 40,000 crime records across 29 cities, covering the period:

January 2020 – July 2024

Dataset attributes include:

Date of occurrence

Crime type

City

Victim gender

Weapon used

Date closed

Other categorical attributes

Source: https://www.kaggle.com/datasets/sudhanvahg/indian-crimes-dataset

The raw event-level records were aggregated into monthly city-level time-series data for forecasting.

## Project Pipeline

The system follows a structured data science pipeline:

Raw Crime Data -> Data Cleaning & Preprocessing -> Monthly Time-Series Aggregation -> Feature Engineering (Lag Features & Rolling Statistics) ->
Crime Risk Index Calculation -> Forecasting Models (SARIMA & Random Forest) -> Model Evaluation (MAE, RMSE, MAPE) -> Recursive Forecasting
-> Streamlit Dashboard Visualization

## Feature Engineering

To enable machine learning forecasting, time-series features were created from historical crime data.

### Lag Features

Lag_1

Lag_2

Lag_3

Lag_6

Lag_12

These capture historical dependencies between past and future crime levels.

### Rolling Statistics

Rolling Mean (3 months)

Rolling Mean (6 months)

Rolling statistics help capture short-term crime trends.

## Forecasting Models

Two forecasting approaches were evaluated.

### 1. SARIMA (Baseline Statistical Model)

SARIMA was implemented as a traditional time-series forecasting model capable of capturing trend and seasonal patterns.

Limitations observed:

difficulty capturing nonlinear patterns

higher errors in volatile cities

### 2. Random Forest Forecasting Model

A Rolling Random Forest regression model was used as the final forecasting model.

#### Advantages:

captures nonlinear relationships

robust to noisy crime data

effective with lag-based features

#### Model Validation

To ensure realistic model evaluation, rolling walk-forward validation was used.

##### Process:

Train model on historical data

Predict next month

Expand training window

Retrain model

Predict next step

##### Evaluation metrics:

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

Mean Absolute Percentage Error (MAPE)

## Crime Risk Modeling

The project introduces two risk indicators.

### 1. Crime Risk Index (CRI)

The Crime Risk Index combines three factors to estimate the relative risk level of crime in a city.

$$
CRI = 0.5C_{norm} + 0.3T + 0.2V
$$

Where:

- $C_{norm}$ = normalized crime level
- $T$ = trend score representing the direction of crime change
- $V$ = volatility score measuring instability in crime patterns

### 2. Forecast-Based Risk Indicator

The Forecast Crime Index (FCI) combines forecasted crime trends and historical volatility
to estimate future crime risk.

$$
FCI = 0.6 \left(\frac{\mu_{forecast}}{\mu_{historic}}\right) + 0.4V
$$

Where:

- $\mu_{forecast}$ = mean predicted crime from the forecasting model
- $\mu_{historic}$ = historical mean crime
- $V$ = crime volatility

### Risk classification:

Risk Score	Category
> 0.80	High Risk
> 0.65	Moderate Risk
≤ 0.65	Low Risk

## Interactive Dashboard

An interactive Streamlit dashboard was built to visualize crime analytics results.

Dashboard modules include:

### City Analysis

historical crime trends

forecast visualization

model performance metrics

### City Comparison

forecast accuracy ranking

model performance comparison

rising crime risk cities

### Volatility vs Forecast Accuracy

relationship between crime volatility and forecasting error

### Structural Trend Analysis

moving averages

monthly momentum (delta)

rolling trend slope

volatility comparison

## Technology Stack

[![Stack](https://skillicons.dev/icons?i=py)](https://skillicons.dev)

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
