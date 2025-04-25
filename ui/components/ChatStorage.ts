export interface ConversationMeta {
    id: string;
    name: string;
    createdAt: string;
  }
  
  export const saveConversation = (id: string, messages: any[]) => {
    localStorage.setItem(`conv_${id}`, JSON.stringify(messages));
  };
  
  export const loadConversation = (id: string): any[] => {
    const data = localStorage.getItem(`conv_${id}`);
    return data ? JSON.parse(data) : [];
  };
  
  export const saveMeta = (meta: ConversationMeta) => {
    const list = listMetadata();
    const exists = list.find((m) => m.id === meta.id);
    if (!exists) list.push(meta);
    else Object.assign(exists, meta);
    localStorage.setItem("conv_meta", JSON.stringify(list));
  };
  
  export const listMetadata = (): ConversationMeta[] => {
    const data = localStorage.getItem("conv_meta");
    return data ? JSON.parse(data) : [];
  };
  
  export const deleteConversation = (id: string) => {
    localStorage.removeItem(`conv_${id}`);
    const list = listMetadata().filter((m) => m.id !== id);
    localStorage.setItem("conv_meta", JSON.stringify(list));
  };
  
  export const duplicateConversation = (id: string) => {
    const base = loadConversation(id);
    const newId = new Date().toISOString();
    saveConversation(newId, base);
    saveMeta({ id: newId, name: "Copie de " + id.slice(11, 16), createdAt: newId });
  };
  