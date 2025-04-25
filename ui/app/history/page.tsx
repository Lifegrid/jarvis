"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

export default function HistoryPage() {
  const [sessions, setSessions] = useState<string[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/conversations")
      .then((res) => res.json())
      .then((data) => setSessions(data.names));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-6">🧠 Historique des Conversations</h2>
      <ul className="space-y-3">
        {sessions.map((s, i) => (
          <li key={i} className="bg-white border p-4 rounded shadow flex justify-between">
            <span>{s}</span>
            <Link
              href={`/chat?id=${encodeURIComponent(s)}`}
              className="text-blue-600 hover:underline"
            >
              Reprendre
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
