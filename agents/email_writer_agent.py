from google.adk.agents import LlmAgent

email_writer_agent = LlmAgent(
    name="email_writer_agent",
    model="gemini-2.5-flash",
    description="email writer",
    instruction="Generate a short promotional email based on the product."
)
