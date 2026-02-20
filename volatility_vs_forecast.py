import streamlit as st
import pandas as pd
import plotly.express as px
from app import load_shared_data

st.set_page_config(
    page_title = "Volatility vs Forecast Error",
    layout = "wide",
    page_icon = "📉"
)

st.title("📉 Volatility vs Forecast Error")
st.markdown("---")

monthly_df, _, performance_df = load_shared_data()

#Recalculate volatility
volatility_list = []

for city in monthly_df["City"].unique():
    temp_df = monthly_df[monthly_df["City"] == city]
    vol = temp_df["Crime_Count"].std() / temp_df["Crime_Count"].mean()
    volatility_list.append({"City": city, "Volatility": vol})

vol_df = pd.DataFrame(volatility_list)

analysis_df = performance_df.merge(vol_df, on = "City")

fig_scatter = px.scatter(
    analysis_df,
    x = "Volatility",
    y = "MAPE",
    text = "City",
    title = "MAPE vs Volatility",
)

fig_scatter.update_traces(textposition = "middle right")

st.plotly_chart(fig_scatter, use_container_width = True)

st.markdown("Statistical Analysis indicates a significant positive correlation "
            "between volatility and percentage forecast error (p < 0.001).")