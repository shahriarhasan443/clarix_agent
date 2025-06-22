from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from agents.audience_agent import audience_agent
from agents.ad_writer_agent import ad_writer_agent
from agents.email_writer_agent import email_writer_agent
from agents.tone_optimizer_agent import tone_optimizer_agent

from utils.input_handler import get_user_input

INSTRUCTION = """You are Clarix, an AI marketing assistant. Your job is to:
1. Identify the product target audience.
2. Write ad copy for social media.
3. Generate a short promotional email.
4. Rewrite content in the desired tone."""

root_agent = LlmAgent(
    name="clarix_agent",
    model="gemini-2.5-flash",
    description="marketing",
    instruction=INSTRUCTION,
    tools=[
        AgentTool(agent=audience_agent),
        AgentTool(agent=ad_writer_agent),
        AgentTool(agent=email_writer_agent),
        AgentTool(agent=tone_optimizer_agent),
    ],
)

if __name__ == "__main__":
    product, tone = get_user_input()
    result = clarix_agent.invoke({"input": product, "tone": tone})
    print("\nGenerated Marketing Content:\n")
    print(result)
