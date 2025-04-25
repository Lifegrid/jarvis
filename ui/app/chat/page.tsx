'use client'

import { MessageList } from '@/components/MessageList'
import { InputBox } from '@/components/InputBox'
import { useConversationStore } from '@/stores/conversationStore'
import { useSearchParams } from 'next/navigation'
import { useEffect, useState } from 'react'

export default function ChatPage() {
  const searchParams = useSearchParams()
  const forceNew = searchParams.get('new')
  const { activeId, createConversation, loadConversation, messages } = useConversationStore()
  const [initialized, setInitialized] = useState(false)

  useEffect(() => {
    if (!initialized) {
      if (forceNew) {
        createConversation()
      } else if (activeId) {
        loadConversation(activeId)
      }
      setInitialized(true)
    }
  }, [initialized, activeId, forceNew, createConversation, loadConversation])

  return (
    <div className="flex flex-col h-full w-full max-w-4xl mx-auto pt-6 pb-32 px-4">
      <MessageList messages={messages} />
      <InputBox />
    </div>
  )
}
