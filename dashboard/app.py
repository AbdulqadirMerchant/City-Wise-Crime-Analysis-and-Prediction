import streamlit as st
import pandas as pd

@st.cache_data
def load_shared_data():
    monthly_df = pd.read_csv("monthly_data.csv")
    future_df = pd.read_csv("future_projection.csv")
    performance_df = pd.read_csv("performance.csv")

    monthly_df["Date"] = pd.to_datetime(monthly_df["Date"])
    future_df["Date"] = pd.to_datetime(future_df["Date"])

    return monthly_df, future_df, performance_df

city_analysis = st.Page("city_analysis.py", title = "City-Wise Analysis", icon = "📊", default = True)
city_comparison = st.Page("city_comparison.py", title = "City Comparison", icon = "🏆")
vol_vs_forecast = st.Page("volatility_vs_forecast.py", title = "Volatility vs Forecast Errors", icon = "📉")
structural_trend_analysis = st.Page("structural_trend_analysis.py",
                                    title = "Structural Trend Analysis",
                                    icon = "🧠")

#Configuring navigation
pg = st.navigation(
    [city_analysis,
    city_comparison,
    vol_vs_forecast,
    structural_trend_analysis], 
    position = "sidebar"
)

pg.run()

st.markdown("---")
st.caption("Developed using Machine Learning-based Rolling Random Forest Forecasting | Abdulqadir Merchant | 2026")
