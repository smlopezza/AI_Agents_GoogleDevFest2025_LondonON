import os
from google.adk.agents import Agent
# from agents.insights_agent.agent import insights_agent
# from agents.segmentation_agent.agent import segmentation_agent
# from agents.strategy_agent.agent import strategy_agent
from google.adk.agents import SequentialAgent
from agents.orchestration_agent.agent import coordinator_agent
from agents.ethics_and_safety_agent.agent import ethical_agent


# Ensures the ethical and safety agent runs before providing the answer to the user
root_agent = SequentialAgent(
    name="Root_agent", 
    sub_agents=[coordinator_agent, ethical_agent]
)



# root_agent =  Agent(
#     name="root_agent",
#     description="Acts as the root agent to coordinate sub-agents.",
#     model='gemini-2.5-flash',
#     instruction="You are the root agent. Your job is to coordinate sub-agents to answer user queries effectively.",
#     sub_agents=[insights_agent, segmentation_agent, strategy_agent],
# )
    