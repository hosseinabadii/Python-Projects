import time
import streamlit as st

from monty_hall import simulate_games

st.header(":zap: Monty Hall Simulation")

col1, col2 = st.columns([0.7, 0.3])
col1.image("../images/banner.png")
num_games = col2.number_input(
    "Enter number of games to simulate",
    min_value=1,
    value=100,
    step=100,
    max_value=1000,
)
simulate = col2.button("Run Simulation", type="primary")


wins_no_switch = 0
wins_switch = 0

col3, col4 = st.columns(2)
col3.subheader("Win Percentage Without Switching")
col4.subheader("Win Percentage With Switching")


chart1 = col3.line_chart(x=None, y=None, width=0, height=300)
chart2 = col4.line_chart(x=None, y=None, width=0, height=300)

if simulate:
    for i in range(num_games):
        num_wins_without_switching, num_wins_with_switching = simulate_games(1)

        wins_no_switch += num_wins_without_switching
        wins_switch += num_wins_with_switching

        chart1.add_rows([wins_no_switch / (i + 1)])
        chart2.add_rows([wins_switch / (i + 1)])

        time.sleep(0.01)
