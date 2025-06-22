from google.adk.agents import LlmAgent

tone_optimizer_agent = LlmAgent(
    name="tone_optimizer_agent",
    model="gemini-2.5-flash",
    description="tone fixer",
    instruction="Rewrite the generated content in the desired tone."
)
