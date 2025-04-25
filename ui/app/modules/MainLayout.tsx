// modules/MainLayout.tsx

import Link from 'next/link'

export default function MainLayout() {
  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-3xl font-bold mb-8 text-center">Jarvis 🤖</h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Link href="/chat">
            <div className="bg-white p-6 rounded-2xl shadow hover:shadow-lg cursor-pointer">
              <h2 className="text-xl font-semibold mb-2">Assistant</h2>
              <p>Discute avec Jarvis comme sur ChatGPT.</p>
            </div>
          </Link>

          <Link href="/planner">
            <div className="bg-white p-6 rounded-2xl shadow hover:shadow-lg cursor-pointer">
              <h2 className="text-xl font-semibold mb-2">Planificateur</h2>
              <p>Organise ta journée, tes objectifs, ton agenda.</p>
            </div>
          </Link>

          <Link href="/memory">
            <div className="bg-white p-6 rounded-2xl shadow hover:shadow-lg cursor-pointer">
              <h2 className="text-xl font-semibold mb-2">Mémoire</h2>
              <p>Consulte les souvenirs et profils mémorisés.</p>
            </div>
          </Link>

          <Link href="/scraper">
            <div className="bg-white p-6 rounded-2xl shadow hover:shadow-lg cursor-pointer">
              <h2 className="text-xl font-semibold mb-2">Scraper</h2>
              <p>Scraping de sites comme CoinMarketCap, etc.</p>
            </div>
          </Link>

          <Link href="/autonomous">
            <div className="bg-white p-6 rounded-2xl shadow hover:shadow-lg cursor-pointer md:col-span-2">
              <h2 className="text-xl font-semibold mb-2">Mode Autonome</h2>
              <p>Active la boucle d’autonomie (analyse, actions, apprentissage).</p>
            </div>
          </Link>
        </div>
      </div>
    </div>
  )
}
