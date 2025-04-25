import '@/styles/globals.css'
import { Sidebar } from '@/components/Sidebar'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Jarvis V∞',
  description: 'Votre assistant personnel intelligent',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body className="flex h-screen bg-gradient-to-br from-black via-gray-900 to-black text-white overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto custom-scrollbar">
          {children}
        </main>
      </body>
    </html>
  )
}
