def calculator(expression: str):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid mathematical expression."
    
