import os
# from google.adk.agents import Agent
from google.adk.agents import SequentialAgent
from agents.orchestration_agent.agent import coordinator_agent
from agents.ethics_and_safety_agent.agent import ethical_agent


# Ensures the ethical and safety agent runs before providing the answer to the user
root_agent = SequentialAgent(
    name="Root_agent", 
    sub_agents=[coordinator_agent, ethical_agent],
    description="Top-level agent that orchestrates the workflow and ensures ethical review.", 
)
