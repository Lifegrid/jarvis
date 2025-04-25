"use client";

import { useEffect, useState } from "react";

export default function SecurityScanPage() {
  const [result, setResult] = useState<string[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/security/scan?domain=localhost")
      .then((res) => res.json())
      .then((data) => setResult(data.result))
      .catch(() => setResult(["❌ Erreur lors du scan de sécurité"]));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">🛡️ Analyse de Sécurité</h2>
      <ul className="space-y-2">
        {result.map((r, i) => (
          <li key={i} className="bg-white rounded shadow p-3 text-sm">
            {r}
          </li>
        ))}
      </ul>
    </div>
  );
}

