"use client";
import { useState } from "react";

export default function PlannerPage() {
  const [routine, setRoutine] = useState("");

  const fetchPlan = async () => {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: "Planifie ma journée de demain" }),
    });
    const data = await res.json();
    setRoutine(data.response);
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">🗓️ Planificateur Intelligent</h2>
      <button
        onClick={fetchPlan}
        className="px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700"
      >
        Générer une routine personnalisée
      </button>
      {routine && <pre className="mt-4 bg-gray-100 p-4 rounded whitespace-pre-wrap">{routine}</pre>}
    </div>
  );
}
