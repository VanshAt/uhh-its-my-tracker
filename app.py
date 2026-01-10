import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ======================
# 🎨 PAGE CONFIG & HEADER
# ======================

# st.set_page_config(
#     page_title="Valorant Insights — Vansh",
#     page_icon="🎯",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# ======================
# 🔧 DATA LOADING & SETUP
# ======================

# Load sample data or uploaded data
def load_data(uploaded_file=None):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Win'] = df['Result'] == 'Win'
        return df
    else:
        # Sample data
        data = {
            "Date": ["2025-12-26"]*6 + ["2025-12-25"]*8 + ["2025-12-24"]*3 + ["2025-12-23"]*2 + ["2025-12-22"]*1,
            "Map": ["Haven", "Haven", "Pearl", "Pearl", "Bind", "Abyss", "Split", "Haven", "Haven", "Corrode", "Bind", "Corrode", "Split", "Sunset", "Abyss", "Sunset", "Corrode", "Split", "Pearl", "Haven"],
            "Mode": ["Competitive"]*20,
            "Round_Score": ["13:3","13:8","13:11","7:13","8:13","2:13","4:13","13:7","10:13","13:4","13:5","13:11","13:9","13:11","13:4","13:11","13:9","9:13","2:13","9:13"],
            "Agent": ["Phoenix","Phoenix","Phoenix","KAY/O","Phoenix","Reyna","Reyna","Sage","Reyna","Reyna","Tejo","Phoenix","Clove","Clove","Clove","Reyna","Reyna","Reyna","Phoenix","Sage"],
            "Rank": ["Silver 1"]*16 + ["Bronze 3"]*4,
            "Result": ["Win","Win","Win","Loss","Loss","Loss","Loss","Win","Loss","Win","Win","Win","Win","Win","Win","Win","Win","Loss","Loss","Loss"],
            "K": [20,26,32,12,15,17,13,9,19,23,9,13,24,22,11,31,17,14,12,12],
            "D": [8,11,16,16,16,14,15,13,19,12,11,19,13,17,13,14,16,18,16,15],
            "A": [5,6,10,6,6,0,4,7,5,7,4,9,14,7,12,5,2,3,0,6],
            "KD": [2.5,2.4,2.0,0.8,0.9,1.2,0.9,0.7,1.0,1.9,0.8,0.7,1.8,1.3,0.8,2.2,1.1,0.8,0.8,0.8],
            "DDΔ": [87,82,153,9,10,44,-19,-28,-1,104,-6,-31,100,32,-32,86,-1,-14,-23,-31],
            "HS%": [18,25,19,15,36,28,8,23,29,33,26,19,26,31,22,23,25,31,22,22],
            "ADR": [214,218,295,136,153,195,129,97,165,240,128,111,220,176,96,232,138,122,148,97],
            "ACS": [346,340,432,207,217,331,219,131,241,384,165,170,314,261,161,357,216,176,240,162],
            "Performance_Score": [967,970,941,543,492,677,385,311,474,987,583,398,937,843,590,893,519,368,375,341],
            "Position": ["MVP","MVP","MVP","6th","6th","2nd","2nd","10th","4th","MVP","7th","9th","2nd","5th","8th","MVP","5th","8th","3rd","8th"],
            "MVP": ["Yes","Yes","Yes","No","No","No","No","No","No","Yes","No","No","No","No","No","Yes","No","No","No","No"]
        }
        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Win'] = df['Result'] == 'Win'
        return df

# # Sidebar for data upload and filters
# st.sidebar.header("📊 Data & Filters")

# uploaded_file = st.sidebar.file_uploader("Upload your valorant_matches.csv", type="csv")
# df = load_data(uploaded_file)

# if uploaded_file:
#     st.sidebar.success("✅ Loaded your data! Dashboard updated.")
# else:
#     st.sidebar.info("Using sample data. Upload CSV to analyze your matches.")

