import uuid

sessions = {}

def criar_session(user_id: int):
    session_id = str(uuid.uuid4())
    sessions[session_id] = user_id
    return session_id

def get_user_id(session_id: str):
    return sessions.get(session_id)

def delete_session(session_id: str):
    sessions.pop(session_id, None)