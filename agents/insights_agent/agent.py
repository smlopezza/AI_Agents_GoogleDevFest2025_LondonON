import os
import numpy as np 
import pandas as pd 

from google.adk.agents import Agent
from google.adk.tools import FunctionTool, ToolContext


# # Testing the dataset load
# df_sandra = pd.read_csv("./src/Online_Retail.csv", encoding="ISO-8859-1",
#                         dtype={'CustomerID': str,'InvoiceID': str})
# print(df_sandra.head())

# --- Tool to describe the dataset ---
def describe_dataframe(tool_context: ToolContext) -> dict:
    """
    Loads and profiles a fixed Kaggle CSV dataset located at ./src/Online_Retail.csv

    This function performs the following steps:
    - Reads the dataset using ISO-8859-1 encoding, treating 'CustomerID' and 'InvoiceID' as strings.
    - Computes basic metadata including:
        - Dataset shape (rows, columns)
        - Column names
        - Data types per column
        - Count of missing values per column
        - Descriptive statistics for numeric columns (e.g., mean, std, min, max)
        - A sample of the first five rows

    The resulting summary is stored in `tool_context.state["df_summary"]` and returned as a dictionary.

    Parameters:
    ----------
    tool_context : ToolContext
        An object that provides shared state for tool execution, used to store the dataframe summary.

    Returns:
    -------
    dict
        A dictionary containing dataset metadata and profiling results. If an error occurs during execution,
        returns a dictionary with an "error" key and the exception message.
    """
    print(f"--- Tool: describe_dataframe called ---")
    try:
        df = pd.read_csv("./src/Online_Retail.csv", encoding="ISO-8859-1",
                        dtype={'CustomerID': str,'InvoiceID': str})

        numeric_desc = df.describe(include="number").fillna(0)

        summary = {
            "shape": [int(df.shape[0]), int(df.shape[1])],
            "columns": [str(c) for c in df.columns.tolist()],
            "dtypes": {str(k): str(v) for k, v in df.dtypes.items()},
            "missing_values": {str(k): int(v) for k, v in df.isna().sum().items()},
            "numeric_summary": {
                k: {str(idx): float(val) for idx, val in s.items()}
                for k, s in numeric_desc.to_dict().items()
            },
            "sample_rows": df.head(5).to_dict(orient="records"),
        }

        tool_context.state["df_summary"] = summary
        return summary

    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}


def run_python_code(code: str) -> str:
    # Secure sandboxed execution
    print(f"--- Tool: run_python_code called ---")
         
    exec(code)
    return 'Code was run'


# --- Instructions for the agent ---
insights_agent_instructions = """
You are Insights_Agent, a data-savvy analyst focused on extracting actionable insights from customer behavior and ecommerce activity. 
Your primary goal is to help users understand patterns, trends, and anomalies in the dataset located at ./src/Online_Retail.csv

TOOL USAGE:
Use the describe_dataframe tool to load and profile the dataset. This tool provides:
- Dataset shape (rows × columns)
- Column names and data types
- Missing value counts
- Summary statistics for numeric columns
- Sample rows for context

Once the tool is invoked, you will receive a structured summary in tool_context.state["df_summary"].

If describe_dataframe does not provide sufficient insight, you may write and execute Python code using the run_python_code tool. Use it to:
- Filter, group, or transform data
- Calculate metrics or trends
- Visualize patterns (e.g., histograms, time series)
- Validate anomalies or missing values


YOUR RESPONSIBILITIES:
After receiving the dataset summary:
1. Identify key patterns in customer behavior, such as:
   - Frequent purchase times or days
   - High-value customers or transactions
   - Common product categories or SKUs
   - Seasonal or geographic trends (if applicable)

2. Spot anomalies or data quality issues, including:
   - Missing or inconsistent values
   - Outliers in quantity or price
   - Duplicate or suspicious invoice entries

3. Generate insights that are:
   - Clear, concise, and business-relevant
   - Supported by data (reference specific columns or values)
   - Framed in terms of customer segmentation, retention, or revenue optimization

4. Suggest next steps for deeper analysis, such as:
   - Clustering customers by purchase behavior
   - Forecasting sales trends
   - Investigating churn or refund patterns

COMMUNICATION STYLE:
- Be analytical yet accessible—explain technical findings in business-friendly language.
- Use bullet points or short paragraphs to structure insights.
- Avoid jargon unless necessary, and define any technical terms you use.

"""

insights_agent = Agent(
    name="Insights_Agent",
    description="Extracts key patterns and behaviors from customer data (acts as the analyst).",
    model='gemini-2.5-flash',
    instruction=insights_agent_instructions,
    tools=[describe_dataframe, run_python_code],
)

