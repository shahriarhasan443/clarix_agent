from google.adk.agents import LlmAgent

audience_agent = LlmAgent(
    name="audience_agent",
    model="gemini-2.5-flash",
    description="audience",
    instruction="Identify the product's target audience based on the product description."
)
