# backend/agent_goal_business.py

from backend.model_runner import generate_business_report

def business_analysis_agent(file_content):
    return generate_business_report(file_content)
