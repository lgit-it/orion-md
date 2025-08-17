
# main.py
import os
from langchain_community.chat_models import Ollama
import config
from agents.agent_factory import create_agent_executor
from tools.document_tools import list_markdown_files, read_file_content, create_embeddings, cluster_texts

def load_prompt_template(filename: str) -> str:
    path = os.path.join(config.PROMPTS_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    print("--- Avvio del sistema Orion-MD ---")
    llm = Ollama(model=config.LLM_MODEL)
    classifier_tools = [list_markdown_files, read_file_content, create_embeddings, cluster_texts]
    classifier_system_prompt = load_prompt_template("classifier_prompt.md")
    classifier_agent_executor = create_agent_executor(llm=llm, tools=classifier_tools, system_prompt=classifier_system_prompt)
    
    task_input = f"La directory da analizzare è '{config.INPUT_DATA_DIR}'"
    print(f"\n--- Invio task all'agente: {task_input} ---\n")
    
    result = classifier_agent_executor.invoke({"input": task_input, "directory": config.INPUT_DATA_DIR})
    
    print("\n--- Task completato ---")
    print("Risultato finale dall'agente:")
    print(result['output'])

if __name__ == "__main__":
    if not os.path.exists(config.INPUT_DATA_DIR):
        os.makedirs(config.INPUT_DATA_DIR)
        with open(os.path.join(config.INPUT_DATA_DIR, "tech.md"), "w") as f: f.write("Recensione CPU M4.")
        with open(os.path.join(config.INPUT_DATA_DIR, "business.md"), "w") as f: f.write("Piano aziendale Q3.")
        with open(os.path.join(config.INPUT_DATA_DIR, "tech_2.md"), "w") as f: f.write("Analisi GPU Nvidia.")
        with open(os.path.join(config.INPUT_DATA_DIR, "business_2.md"), "w") as f: f.write("Strategia marketing social.")
    main()
