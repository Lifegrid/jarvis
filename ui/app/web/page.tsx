"use client";

import { useEffect, useState } from "react";

export default function WebScanPage() {
  const [result, setResult] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/web/scan")
      .then((res) => res.json())
      .then((data) => setResult(data.result))
      .catch(() => setResult("❌ Erreur lors de l'analyse web"));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">🌐 Analyse Web</h2>
      <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap text-sm">
        {result || "Chargement..."}
      </pre>
    </div>
  );
}
