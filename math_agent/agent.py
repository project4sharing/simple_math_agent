from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of the two integers.
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The difference of the two integers.
    """
    return a - b

llm = LiteLlm(
    model="LOCAL",              # "openai/" prefix = OpenAI-compatible endpoint
    api_base="http://localhost:8080/v1",  # note: api_base, not base_url
    api_key="NONE",
)

# llm = LiteLlm(model="gemini-2.5-flash") to use Gemini 2.5 Flash model instead of local OpenAI-compatible endpoint
# Change env.sample to .env so it will determine whether to use Gemini (AI Studio / Gemini API)or enterprise Vertex with google project

root_agent = Agent(
    name="math_agent",
    model=llm,
    description="Agent to answer questions about addition and subtraction of two integers.",
    instruction="You are a helpful agent who can answer user questions about the sum and difference of two integers.",
    tools=[add, subtract]
)
