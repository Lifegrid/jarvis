'use client'

import { useEffect, useRef } from 'react'
import { useConversationStore } from '@/stores/conversationStore'

export const MessageList = () => {
  const { messages } = useConversationStore()
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    // Scroll automatique vers le bas quand un message arrive
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  return (
    <div className="flex flex-col gap-4 overflow-y-auto pb-10">
      {messages.map((message, index) => (
        <div
          key={index}
          className={`flex ${
            message.from === 'user' ? 'justify-end' : 'justify-start'
          }`}
        >
          <div
            className={`max-w-[80%] p-3 rounded-lg ${
              message.from === 'user'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-700 text-white'
            }`}
          >
            {message.text}
          </div>
        </div>
      ))}
      <div ref={bottomRef} />
    </div>
  )
}
