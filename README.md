# LangChain Job Search Agent

Un agente ReAct costruito con **LangChain** e **TavilySearch**, in grado di cercare offerte di lavoro su LinkedIn
per ruoli che utilizzano LangChain, LangGraph o tecnologie correlate.

## Funzionalità
- Usa `LangChain` con `ChatOpenAI` per ragionamento e generazione.
- Esegue ricerche web tramite `TavilySearch`.
- Restituisce risultati ben strutturati in formato Pydantic.

## Setup

1. Clona il repository:
   ```bash
   git clone https://github.com/tuo-username/langchain_jobs.git
   cd langchain_jobs
   ```

2. Installa le dipendenze (con `uv`):
   ```bash
   uv sync
   ```

   oppure con `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. Crea il file `.env`:
   ```bash
   cp .env.example .env
   ```

   E inserisci le tue chiavi API:
   ```
   OPENAI_API_KEY=...
   TAVILY_API_KEY=...
   ```

4. Esegui:
   ```bash
   uv run linkedin_search.py
   ```

## Output
L’agente stampa in console:
- Una sintesi testuale
- L’elenco delle offerte trovate con titolo, azienda, località e link LinkedIn

---
