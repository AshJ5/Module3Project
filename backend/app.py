from fastapi import FastAPI, Request, Response
from game_state_manager import GameStateManager

app = FastAPI(title="🥪 Sandwich Quest Backend")

# Simple manual CORS middleware
@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    if request.method == "OPTIONS":
        return Response(status_code=200, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS",
            "Access-Control-Allow-Headers": "*",
        })

    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


game_manager = GameStateManager()


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "message": "🥪 Sandwich Quest Backend is running!"
    }


@app.get("/api/game/state")
def get_game_state(sessionId: str = "default-session"):
    session = game_manager.get_session(sessionId)
    return session


@app.post("/api/game/choice")
def record_choice(choice: dict, sessionId: str = "default-session"):
    choice_id = choice.get("choiceId")
    scene_id = choice.get("sceneId")
    next_scene_id = choice.get("nextSceneId")
    if not choice_id or not scene_id or not next_scene_id:
        return {"error": "Missing required fields: choiceId, sceneId, nextSceneId"}

    updated_session = game_manager.record_choice(
        sessionId, choice_id, scene_id, next_scene_id
    )
    print(f"Choice recorded - Session: {sessionId}, Choice: {choice_id}")
    return {"success": True, "session": updated_session}


@app.post("/api/game/reset")
def reset_game(sessionId: str = "default-session"):
    reset_session = game_manager.reset_session(sessionId)
    return {"success": True, "session": reset_session}


@app.get("/api/admin/sessions")
def get_all_sessions():
    sessions = game_manager.all_sessions()
    return {"totalSessions": len(sessions), "sessions": sessions}


@app.get("/api/admin/stats")
def get_statistics():
    sessions = game_manager.all_sessions()
    total = len(sessions)
    avg_choices = round(sum(len(s.get("choices", [])) for s in sessions) / total, 2) if total else 0
    crate = sum(1 for s in sessions if any(c.get('to') == 'ending_crate' for c in s.get('choices', [])))
    chase = sum(1 for s in sessions if any(c.get('to') == 'ending_chase' for c in s.get('choices', [])))
    return {
        "totalSessions": total,
        "averageChoices": avg_choices,
        "crate_ending": crate,
        "chase_ending": chase
    }


if __name__ == "__main__":
    import uvicorn
    print("🥪 Sandwich Heist Backend running on http://localhost:8000")
    print("📊 Admin stats available at http://localhost:8000/api/admin/stats")
    print("📚 Docs available at http://localhost:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)
