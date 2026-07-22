from google.adk.agents import LlmAgent
# from google.adk.models.lite_llm import LiteLlm
from google.genai import types
from google.adk.planners import BuiltInPlanner

import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine_id = os.environ.get("GOOGLE_CLOUD_AGENT_ENGINE_ID", "NULL_ENGINE_ID")
logger.info("#####  Using Google Cloud Agent Engine ID: %s", engine_id)

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

# To use local OpenAI-compatible endpoint
# llm = LiteLlm(
#     model="LOCAL",              # "openai/" prefix = OpenAI-compatible endpoint
#     api_base="http://localhost:8080/v1",  # note: api_base, not base_url
#     api_key="NONE",
# )

#Set default model
LlmAgent.set_default_model("gemini-2.5-flash")



# To use Gemini 2.5 Flash model instead of local OpenAI-compatible endpoint
# llm = LiteLlm(model="gemini-2.5-flash") 
llm = "gemini-2.5-flash" 
# Change env.sample to .env so it will determine whether to use Gemini (AI Studio / Gemini API)or enterprise Vertex with google project

root_agent = LlmAgent(
    name="simple_math_agent",
    model=llm,
    description="Agent to answer questions about addition and subtraction of two integers.",
    instruction="""You are a helpful agent who can answer user questions about the sum and difference of two integers.
    When a user asks for the sum or difference of two integers:
    1. Validate that the input is in the form of two integers.
    2. If the input is valid, call the appropriate tool (add or subtract) to compute the result.
    3. Return the result to the user.
    Example Query: "Add {a} and {b}"
    Example Response: "The sum of {a} and {b} is {result}."
    Example Query: "Subtract {a} from {b}"
    Example Response: "The difference of {a} and {b} is {result}."
    """,
    generate_content_config = types.GenerateContentConfig(
        temperature=0.0,
        max_output_tokens=256,
        # safety_settings=types.SafetySetting(
        #     category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        #     threshold=types.HarmBlockThreshold.BLOCK_NONE
        # ),
        # Add Model Armor Config
        # model_armor_config=types.ModelArmorConfig(
        #     enable_model_armor=True,
        #     model_armor_level=types.ModelArmorLevel.STRICT,
        # ),
    ),
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_budget=1024
        )
    ),
    include_contents = "default",
    tools=[add, subtract]
)
