from google.adk.agents import LlmAgent

ad_writer_agent = LlmAgent(
    name="ad_writer_agent",
    model="gemini-2.5-flash",
    description="ad writer",
    instruction="Write a catchy ad copy for social media."
)
