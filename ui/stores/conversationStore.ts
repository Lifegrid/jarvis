import { create } from 'zustand'
import axios from 'axios'

interface Message {
  text: string
  from: 'user' | 'jarvis'
  timestamp: string
}

interface Conversation {
  id: string
  title: string
}

interface ConversationStore {
  conversations: Conversation[]
  activeId: string | null
  messages: Message[]
  loadConversations: () => Promise<void>
  loadConversation: (id: string) => Promise<void>
  createConversation: () => void
  setMessages: (messages: Message[]) => void
  addMessage: (conversationId: string, message: Message) => void
}

export const useConversationStore = create<ConversationStore>((set) => ({
  conversations: [],
  activeId: null,
  messages: [],

  loadConversations: async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/conversations')
      const data = res.data.conversations
      set({ conversations: data })
    } catch (error) {
      console.error("Erreur lors du chargement des conversations :", error)
    }
  },

  loadConversation: async (id) => {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/conversation/${id}`)
      const data = res.data.messages
      set({
        activeId: id,
        messages: data,
      })
    } catch (error) {
      console.error("Erreur lors du chargement de la conversation :", error)
    }
  },

  createConversation: () => {
    const newId = Date.now().toString()
    set((state) => ({
      conversations: [
        { id: newId, title: "Nouvelle conversation" },
        ...state.conversations,
      ],
      activeId: newId,
      messages: []
    }))
  },

  setMessages: (messages) => set({ messages }),

  addMessage: (conversationId, message) => {
    set((state) => {
      if (state.activeId !== conversationId) {
        console.warn(`Le message n'a pas pu être ajouté : conversation ID différent.`)
        return state
      }

      return {
        messages: [...state.messages, message]
      }
    })
  }
}))
