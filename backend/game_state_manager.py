class GameStateManager:
    """Minimal in-memory session manager for the game."""

    def __init__(self):
        self.sessions = {}

    def _make_session(self, sid):
        return {
            "sessionId": sid,
            "currentScene": "opening",
            "choices": [],
            "visited": ["opening"],
        }

    def get_session(self, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = self._make_session(session_id)
        return self.sessions[session_id]

    def record_choice(self, session_id, choice_id, scene_id, next_scene_id):
        s = self.get_session(session_id)
        s["choices"].append({
            "choiceId": choice_id,
            "from": scene_id,
            "to": next_scene_id,
        })
        s["currentScene"] = next_scene_id
        if next_scene_id not in s["visited"]:
            s["visited"].append(next_scene_id)
        return s

    def reset_session(self, session_id):
        self.sessions[session_id] = self._make_session(session_id)
        return self.sessions[session_id]

    def all_sessions(self):
        return list(self.sessions.values())

