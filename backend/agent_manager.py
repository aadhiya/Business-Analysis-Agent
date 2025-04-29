from backend.agent_goal_business import business_analysis_agent

def handle_business_goal(file_content):
    # Simple agent switcher for Business Analysis goal
    return business_analysis_agent(file_content)
