import streamlit as st
import pandas as pd
import plotly.express as px
from app import load_shared_data

st.set_page_config(
    page_title = "City Wise Comparison",
    layout = "wide",
    page_icon = "🏆"
)

#Load data
monthly_df, future_df, performance_df = load_shared_data()

st.title("City Ranking by Forecast Error")
st.markdown("---")

ranking = performance_df.sort_values("MAE")

fig_rank = px.bar(
    ranking, 
    x = "City", 
    y = "MAE",
    title = "MAE comparison Across Cities"
)
st.plotly_chart(fig_rank, use_container_width=True)

st.dataframe(ranking, hide_index = True)

st.markdown("---")

st.subheader("Top 5 Projected Rising Risk Cities")

risk_list = []

for city in monthly_df["City"].unique():
    hist = monthly_df[monthly_df["City"] == city]
    future = future_df[future_df["City"] == city]

    hist_mean = hist["Crime_Count"].mean()
    future_mean = future["Forecast"].mean()
    vol = hist["Crime_Count"].std() / hist_mean

    score = (future_mean / hist_mean) * 0.6 + vol * 0.4

    risk_list.append({"City":city, "Risk Score": score})

risk_df = pd.DataFrame(risk_list).sort_values("Risk Score", ascending = False)

st.dataframe(risk_df.head(5), hide_index=True)

st.markdown("---")
st.subheader("Model Selection Rationale")

st.write("""
Initial experimentation compared SARIMA and Random Forest on representative cities.
Random Forest consistently achieved lower MAE under rolling validation and 
better captured nonlinear patterns.

Therefore, Rolling Random Forest was selected as the primary forecasting model.

""")
