# agents/agent_factory.py
# Componente per costruire gli agenti in modo standardizzato.

from typing import List
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import BaseTool

def create_agent_executor(llm: ChatOllama, tools: List[BaseTool], system_prompt: str) -> AgentExecutor:
    """
    Crea un AgentExecutor configurato con un LLM, una lista di tool e un prompt di sistema.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    # --- CORREZIONE ---
    # Associa esplicitamente i tool al modello prima di creare l'agente.
    # Questo è il passaggio chiave che prepara il modello a ricevere e usare gli strumenti.
    llm_with_tools = llm.bind_tools(tools)

    # Passiamo il modello "preparato" (`llm_with_tools`) alla funzione di creazione dell'agente.
    agent = create_tool_calling_agent(llm_with_tools, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )
    return agent_executor
