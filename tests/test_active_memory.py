from memory_engine.active_memory import save_memory, recall_memory, clear_memory, export_memory

def test_memory():
    print("🧠 Test mémoire active...")

    # Étape 1 : Nettoyer la mémoire existante
    clear_memory()

    # Étape 2 : Enregistrer quelques souvenirs
    save_memory("J'aime les crêpes")
    save_memory("Mon prénom est Jérém")
    save_memory("Jarvis doit être intelligent et utile")

    # Étape 3 : Vérification de récupération
    mem = recall_memory()
    print("📚 Contenu mémoire :")
    for item in mem:
        print(f"  • {item}")

    assert len(mem) == 3

    # Étape 4 : Export
    path = export_memory("tests/memory_dump.txt")
    print(f"💾 Mémoire exportée : {path}")

    # Étape 5 : Nettoyage
    clear_memory()
    assert len(recall_memory()) == 0

if __name__ == "__main__":
    test_memory()
