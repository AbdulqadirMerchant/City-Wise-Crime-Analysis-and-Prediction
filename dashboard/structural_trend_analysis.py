import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from app import load_shared_data

st.set_page_config(
    page_title = "Structural Trend Analysis",
    layout = "wide",
    page_icon = "🧠"
)

st.title("Structural Trend Continuation")

#Load data
monthly_df, future_df, performance_df = load_shared_data()

st.markdown("---")

city = st.selectbox("Select City", monthly_df["City"].unique(), width = 300)

#Merge Historical + Forecast data
city_hist = monthly_df[monthly_df["City"] == city]
city_future = future_df[future_df["City"] == city]

combined_df = pd.concat([
    city_hist[["Date", "Crime_Count"]],
    city_future.rename(columns = {"Forecast": "Crime_Count"})[["Date", "Crime_Count"]]
])

combined_df = combined_df.sort_values("Date").reset_index(drop = "True")

#Recalculate features
combined_df["MA_3"] = combined_df["Crime_Count"].rolling(3).mean()
combined_df["MA_6"] = combined_df["Crime_Count"].rolling(6).mean()
combined_df["Delta"] = combined_df["Crime_Count"].diff()

#Rolling trend slope (6-month window)
def rolling_slope(series):
    slopes = []
    for i in range(len(series)):
        if i < 5:
            slopes.append(None)
        else:
            y = series[i - 5: i + 1] #Create a rolling window of 6 months
            x = list(range(6))
            slope = pd.Series(y).reset_index(drop = True).corr(pd.Series(x))
            slopes.append(slope)
    
    return slopes

combined_df["Trend_Slope"] = rolling_slope(combined_df["Crime_Count"])

tab1, tab2, tab3 = st.tabs([
    "Moving Averages",
    "Momentum(Delta)",
    "Trend Slope"
])

with tab1:

    fig_ma = go.Figure()

    fig_ma.add_trace(go.Scatter(
        x = combined_df["Date"],
        y = combined_df["MA_3"],
        name = "3-Month MA"
    ))

    fig_ma.add_trace(go.Scatter(
        x = combined_df["Date"],
        y = combined_df["MA_6"],
        name = "6-Month MA"
    ))

    fig_ma.update_layout(
        title = "Moving Average Continuation into 2025",
        xaxis_title = "Date",
        yaxis_title = "Crime Count",
        height = 500
    )

    st.plotly_chart(fig_ma, use_container_width = True)

with tab2:

    fig_delta = px.bar(
        combined_df,
        x = "Date",
        y = "Delta",
        title = "Monthly Crime Change (Momentum)"
    )

    st.plotly_chart(fig_delta, use_container_width = True)

with tab3:

    fig_slope = px.line(
        combined_df,
        x = "Date",
        y = "Trend_Slope",
        title = "Rolling Trend Slope Evaluation (6-Month)"
    )

    st.plotly_chart(fig_slope, use_container_width = True)

st.markdown("---")
st.subheader("Volatility Comparison")

#Historical Volatility
hist_vol = city_hist["Crime_Count"].std() / city_hist["Crime_Count"].mean()

#Forecast Volatility
forecast_vol = city_future["Forecast"].std() / city_future["Forecast"].mean()

col1, col2 = st.columns(2)

col1.metric("Historical Volatility", round(hist_vol, 3))
col2.metric("Forecast Volatility", round(forecast_vol, 3))

if forecast_vol > hist_vol:
    st.write("Projected Volatility indicates increasing structural instability")
else:
    st.write("Projected volatility suggests relative structural stabilization")
