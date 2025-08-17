# main.py
# Punto di avvio principale per eseguire il task di classificazione.

import os
# CORREZIONE: Usiamo OllamaChat, che è un Chat Model compatibile con i tool-calling agents.
from langchain_community.chat_models import ChatOllama 

import config
from agents.agent_factory import create_agent_executor
from tools.document_tools import (
    list_markdown_files,
    read_file_content,
    create_embeddings,
    cluster_texts
)

def load_prompt_template(filename: str) -> str:
    """Carica un template di prompt da un file markdown."""
    path = os.path.join(config.PROMPTS_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    """
    Funzione principale che orchestra l'esecuzione del task.
    """
    print("--- Avvio del sistema Orion-MD ---")

    # 1. Inizializza il modello come Chat Model
    llm = ChatOllama (model=config.LLM_MODEL)

    # 2. Definisci i tool per il sub-agente di classificazione
    classifier_tools = [
        list_markdown_files,
        read_file_content,
        create_embeddings,
        cluster_texts
    ]

    # 3. Carica il prompt per il sub-agente
    classifier_system_prompt = load_prompt_template("classifier_prompt.md")

    # 4. Crea l'esecutore per il sub-agente di classificazione
    classifier_agent_executor = create_agent_executor(
        llm=llm,
        tools=classifier_tools,
        system_prompt=classifier_system_prompt
    )

    # 5. Esegui il task
    task_input = f"La directory da analizzare è '{config.INPUT_DATA_DIR}'"
    
    print(f"\n--- Invio task all'agente: {task_input} ---\n")
    
    result = classifier_agent_executor.invoke({
        "input": task_input,
        "directory": config.INPUT_DATA_DIR
    })

    print("\n--- Task completato ---")
    print("Risultato finale dall'agente:")
    print(result['output'])

if __name__ == "__main__":
    # Creiamo qualche file di esempio se non esistono
    if not os.path.exists(config.INPUT_DATA_DIR):
        os.makedirs(config.INPUT_DATA_DIR)
        with open(os.path.join(config.INPUT_DATA_DIR, "tech_review.md"), "w") as f:
            f.write("Recensione del nuovo processore M4. Le performance sono incredibili, specialmente per il machine learning.")
        with open(os.path.join(config.INPUT_DATA_DIR, "business_plan.md"), "w") as f:
            f.write("Il nostro piano aziendale per il Q3 prevede un'espansione nel mercato europeo. Target di fatturato: 5 milioni.")
        with open(os.path.join(config.INPUT_DATA_DIR, "cpu_analysis.md"), "w") as f:
            f.write("Analisi comparativa tra CPU Intel e AMD. La nuova architettura Zen 5 mostra un IPC superiore.")
        with open(os.path.join(config.INPUT_DATA_DIR, "market_strategy.md"), "w") as f:
            f.write("La strategia di marketing si focalizzerà sui social media. Budget allocato: 200k. Obiettivo: aumentare la brand awareness.")

    main()
