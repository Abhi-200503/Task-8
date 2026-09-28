# Task 8 - Evaluate Query Accuracy and Forecast Explanation Quality

## Objective

The objective of Task 8 is to evaluate the accuracy of natural-language telemetry queries and the quality of forecast explanations provided by the grid assistant.

## Description

The system allows users to enter natural-language questions related to power consumption, forecasting, voltage, frequency, and grid status.

The evaluation focuses on two main areas:

1. Query Accuracy
2. Forecast Explanation Quality

## Query Accuracy

Query accuracy measures whether the system correctly understands the user's question and provides the expected result.

The tested queries include:

- Predicted peak consumption
- Predicted average consumption
- Peak power consumption
- Average power consumption
- Voltage
- Frequency
- Grid status

## Forecast Explanation Quality

Forecast explanation quality evaluates whether the system responses are:

- Clear
- Relevant
- Concise
- Easy to understand
- Provided with the appropriate measurement unit

## Technologies Used

- Python
- Streamlit
- Pandas

## Project Structure

```text
Task-8/
│
├── app.py
├── grid_data.csv
├── requirements.txt
├── README.md
└── EVALUATION_RESULTS.md