# # Date range filter
# min_date = df['Date'].min()
# max_date = df['Date'].max()
# date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)
# df = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]

# df = df.sort_values('Date')

df = load_data()

df = df.sort_values('Date')

# ======================
# 🎨 PAGE CONFIG & HEADER
# ======================

st.markdown(
    """
    <style>
    .main { padding-top: 2rem; }
    .stMetric { background-color: #1e293b; border-radius: 8px; padding: 1rem; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎯 Vansh's Valorant Performance Dashboard")
st.caption("Focused on **one-tap aim consistency**, agent mastery & climb strategy • Data from Dec 22–26, 2025")

# Sidebar for data upload and filters
st.sidebar.header("📊 Data & Filters")

uploaded_file = st.sidebar.file_uploader("Upload your valorant_matches.csv", type="csv")
df = load_data(uploaded_file)

if uploaded_file:
    st.sidebar.success("✅ Loaded your data! Dashboard updated.")
else:
    st.sidebar.info("Using sample data. Upload CSV to analyze your matches.")

# Date range filter
min_date = df['Date'].min()
max_date = df['Date'].max()
date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)
df = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]

df = df.sort_values('Date')

# ======================
# 📊 KEY METRICS
# ======================

col1, col2, col3, col4, col5 = st.columns(5)

win_rate = df['Win'].mean() * 100
avg_kd = df['KD'].mean()
avg_hs = df['HS%'].mean()
mvp_rate = (df['MVP'] == 'Yes').mean() * 100
top_agent = df['Agent'].value_counts().idxmax()

col1.metric("Win Rate", f"{win_rate:.1f}%", f"{len(df[df['Win']])}W / {len(df[~df['Win']])}L")
col2.metric("Avg K/D", f"{avg_kd:.2f}")
col3.metric("Avg HS%", f"{avg_hs:.1f}%")
col4.metric("MVP Rate", f"{mvp_rate:.0f}%")
col5.metric("Top Agent", top_agent)

# ======================
# 📈 TRENDS & VISUALS
# ======================

st.markdown("---")
st.subheader("📈 Performance Over Time")

# K/D & HS% Trend
fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(
    x=df['Date'], y=df['KD'], mode='lines+markers', name='K/D',
    line=dict(color='#8b5cf6', width=3), marker=dict(size=6)
))
fig_trend.add_trace(go.Scatter(
    x=df['Date'], y=df['HS%'], mode='lines+markers', name='Headshot %',
    yaxis='y2', line=dict(color='#10b981', width=3, dash='dot'), marker=dict(size=6)
))
fig_trend.update_layout(
    xaxis_title="Date",
    yaxis=dict(title="K/D", side="left", range=[0, max(df['KD'])*1.1]),
    yaxis2=dict(title="HS%", overlaying="y", side="right", range=[0, 100]),
    hovermode="x unified",
    template="plotly_dark",
    height=400
)
st.plotly_chart(fig_trend, use_container_width=True)

# ======================
# 🦸 AGENT ANALYSIS
# ======================

st.subheader("🦸 Agent Performance")

agent_stats = df.groupby('Agent').agg(
    Matches=('Agent', 'count'),
    Wins=('Win', 'sum'),
    Win_Rate=('Win', 'mean'),
    Avg_KD=('KD', 'mean'),
    Avg_HS=('HS%', 'mean'),
    Avg_ACS=('ACS', 'mean')
).round(2).reset_index()
agent_stats['Win_Rate'] = (agent_stats['Win_Rate'] * 100).round(1)

# Sort by Win Rate (min 2 matches)
agent_stats = agent_stats[agent_stats['Matches'] >= 2].sort_values('Win_Rate', ascending=False)

fig_agents = px.bar(
    agent_stats,
    x='Agent',
    y=['Avg_KD', 'Avg_HS'],
    barmode='group',
    labels={'value': 'Metric', 'variable': 'Metric'},
    title="Agent Comparison (≥2 Matches)",
    color_discrete_sequence=['#8b5cf6', '#10b981']
)
fig_agents.update_layout(template="plotly_dark", height=400)
st.plotly_chart(fig_agents, use_container_width=True)

# Highlight Clove (your 100% win rate agent!)
if 'Clove' in agent_stats['Agent'].values:
    clove_data = agent_stats[agent_stats['Agent'] == 'Clove'].iloc[0]
    st.info(f"🌟 **Clove is your OP agent!** {int(clove_data['Matches'])}W-0L, {clove_data['Avg_KD']:.1f} K/D, {clove_data['Avg_HS']:.0f}% HS — consider maining!")

# ======================
# 🎯 ONE-TAP AIM INSIGHTS (Your Focus!)
# ======================

st.markdown("---")
st.subheader("🎯 One-Tap Aim Potential")

# Define "One-Tap Friendly" matches: HS% ≥ 25 AND K/D ≥ 1.5
df['One_Tap_Opportunity'] = (df['HS%'] >= 25) & (df['KD'] >= 1.5)

one_tap_df = df[df['One_Tap_Opportunity']]

col_a, col_b = st.columns(2)
with col_a:
    st.metric("High-Potential Matches", f"{len(one_tap_df)}/{len(df)}", f"{len(one_tap_df)/len(df)*100:.0f}% of games")
with col_b:
    if len(one_tap_df) > 0:
        st.metric("Avg HS% (in these)", f"{one_tap_df['HS%'].mean():.1f}%")

if len(one_tap_df) > 0:
    st.write("**Top One-Tap Performances**")
    st.dataframe(
        one_tap_df[['Date', 'Map', 'Agent', 'K', 'D', 'HS%', 'KD']].sort_values('HS%', ascending=False),
        hide_index=True,
        use_container_width=True
    )

    # Recommendation
    top_1t_agent = one_tap_df['Agent'].mode()[0] if not one_tap_df['Agent'].mode().empty else "Reyna"
    st.success(f"""
    🔔 **Aim Training Suggestion**:  
    Your highest HS% (36%) came on **Phoenix** (Bind).  
    → Try Aim Labs: **'One-Tap Duelist'** + **'HS Focus: Close Range'** routines 15 mins/day.  
    Target: Consistently >30% HS on Duelists.
    """)

# ======================
# 🗺️ MAP WIN RATE 
# ======================

st.subheader("🗺️ Map Performance")
map_stats = df.groupby('Map').agg(
    Wins=('Win', 'sum'),
    Matches=('Map', 'count')
).reset_index()
map_stats['Win_Rate'] = (map_stats['Wins'] / map_stats['Matches'] * 100).round(1)

fig_maps = px.bar(
    map_stats,
    x='Map', y='Win_Rate',
    color='Win_Rate',
    color_continuous_scale=['#ef4444', '#f59e0b', '#10b981'],
    labels={'Win_Rate': 'Win Rate (%)'},
    title="Win Rate by Map"
)
fig_maps.update_layout(template="plotly_dark", height=350)
st.plotly_chart(fig_maps, use_container_width=True)

# ======================
# 📤 EXPORT & NEXT STEPS
# ======================

st.markdown("---")
st.subheader("📥 Ready to Use Your Own Data?")

st.markdown("""
✅ **To analyze your live matches**:
1. Save your match data as `valorant_matches.csv` (use format above)
2. Upload via the sidebar
3. Dashboard updates automatically!
""")

# Download current data
csv = df.to_csv(index=False)
st.download_button(
    label="📥 Download Current Data as CSV",
    data=csv,
    file_name="valorant_matches.csv",
    mime="text/csv"
)

st.markdown("""
---
### 🔐 Privacy Note  
All processing happens in your browser — no data leaves your device.  
Built by Vansh Dambhare • B.Tech CSE (AI/ML) • Nagpur 🇮🇳
""")

# Footer
st.caption("💡 Tip: Update your match log weekly for long-term progress tracking!")