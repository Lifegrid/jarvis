// 'use client' directive pour marquer ce composant comme un Client Component
'use client';

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';

const Sidebar = () => {
  const [conversations, setConversations] = useState<any[]>([]);
  const router = useRouter();

  useEffect(() => {
    // Simuler une récupération des conversations
    const fetchConversations = async () => {
      try {
        const response = await fetch('/api/conversations');
        const data = await response.json();
        setConversations(data.conversations);
      } catch (error) {
        console.error('Erreur lors de la récupération des conversations:', error);
      }
    };

    fetchConversations();
  }, []);

  const handleConversationClick = (conversationId: string) => {
    router.push(`/chat?conversation_id=${conversationId}`);
  };

  return (
    <div className="sidebar">
      <h3>Conversations</h3>
      <ul>
        {conversations.length > 0 ? (
          conversations.map((conversation) => (
            <li key={conversation.id}>
              <button onClick={() => handleConversationClick(conversation.id)}>
                {conversation.title}
              </button>
            </li>
          ))
        ) : (
          <li>Aucune conversation disponible.</li>
        )}
      </ul>
    </div>
  );
};

export default Sidebar;
