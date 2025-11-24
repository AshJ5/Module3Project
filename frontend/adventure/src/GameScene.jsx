import React, { useState } from 'react'
import gameData from './game-data.json'
import './GameScene.css'

export default function GameScene() {
  const [sceneId, setSceneId] = useState('opening')
  const [choices, setChoices] = useState([])

  const scene = gameData.scenes[sceneId]
  if (!scene) return <div className="error">Scene not found</div>

  const choose = async (choice) => {
    setChoices(prev => [...prev, choice.id])
  
    try {
      await fetch('http://localhost:8000/api/game/choice', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choiceId: choice.id, sceneId: sceneId, nextSceneId: choice.next })
      })
    } catch (e) {
    
    }
    setSceneId(choice.next)
  }

  return (
    <div className="game">
      <h1>🥪 The Great Sandwich Quest</h1>

      <h2>{scene.title}</h2>
      <p className="desc">{scene.description}</p>

      <div className="narration">
        <p>{scene.narration}</p>
        {scene.narration_continued && <p>{scene.narration_continued}</p>}
      </div>

      <div className="choices">
        {scene.choices && scene.choices.map(c => (
          <button key={c.id} onClick={() => choose(c)}>{c.text}</button>
        ))}
      </div>

      <div className="status">Scene: {sceneId} • Choices: {choices.length}</div>
    </div>
  )
}
