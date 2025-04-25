"use client";
import { useState } from "react";

export default function TerminalUI() {
  const [command, setCommand] = useState("");
  const [history, setHistory] = useState<{ input: string; output: string; error?: boolean }[]>([]);
  const [loading, setLoading] = useState(false);

  const handleRun = async () => {
    if (!command.trim()) return;
    setLoading(true);
    setHistory((prev) => [...prev, { input: command, output: "...", error: false }]);

    try {
      const res = await fetch("http://localhost:8000/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ command }),
      });
      const data = await res.json();

      const output = data.output || data.error || "(aucune sortie)";
      setHistory((prev) => [
        ...prev.slice(0, -1),
        { input: command, output, error: !!data.error },
      ]);
    } catch (err) {
      setHistory((prev) => [
        ...prev.slice(0, -1),
        { input: command, output: "Erreur réseau", error: true },
      ]);
    } finally {
      setCommand("");
      setLoading(false);
    }
  };

  const handleKey = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") handleRun();
  };

  return (
    <div className="bg-black text-green-400 font-mono h-full p-4 flex flex-col">
      <div className="flex-1 overflow-y-auto space-y-3">
        {history.map((entry, idx) => (
          <div key={idx}>
            <div className="text-blue-400">$ {entry.input}</div>
            <pre className={entry.error ? "text-red-400" : "text-green-300"}>{entry.output}</pre>
          </div>
        ))}
      </div>
      <div className="pt-4 border-t border-green-700 mt-4">
        <input
          className="w-full bg-transparent border-none focus:outline-none text-green-200 placeholder-green-600"
          placeholder="Tapez une commande (ex: ls)"
          value={command}
          onChange={(e) => setCommand(e.target.value)}
          onKeyDown={handleKey}
          disabled={loading}
        />
      </div>
    </div>
  );
}
