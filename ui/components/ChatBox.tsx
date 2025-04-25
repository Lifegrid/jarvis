'use client'

import React, { useEffect, useRef } from 'react'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

interface Message {
  from: 'user' | 'jarvis'
  text: string
  timestamp: string
}

interface Props {
  messages: Message[]
}

export default function ChatBox({ messages }: Props) {
  const endRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  return (
    <div className="flex flex-col gap-4 px-4 py-6 overflow-y-auto flex-grow scroll-smooth max-h-full">
      {messages.map((msg, i) => (
        <div
          key={i}
          className={`max-w-2xl px-4 py-3 rounded-xl shadow-lg transition-all duration-300 ${
            msg.from === 'jarvis'
              ? 'self-start bg-white/10 border-l-4 border-jarvis-blue'
              : 'self-end bg-jarvis-dark border-r-4 border-jarvis-neon'
          }`}
        >
          <ReactMarkdown
            children={msg.text}
            remarkPlugins={[remarkGfm]}
            className="prose prose-invert text-sm md:text-base max-w-full"
          />
          <div className="text-xs text-zinc-400 mt-2 text-right">
            {new Date(msg.timestamp).toLocaleTimeString()}
          </div>
        </div>
      ))}
      <div ref={endRef} />
    </div>
  )
}
