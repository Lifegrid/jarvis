"use client";

import { useState } from "react";

export default function TerminalPage() {
  const [command, setCommand] = useState("");
  const [output, setOutput] = useState<string[]>([]);

  const runCommand = async () => {
    const res = await fetch("http://localhost:8000/terminal/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command }),
    });
    const data = await res.json();
    setOutput((prev) => [...prev, `$ ${command}`, data.output]);
    setCommand("");
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">🖥️ Terminal IA</h2>
      <input
        value={command}
        onChange={(e) => setCommand(e.target.value)}
        placeholder="Tape une commande..."
        className="border px-3 py-2 rounded w-full max-w-xl"
        onKeyDown={(e) => e.key === "Enter" && runCommand()}
      />
      <div className="mt-6 bg-black text-green-400 p-4 rounded font-mono text-sm">
        {output.map((line, i) => (
          <div key={i}>{line}</div>
        ))}
      </div>
    </div>
  );
}
