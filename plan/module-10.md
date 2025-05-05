# 📘 Module 10: AI Agent Workflows

| Submodule                  | Study | Project | Difficulty |
| -------------------------- | ----- | ------- | ---------- |
| 10.1 Prompt Engineering    | 5h    | 3h      | I          |
| 10.2 Tool-Calling & Agents | 6h    | 3h      | A          |
| 10.3 Retrieval & Indexing  | 6h    | 3h      | A          |

### 10.1 Prompt Engineering

| Item                    | Description                      | Learning Objectives                      | Micro-Project                     | Study | Build | Level |
| ----------------------- | -------------------------------- | ---------------------------------------- | --------------------------------- | ----- | ----- | ----- |
| 10.1.1 Prompt Formats   | Basic structure and system roles | - Use system + user prompts              | Conversational agent with roles   | 2h    | 1h    | I     |
| 10.1.2 Output Control   | Temperature, format instructions | - Control output size, format, structure | CSV report or Markdown summarizer | 2h    | 1h    | I     |
| 10.1.3 Function Binding | Prompt-generated functions       | - Trigger code from model replies        | Prompt-generated calculator       | 1h    | 1h    | I     |

**Branch Project 10.1:** Prompt Lab – A playground to explore persona roles, instruction tuning, and output shaping.

### 10.2 Tool-Calling & Agents

| Item                    | Description                      | Learning Objectives                        | Micro-Project                   | Study | Build | Level |
| ----------------------- | -------------------------------- | ------------------------------------------ | ------------------------------- | ----- | ----- | ----- |
| 10.2.1 Tool Use         | LLM with API call capabilities   | - Map input to action calls                | OpenAI tool-calling weather app | 2h    | 1.5h  | A     |
| 10.2.2 Planning Agents  | Multi-step planning              | - Chain reasoning using intermediate steps | Task planner over calendar API  | 2h    | 1h    | A     |
| 10.2.3 Agent Frameworks | LangChain, Semantic Kernel, etc. | - Setup agent runtimes                     | Scripted LangChain assistant    | 2h    | 0.5h  | A     |

**Branch Project 10.2:** Multi-Agent Assistant – Planner + executor pair to read emails and draft meeting suggestions.

### 10.3 Retrieval & Indexing

| Item                  | Description                    | Learning Objectives                   | Micro-Project                         | Study | Build | Level |
| --------------------- | ------------------------------ | ------------------------------------- | ------------------------------------- | ----- | ----- | ----- |
| 10.3.1 Embeddings     | Text → vector space            | - Generate and store semantic vectors | Embed blog post content in local DB   | 2h    | 1h    | A     |
| 10.3.2 Vector DB      | Search with similarity         | - Query KNN in Pinecone or Chroma     | PDF Q\&A assistant with vector search | 2h    | 1.5h  | A     |
| 10.3.3 RAG Techniques | Combine retrieval + generation | - Integrate context into prompts      | Retrieval-augmented QA bot over docs  | 2h    | 0.5h  | A     |

**Branch Project 10.3:** DocQuery AI – Upload doc + ask questions using embedding search and generation.

**Capstone 10:** AI Agent IDE – A local web app to run agent tools: planner, retriever, document Q\&A, with LangChain or OpenAI tool-calling backend.
