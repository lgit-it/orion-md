# orion-md

progetto di prova di un architettura con subagenti AI per la gestione di file md

Per iniziare a lavorare.

Una volta scaricato il progetto, i passi successivi sono:

1. Installare le dipendenze con: `pip install -r requirements.txt`
2. Scaricare il modello LLM: `ollama pull llama3:8b`
3. Avviare il server dei tool: `uvicorn mcp_server.server:app --reload`
4. In un altro terminal, eseguire il programma principale: `python main.py`
