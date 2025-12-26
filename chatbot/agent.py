memory = []

def remember(text: str):
    memory.append(text)

def get_memory():
    return memory

def reset_memory():
    memory.clear()

memory ={}

def remember(session_id:str, text:str):
    if session_id not in memory:
        memory[session_id] = []
    memory[session_id].append(text)

def get_memory(session_id:str):
    return memory.get(session_id, [])

def reset_memory(session_id:str):
    if session_id in memory:
        memory[session_id].clear()