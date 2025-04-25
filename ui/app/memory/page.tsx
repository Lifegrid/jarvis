'use client'

import React, { useEffect, useState } from 'react'

export default function MemoryPage() {
  const [bilan, setBilan] = useState<string>('Chargement du bilan...')

  useEffect(() => {
    fetch('http://localhost:8000/bilan')
      .then(res => res.json())
      .then(data => setBilan(data.bilan))
      .catch(() => setBilan("Erreur lors du chargement du bilan."))
  }, [])

  return (
    <div className="p-6 md:p-10 max-w-4xl mx-auto text-white space-y-6">
      <h1 className="text-3xl font-bold glow-text">Mémoire quotidienne</h1>

      <div className="card whitespace-pre-wrap text-sm md:text-base leading-relaxed">
        {bilan}
      </div>
    </div>
  )
}
