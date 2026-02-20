import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app import load_shared_data

st.set_page_config(
    page_title = "City Crime Intelligence Platform",
    layout = "wide",
    page_icon = "📊")

#Load data
monthly_df, future_df, performance_df = load_shared_data()

st.title("📊 City Crime Intelligence Platform")
st.markdown("Forecasting & Risk Analytics (2020 - 2025 Projection)")
st.markdown("---")

#Sidebar
city = st.selectbox("Select City", monthly_df["City"].unique(), width = 300)

# #Creating tabs
# tab1, tab2, tab3 = st.tabs([
#     "📈 City Analysis",
#     "🏆 City Comparison",
#     "📊 Volatility vs Accuracy"
# ]
# )

city_data = monthly_df[monthly_df["City"] == city]
future_data = future_df[future_df["City"] == city]
performance_data = performance_df[performance_df["City"] == city]

latest_actual = city_data["Crime_Count"].iloc[-1]
avg_crime = city_data["Crime_Count"].mean()
volatility = city_data["Crime_Count"].std() / avg_crime

col1, col2, col3 = st.columns(3)

col1.metric("Latest Crime Count", int(latest_actual))
col2.metric("Average Monthly Crime", round(float(avg_crime), 1))
col3.metric("Volatility", round(float(volatility), 3))

st.markdown("---")

#Risk Score = 
    #(forecast_mean / historical_mean) * 0.6 +
    #volatility * 0.4

#60% weight -> Projected Increase
#40% weight -> Structural Instability    
forecast_mean = future_data["Forecast"].mean()
risk_score = (forecast_mean / avg_crime) * 0.6 + volatility * 0.4 #Avg_crime = historical_mean

if risk_score > 0.8:
    risk_label = "🔴 High Risk"
elif risk_score > 0.65:
    risk_label = "🟠 Moderate Risk"
else:
    risk_label = "🟢 Low Risk"

st.subheader("Risk Classification 🚨")

st.markdown(f"### {risk_label}")
st.write(f"Risk Score: {round(risk_score, 3)}")

st.markdown("---")

#Plotly Historical + Forecast
fig = go.Figure()

fig.add_trace(go.Scatter(
    x = city_data["Date"],
    y = city_data["Crime_Count"],
    mode = "lines",
    name = "Historical"
))

fig.add_trace(go.Scatter(
    x = future_data["Date"],
    y = future_data["Forecast"],
    mode = "lines",
    name = "Forecast 2025",
    line = dict(dash = "dash")
))

fig.update_layout(
    title = f"{city} Crime Trend & Forecast",
    xaxis_title = "Date",
    yaxis_title = "Crime Count",
    height = 500
)

st.plotly_chart(fig, use_container_width = True)

st.markdown("---")

st.subheader("📉 Model Performance")

col1, col2, col3 = st.columns(3)
col1.metric("MAE", round(float(performance_data["MAE"].values[0]), 2))
col2.metric("RMSE", round(float(performance_data["RMSE"].values[0]), 2))
col3.metric("MAPE (Scale-Normalized Error)", str(round(float(performance_data["MAPE"].values[0]), 2)) + "%")

st.download_button(
    label = "Download 2025 Forecast",
    data = future_data.to_csv(index = False),
    file_name = f"{city}_2025_forecast.csv"
)