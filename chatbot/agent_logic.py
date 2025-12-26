from llm import call_llm
from agent import remember, get_memory, reset_memory
from tools import calculator
from search import search_wikipedia

def agent_think(session_id: str, user_input: str):

    if "reset" in user_input.lower():
        reset_memory(session_id)
        return "Memory has been cleared."

    tool = decide_tool(user_input)

    # 🔍 SEARCH TOOL
    if tool == "search":
        result = search_wikipedia(user_input)
        remember(session_id, f"User: {user_input}")
        remember(session_id, f"Search result: {result}")
        return result

    # 🧮 CALCULATOR TOOL
    if tool == "calculator":
        expression = extract_math_expression(user_input)
        result = calculator(expression)

        remember(session_id, f"User: {user_input}")
        remember(session_id, f"Expression: {expression}")
        remember(session_id, f"Agent (calculator): {result}")

        return result


    # 💬 NORMAL LLM RESPONSE
    prompt = f"""
You are a helpful AI agent.

Memory:
{get_memory(session_id)}

User said:
{user_input}

Respond briefly.
"""

    response = call_llm(prompt)

    remember(session_id, f"User: {user_input}")
    remember(session_id, f"Agent: {response}")

    return response


def decide_tool(user_input: str) -> str:
    prompt = f"""
You are an AI agent.

Decide which tool is needed for the user input below.

Tools:
- search → for factual, real-world information
- calculator → for math calculations
- none → for general conversation

Respond with ONLY one word: search, calculator, or none.

User input:
{user_input}
"""

    decision = call_llm(prompt)
    return decision.strip().lower()

def extract_math_expression(user_input: str) -> str:
    prompt = f"""
Extract ONLY the mathematical expression from the text below.
Do not add words.
Do not explain.

Text:
{user_input}

Expression:
"""
    expression = call_llm(prompt)
    return expression.strip()
