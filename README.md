# Customer Segmentation & Marketing Planner

## Summary:
This notebook was created as part of the [Google DevFest 2025 London: Building Safe, Secure and Scalable Solutions with AI and Cloud](https://gdg.community.dev/events/details/google-gdg-london-presents-google-devfest-2025-london-building-safe-secure-and-scalable-solutions-with-ai-and-cloud/cohost-gdg-london-1) 

It is the working material for the 90 minutes interactive workshop: **Exploring Agentic AI: Hands-On with Gemini in Kaggle**


#### Event Details
Date: Saturday, September 27, 2025 <br>
Venue: Student Union Hall (Forwell Hall), Fanshawe College, London, ON 

#### Theme: Building Safe, Secure, and Scalable Solutions with AI and Cloud
This year, DevFest 2025 dives into practical applications of AI and Google Cloud—equipping developers with real-world tools, insights, and hands-on skills to design the future of technology.



## Business Problem

A UK-based online retailer is facing challenges in understanding its diverse customer base and optimizing its marketing efforts. With thousands of transactions across multiple countries, the company struggles to:

- Identify meaningful customer segments based on purchasing behavior
- Tailor marketing campaigns to different customer profiles
- Avoid generic promotions that lead to low engagement and wasted budget
- Ensure recommendations are ethical, inclusive, and aligned with customer preferences

## Business Opportunity

The rise of agentic AI presents a transformative opportunity for online retailers to move beyond static analytics and embrace intelligent, goal-driven systems. By leveraging transactional data and Gemini-powered agents, the company can:

- Unlock deeper customer insights through dynamic segmentation based on behavior and purchasing patterns
- Automate personalized marketing strategies that adapt to each customer segment, increasing engagement and conversion
- Scale decision-making with AI agents that reason, plan, and act — reducing manual effort and accelerating campaign deployment
- Build trust and brand loyalty by embedding ethical guardrails that ensure fairness, transparency, and responsible recommendations
- Empower cross-functional teams with a reusable, interpretable agent framework that supports experimentation and continuous improvement

## Objective: Build a Customer Segmentation & Marketing Planner Agent

Build an agent that:
- Segments customers based on behavior
- Recommends tailored marketing strategies
- Ensures ethical and responsible outputs


Tools:
- Python
- Google Agent Development Kit: https://google.github.io/adk-docs/


## Dataset:
For this project the 'Online Retail' dataset from the University of California, Irvine – Machine Learning Repository was selected. This dataset contains transactional data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

You can find the dataset:
- https://archive.ics.uci.edu/dataset/352/online+retail OR
- https://www.kaggle.com/datasets/carrie1/ecommerce-data

We will use the Kaggle version for this project. 

## Agent Architecture
![Agent Architecture](src/AI%20Agent%20Architecture.drawio.png)