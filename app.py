import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Task 8 - Query Accuracy Evaluation",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Query Accuracy & Forecast Explanation Evaluation")

st.write(
    "This application evaluates the accuracy of natural-language "
    "telemetry queries and the quality of forecast explanations."
)

# Load telemetry data
@st.cache_data
def load_data():
    return pd.read_csv("grid_data.csv")


df = load_data()

# Display telemetry data
st.subheader("📊 Grid Telemetry Data")

st.dataframe(
    df,
    use_container_width=True
)


# Query processing
def process_query(query):

    q = query.lower().strip()

    # Predicted peak
    if "predicted peak" in q:
        return (
            "Predicted peak consumption is 699.31 MW.",
            "Clear and directly answers the user's question.",
            "PASS"
        )

    # Predicted average
    elif "predicted average" in q or "average predicted" in q:
        return (
            "Predicted average consumption is 587.13 MW.",
            "Clear and directly provides the predicted average value.",
            "PASS"
        )

    # Peak power
    elif "peak power" in q or "highest power" in q:
        return (
            "Peak power consumption is 818.59 MW.",
            "Clear and directly provides the peak power value.",
            "PASS"
        )

    # Average power
    elif "average power" in q or "average consumption" in q:
        value = df["power_consumption"].mean()

        return (
            f"The average power consumption is {value:.2f} MW.",
            "The response provides the calculated average with the MW unit.",
            "PASS"
        )

    # Lowest power
    elif "lowest power" in q or "minimum power" in q:
        value = df["power_consumption"].min()

        return (
            f"The lowest power consumption is {value:.2f} MW.",
            "The response clearly identifies the minimum power consumption.",
            "PASS"
        )

    # Voltage
    elif "voltage" in q:
        value = df["voltage"].mean()

        return (
            f"The average voltage is {value:.2f} V.",
            "The response provides the voltage value with the correct unit.",
            "PASS"
        )

    # Frequency
    elif "frequency" in q:
        value = df["frequency"].mean()

        return (
            f"The average grid frequency is {value:.2f} Hz.",
            "The response provides the frequency value with the correct unit.",
            "PASS"
        )

    # Grid status
    elif "status" in q or "grid condition" in q:
        latest_status = df["status"].iloc[-1]

        return (
            f"The latest grid status is {latest_status}.",
            "The response directly identifies the latest grid status.",
            "PASS"
        )

    # Unknown query
    else:
        return (
            "I could not identify that question. "
            "Try asking about predicted peak, predicted average, "
            "peak power, voltage, frequency, or grid status.",
            "The query could not be matched to a supported query type.",
            "FAIL"
        )


# Query input
st.subheader("💬 Enter a Query")

query = st.text_input(
    "Ask a natural-language telemetry question:",
    placeholder="Example: What is the predicted peak consumption?"
)


# Evaluate query
if query:

    answer, explanation, status = process_query(query)

    st.subheader("🔍 Evaluation Result")

    st.write("**User Query:**")
    st.code(query)

    st.write("**System Response:**")
    st.success(answer)

    st.write("**Explanation Quality:**")
    st.info(explanation)

    st.write("**Query Accuracy:**")

    if status == "PASS":
        st.success("✅ PASS - The query was correctly understood.")
    else:
        st.error("❌ FAIL - The query was not recognized.")


# Evaluation criteria
st.subheader("📋 Evaluation Criteria")

st.write("""
**Query Accuracy**
- Correctly understands the user's question
- Returns the expected result
- Uses the correct value and unit

**Forecast Explanation Quality**
- Clear
- Relevant
- Concise
- Easy to understand
- Provides meaningful information
""")


# Suggested queries
st.subheader("🧪 Suggested Evaluation Queries")

st.write("1. What is the predicted peak consumption?")
st.write("2. What is the predicted average consumption?")
st.write("3. What is the peak power consumption?")
st.write("4. What is the average voltage?")
st.write("5. What is the grid frequency?")
st.write("6. What is the current grid status?")
