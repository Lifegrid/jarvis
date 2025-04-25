"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";

export default function WebSearchButton({ onResult }: { onResult: (msg: string) => void }) {
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    const query = prompt("🔍 Que veux-tu que Jarvis cherche sur le web ?");
    if (!query) return;
    setLoading(true);
    try {
      const res = await fetch(`http://localhost:8000/web/research?q=${encodeURIComponent(query)}`);
      const data = await res.json();

      const summary = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: `Résume ces résultats :\n${data.result}` }),
      });
      const final = await summary.json();
      onResult(final.response);
    } catch (e) {
      onResult("❌ Échec de la recherche web.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Button onClick={handleClick} disabled={loading} className="w-full mt-2">
      {loading ? "🔄 Recherche en cours..." : "🌐 Lancer une recherche web"}
    </Button>
  );
}
