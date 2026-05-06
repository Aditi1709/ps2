import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from loaders.load_orders import load_orders
from loaders.load_agents import load_agents
from core.dispatcher import Dispatcher

st.set_page_config(
    page_title="Smart Delivery Dashboard",
    layout="wide"
)

st.title("🚚 Smart Delivery Simulation Dashboard")

# Load data
orders = load_orders()
agents = load_agents()

# Convert to DataFrames
orders_df = pd.DataFrame(orders)
agents_df = pd.DataFrame(agents)

# Show raw data
st.header("📦 Orders")
st.dataframe(orders_df)

st.header("🧑‍💼 Agents")
st.dataframe(agents_df)

# Run Simulation
if st.button("▶ Run Simulation"):

    dispatcher = Dispatcher()

    dispatch_results = []

    for order in orders:

        result = dispatcher.dispatch_order(order, agents)

        if result:
            dispatch_results.append(result)

    results_df = pd.DataFrame(dispatch_results)

    st.header("✅ Dispatch Results")
    st.dataframe(results_df)

    # Metrics
    st.header("📊 Metrics")

    total_orders = len(orders)

    assigned_orders = len(dispatch_results)

    high_priority_orders = len(
        orders_df[orders_df["priority"] == "high"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Orders", total_orders)
    col2.metric("Assigned Orders", assigned_orders)
    col3.metric("High Priority Orders", high_priority_orders)

    # Agent workload
    st.header("📈 Agent Workload")

    updated_agents_df = pd.DataFrame(agents)

    workload_df = updated_agents_df[
        ["agent_id", "cumulative_assignments"]
    ]

    workload_df = workload_df.set_index("agent_id")

    st.bar_chart(workload_df)

    # Final Agent States
    st.header("🧠 Final Agent States")
    st.dataframe(updated_agents_df)

st.caption("Smart Delivery Simulation System")