export function ChatMessage({ text, from, timestamp }: { text: string; from: string; timestamp: string }) {
  const isUser = from === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-2xl px-5 py-3 rounded-2xl shadow-md whitespace-pre-wrap leading-relaxed text-base ${
          isUser ? "bg-blue-600 text-white" : "bg-white dark:bg-zinc-800 text-zinc-900 dark:text-zinc-100"
        }`}
      >
        <div className="text-xs text-right text-zinc-400 mb-1">
          {new Date(timestamp).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
        </div>
        {text}
      </div>
    </div>
  );
}