'use client'

import { useState } from 'react'
import { useConversationStore } from '@/stores/conversationStore'
import { nanoid } from 'nanoid'

export const InputBox = () => {
  const [text, setText] = useState('')
  const [loading, setLoading] = useState(false)

  const { activeId, addMessage } = useConversationStore()

  const handleSend = async () => {
    if (!text.trim() || !activeId) return

    const userMessage = {
      id: nanoid(),
      text: text.trim(),
      from: 'user' as const,
      timestamp: new Date().toISOString(),
    }

    // Affiche immédiatement le message utilisateur
    addMessage(activeId, userMessage)
    setText('')
    setLoading(true)

    try {
      const res = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        body: new URLSearchParams({
          message: userMessage.text,
          conversation_id: activeId,
        }),
      })

      const data = await res.json()

      const jarvisMessage = {
        id: nanoid(),
        text: data.reply || "❌ Erreur dans la réponse de Jarvis.",
        from: 'jarvis' as const,
        timestamp: new Date().toISOString(),
      }

      addMessage(activeId, jarvisMessage)
    } catch (err) {
      const errorMessage = {
        id: nanoid(),
        text: "❌ Impossible de contacter Jarvis. (API OFF?)",
        from: 'jarvis' as const,
        timestamp: new Date().toISOString(),
      }
      addMessage(activeId, errorMessage)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="fixed bottom-0 left-0 w-full bg-black border-t border-gray-800 p-4">
      <div className="max-w-4xl mx-auto flex items-center gap-2">
        <input
          className="flex-1 px-4 py-3 rounded-lg bg-gray-800 text-white focus:outline-none"
          placeholder={loading ? "Attente de Jarvis..." : "Écris ton message..."}
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          disabled={loading}
        />
        <button
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg disabled:opacity-50"
          onClick={handleSend}
          disabled={loading}
        >
          {loading ? "..." : "Envoyer"}
        </button>
      </div>
    </div>
  )
}
