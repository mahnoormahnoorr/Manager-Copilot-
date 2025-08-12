# Manager_Copilot

An interactive, role-aware onboarding checklist generator. It pulls content from your own webpages, stores it in Chroma (vector DB), and—using a Retrieval-Augmented Generation (RAG) chain—creates a manager-facing checklist you can check off right inside a Jupyter notebook. When everything’s done, you get a tasteful 🎉 completion banner.

## Features ##
1. Role / level aware retrieval (IT, HR, Finance; Junior/Specialist/Senior; hire type).
2. Grounded answers: pulls only from your indexed URLs (no “model memory”).
3. Interactive UI (ipywidgets): checkboxes, live progress, add/edit/remove items.
4. Completion celebration when all tasks are checked off.
5. References: show which URLs informed the checklist.

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

**How to Work with it?**

1) Index your URLs (one-time or when content changes)
Run build_index.py file. Create your Chroma collection. Note the dept tag and urls of your choice.

2) Run the interactive checklist UI
Run onboarding_assistant.py file. Pick a Role, Level, and Hire type, enter a brief Task (e.g., “Onboard a new employee in Espoo (30 days)”), then click Generate Checklist—the app retrieves relevant policy chunks from your Chroma index and uses RAG with OpenAI to produce a role-aware checklist. You’ll get an interactive list you can check off, edit inline, and add/delete items from, with a live progress bar and a small celebration when everything’s complete. Because it’s grounded in your indexed pages, the output reflects your policies—not the model’s guesses.


📝 Acknowledgments

Built with LangChain, Chroma, OpenAI, and ipywidgets.



