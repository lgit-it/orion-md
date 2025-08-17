# **Struttura del Progetto Orion-MD**

Per mantenere il progetto organizzato, scalabile e facile da manutenere, ho definito la seguente struttura di file e cartelle. Ogni parte ha uno scopo preciso, dalla gestione dei prompt alla logica degli agenti.

/orion-md  
|  
|-- agents/  
|   |-- \_\_init\_\_.py  
|   |-- agent\_factory.py      \# Funzione per creare e assemblare gli agenti  
|  
|-- prompts/  
|   |-- orchestrator\_prompt.md  \# Prompt per l'agente principale (orchestratore)  
|   |-- classifier\_prompt.md    \# Prompt per il sub-agente di classificazione  
|  
|-- tools/  
|   |-- \_\_init\_\_.py  
|   |-- document\_tools.py     \# Strumenti per manipolare file e analizzare testi  
|  
|-- mcp\_server/  
|   |-- server.py             \# Server FastAPI che espone i tool come API  
|  
|-- data/  
|   |-- input\_markdown/       \# Qui vanno i file .md da analizzare  
|   |   |-- doc1.md  
|   |   |-- doc2.md  
|   |-- rag\_storage/          \# Database vettoriale (ChromaDB) per il RAG  
|  
|-- rag/  
|   |-- setup\_rag.py          \# Script per inizializzare e popolare il RAG  
|  
|-- main.py                   \# Punto di avvio principale dell'applicazione  
|-- config.py                 \# Impostazioni globali (nomi dei modelli, percorsi, etc.)  
|-- requirements.txt          \# Elenco delle dipendenze Python

Questa organizzazione separa chiaramente la logica (agents), i dati (data), le istruzioni (prompts) e gli strumenti (tools), rendendo il sistema più robusto.
