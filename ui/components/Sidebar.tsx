'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useConversationStore } from '@/stores/conversationStore'
import { Bot, PlusCircle } from 'lucide-react'
import { cn } from '@/lib/utils'

export const Sidebar = () => {
  const router = useRouter()
  const { conversations, activeId, loadConversation, loadConversations } = useConversationStore()

  useEffect(() => {
    loadConversations()
  }, [])

  const handleNewConversation = () => {
    router.push('/chat?new=true')
  }

  const handleLoadConversation = (id: string) => {
    loadConversation(id)
    router.push('/chat')
  }

  return (
    <aside className="w-64 h-screen bg-[#0d0d0d] border-r border-gray-800 text-white flex flex-col justify-between p-4">
      <div>
        <h1 className="text-2xl font-bold mb-8 text-center">🤖 Jarvis</h1>

        <button
          onClick={handleNewConversation}
          className="flex items-center gap-2 w-full px-4 py-2 mb-4 bg-blue-600 hover:bg-blue-700 rounded-lg transition"
        >
          <PlusCircle className="w-5 h-5" />
          Nouvelle conversation
        </button>

        <nav className="flex flex-col gap-2">
          {conversations.map((conv) => (
            <button
              key={conv.id}
              onClick={() => handleLoadConversation(conv.id)}
              className={cn(
                'flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-gray-700 text-left transition',
                activeId === conv.id ? 'bg-gray-700 font-bold' : ''
              )}
            >
              <Bot className="w-4 h-4" />
              <span className="truncate">{conv.title || 'Sans titre'}</span>
            </button>
          ))}
        </nav>
      </div>

      <div className="text-xs text-center text-gray-500">
        Jarvis V∞ • {new Date().getFullYear()}
      </div>
    </aside>
  )
}
