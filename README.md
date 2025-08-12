# Manager_Copilot

An interactive, role-aware onboarding checklist generator. It pulls content from your own webpages, stores it in Chroma (vector DB), and—using a Retrieval-Augmented Generation (RAG) chain—creates a manager-facing checklist you can check off right inside a Jupyter notebook. When everything’s done, you get a tasteful 🎉 completion banner.

## Features ##
Role / level aware retrieval (IT, HR, Finance; Junior/Specialist/Senior; hire type).
Grounded answers: pulls only from your indexed URLs (no “model memory”).
Interactive UI (ipywidgets): checkboxes, live progress, add/edit/remove items.
Completion celebration when all tasks are checked off.
References: show which URLs informed the checklist.

**🚀 Prerequisites**

To run this starter code, you will need: 
Python 3.9+
JupyterLab / Notebook
Packages (minimal):

```bash
pip install langchain langchain-community langchain-openai \
           chromadb tiktoken ipywidgets pydantic
```

An OpenAI API key:

```bash
export OPENAI_API_KEY=sk-...
```

If your pages are JS-heavy, also install Playwright and switch the loader:

```bash
pip install playwright && playwright install
```




