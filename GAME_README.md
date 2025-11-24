# 🥪 The Great Sandwich Heist

A comedy interactive adventure game built with React (frontend) and Flask (Python backend).

## Project Structure

```
Module3Project/
├── frontend/
│   └── adventure/
│       ├── src/
│       │   ├── App.jsx              # Main React app component
│       │   ├── App.css              # App styles
│       │   ├── GameScene.jsx        # Game UI component
│       │   ├── GameScene.css        # Game styles
│       │   ├── game-data.json       # Story dialogue and scenes
│       │   ├── index.css
│       │   └── main.jsx
│       ├── index.html
│       ├── package.json
│       ├── vite.config.js
│       └── eslint.config.js
│
├── backend/
│   ├── app.py                       # Flask application (main server)
│   ├── main.py                      # Startup script
│   ├── game_state_manager.py        # Game state logic
│   └── requirements.txt             # Python dependencies
│
└── README.md
```

## Story Overview

Play as **Benny Bramble**, a Food Detective at the Department of Edible Investigations (DEI). Your mission: Find the missing Triple-Decker Turbo Sandwich by interrogating your ridiculous coworkers and making tough choices.

### Characters
- **Tina the Intern** - Claims the sandwich has legs and ran away
- **Hank the Janitor** - Suspiciously allergic to sandwiches
- **Dr. Picklesworth** - Works on "Project: Sentient Snack"

### Two Endings
1. **The Sandwich Conspiracy** - Open Dr. Picklesworth's crate and discover a sentient sandwich
2. **The Great Chase** - Chase the sandwich and get caught tackling a vacuum robot

## Setup & Installation

### Prerequisites
- Node.js 16+ (for frontend)
- Python 3.8+ (for backend)

### Backend Setup (Python/Flask)

1. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run the Flask server:**
   ```bash
   python app.py
   ```
   or
   ```bash
   python main.py
   ```

   Server will start on `http://localhost:5000`

### Frontend Setup (React/Vite)

1. **Install Node dependencies:**
   ```bash
   cd frontend/adventure
   npm install
   ```

2. **Run the development server:**
   ```bash
   npm run dev
   ```

   Frontend will be available at `http://localhost:5173`

## Running the Complete Application

1. **Start the backend** (Terminal 1):
   ```bash
   cd backend
   python app.py
   ```

2. **Start the frontend** (Terminal 2):
   ```bash
   cd frontend/adventure
   npm run dev
   ```

3. **Open your browser** to `http://localhost:5173`

4. **Play the game!** Make choices and see which ending you get.

## API Endpoints

### Game Endpoints
- `GET /api/health` - Health check
- `GET /api/game/state?sessionId=<id>` - Get current game state
- `POST /api/game/choice` - Record a player choice
- `POST /api/game/reset?sessionId=<id>` - Reset the game

### Admin/Analytics Endpoints
- `GET /api/admin/stats` - View game statistics
- `GET /api/admin/sessions` - View all game sessions

## Example API Calls

### Record a Choice
```bash
curl -X POST http://localhost:5000/api/game/choice \
  -H "Content-Type: application/json" \
  -d '{
    "choiceId": "interrogate_tina",
    "sceneId": "opening",
    "nextSceneId": "tina_scene"
  }'
```

### View Statistics
```bash
curl http://localhost:5000/api/admin/stats
```

## Game Flow

1. **Opening** - Discover the missing sandwich
2. **Investigation Phase** - Question three suspects (can do in any order)
3. **Final Choice** - Open the crate OR chase the sandwich
4. **Ending** - Get one of two different endings based on your choice

## Features

✅ JSON-driven dialogue system (easy to expand)  
✅ Session management (track player progress)  
✅ Analytics endpoints (see game statistics)  
✅ Beautiful UI with animations  
✅ Python Flask backend (simple, clean API)  
✅ React frontend with Vite (fast, modern tooling)  

## Future Enhancements

- 🗄️ Add database persistence (MongoDB/PostgreSQL)
- 🎮 Add more scenes and endings
- 🏆 Add achievement/scoring system
- 🎵 Add sound effects and music
- 👥 Add multiplayer/competitive modes
- 📱 Mobile optimization

## Development Notes

### Adding New Scenes

Edit `frontend/adventure/src/game-data.json`:

```json
"my_new_scene": {
  "id": "my_new_scene",
  "title": "Scene Title",
  "description": "Scene description",
  "narration": "Dialogue text",
  "choices": [
    {
      "id": "choice_1",
      "text": "Button text",
      "next": "next_scene_id"
    }
  ]
}
```

### Testing the Backend

With the Flask server running:
```bash
curl http://localhost:5000/api/health
```

## Troubleshooting

**Frontend can't connect to backend:**
- Make sure Flask is running on `http://localhost:5000`
- Check CORS is enabled in `app.py`
- Look for errors in browser console (F12)

**Python dependency errors:**
- Verify you're in the `/backend` directory
- Run `pip install --upgrade pip`
- Reinstall with: `pip install -r requirements.txt --force-reinstall`

**Frontend won't start:**
- Make sure Node.js 16+ is installed: `node --version`
- Delete `node_modules/` and `package-lock.json`, then `npm install`

## License

Educational project - Use freely!
