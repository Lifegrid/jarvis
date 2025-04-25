export interface Message {
    text: string;
    from: "user" | "jarvis" | "error" | "web_summary";
    timestamp: string;
    links?: string[];
  }
  