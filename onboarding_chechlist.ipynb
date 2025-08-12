# --- Imports ---


from typing import List, Literal
from pydantic import BaseModel, Field
from operator import itemgetter
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from ipywidgets import Dropdown, Text, Button, VBox, HBox, HTML, Checkbox, Textarea, IntProgress, Layout
from IPython.display import display
import json, datetime, os, re

# --- Optional: role+level aware retriever (works even if you don't have 'level' metadata) ---
def build_where_filter(role: str | None, level: str | None, hire_type: str | None, include_level=True, include_hire=False):
    terms = []
    if role:
        terms.append({"dept": {"$in": [role, "all"]}})
    if include_level and level:
        terms.append({"level": {"$in": [level, "all"]}})
    if include_hire and hire_type:
        terms.append({"hire": {"$in": [hire_type, "all"]}})

    if not terms:
        return {}
    if len(terms) == 1:
        return terms[0]
    return {"$and": terms}


def get_retriever(role: str, level: str | None = None, hire_type: str | None = None):
    # dept filter only (safe even if no 'level' metadata exists)
    where = build_where_filter(role, level, hire_type, include_level=True, include_hire=False)
    return vectordb.as_retriever(search_kwargs={"k": 6, "filter": where})


# --- JSON schema for structured checklist (added 'level') ---
class ChecklistItem(BaseModel):
    id: int
    text: str
    owner: str
    due: str

    status: Literal["open","blocked","done"] = "open"

class ManagerChecklist(BaseModel):
    role: str
    level: str
    hire_type: Literal["internal","external"] 
    title: str
    overview: str
    assumptions: List[str] = []
    open_questions: List[str] = []
    checklist: List[ChecklistItem]
    risks: List[str] = []
    dependencies: List[str] = []
    metrics: List[str] = []
    references: List[str] = []

parser = JsonOutputParser(pydantic_object=ManagerChecklist)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an onboarding assistant. Using ONLY the provided context, create a practical checklist "
     "tailored for role '{role}' and seniority '{level}'. If info is missing, use 'assumptions' and "
     "'open_questions'. Output valid JSON matching the schema."),
    ("human",
     "Role: {role}\nSeniority: {level}Hire type: {hire_type}\nTask: {task}\n\nContext:\n{context}\n\n{format_instructions}")
]).partial(format_instructions=parser.get_format_instructions())

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def join_docs(docs):
    return "\n\n---\n\n".join(d.page_content for d in docs)

def build_chain(role: str, level: str, hire_type: str = "external"):
    retriever = get_retriever(role, level, hire_type)
    return (
        {
            "context": itemgetter("task") | retriever | RunnableLambda(join_docs),
            "task": itemgetter("task"),
            "role": itemgetter("role"),
            "level": itemgetter("level"),
            "hire_type": itemgetter("hire_type"),
        }
        | prompt
        | llm
        | parser
    )

# --- Celebration HTML (shows when all items are done) ---
CELEBRATION_HTML = r"""
<style>
  .chk-wrap { position: relative; margin-top: 12px; }
  .chk-banner {
    background: linear-gradient(90deg,#7c3aed,#a78bfa);
    color: white; padding: 14px 16px; border-radius: 14px;
    box-shadow: 0 8px 24px rgba(124,58,237,.25);
    font-weight: 600; text-align: center; letter-spacing: .2px;
  }
  .chk-sub { text-align:center; color:#4b5563; margin-top:6px; }
  .chk-confetti { position: relative; height: 0; }
  .chk-confetti span{
    position:absolute; top:-8vh; font-size: 22px; user-select:none;
    animation: chk-fall 2.8s linear infinite;
  }
  @keyframes chk-fall {
    0% { transform: translateY(0) rotate(0deg); opacity: 0; }
    10% { opacity: 1; }
    100% { transform: translateY(36vh) rotate(360deg); opacity: 0; }
  }
</style>
<div class="chk-wrap">
  <div class="chk-banner">🎉 Congratulations! Everything is done. You crushed it. 🎉</div>
  <div class="chk-sub">+1000 purple points 💜</div>
  <div class="chk-confetti">
    <span style="left:2%; animation-delay:0s">💜</span>
    <span style="left:10%; animation-delay:.15s">✨</span>
    <span style="left:18%; animation-delay:.35s">🎊</span>
    <span style="left:26%; animation-delay:.05s">💫</span>
    <span style="left:34%; animation-delay:.25s">🎉</span>
    <span style="left:42%; animation-delay:.45s">💜</span>
    <span style="left:50%; animation-delay:.1s">✨</span>
    <span style="left:58%; animation-delay:.3s">🎊</span>
    <span style="left:66%; animation-delay:.2s">💫</span>
    <span style="left:74%; animation-delay:.4s">🎉</span>
    <span style="left:82%; animation-delay:.12s">💜</span>
    <span style="left:90%; animation-delay:.28s">✨</span>
  </div>
</div>
"""
# --- Editable checklist renderer (inline edit + add/delete + save/export) ---
out = VBox()  # container your UI already uses

def render_checklist_editor(result: dict, save_path: str | None = None):
    title = result.get("title", "Checklist")
    overview = result.get("overview", "")
    items = result.get("checklist", [])

    header = HTML(f"<h3>{title}</h3><p>{overview}</p>")
    progress = IntProgress(min=0, max=max(1,len(items)),
                           value=sum(1 for it in items if it.get("status")=="done"),
                           layout=Layout(width="50%"))

    celebration = HTML("")  # fills when all complete
    rows = []

    def update_progress():
        done = sum(1 for it in items if it.get("status")=="done")
        progress.value = done
        celebration.value = CELEBRATION_HTML if items and done == len(items) else ""

    # build rows with editable fields
    for it in items:
        cb = Checkbox(value=(it.get("status")=="done"), description="", indent=False)
        txt = Text(value=it["text"], layout=Layout(width="45%"))
        owner = Text(value=it["owner"], layout=Layout(width="15%"))
        due = Text(value=it["due"], layout=Layout(width="13%"))

        del_btn = Button(description="✖", layout=Layout(width="36px"))

        def on_cb(change, item=it):
            item["status"] = "done" if change["new"] else "open"
            update_progress()
        cb.observe(on_cb, names="value")

        def on_txt(change, item=it):
            item["text"] = change["new"]
        txt.observe(on_txt, names="value")

        def on_owner(change, item=it):
            item["owner"] = change["new"]
        owner.observe(on_owner, names="value")

        def on_due(change, item=it):
            item["due"] = change["new"]
        due.observe(on_due, names="value")

        def on_del(_=None, item=it):
            items.remove(item)
            render_checklist_editor(result, save_path)  # re-render
        del_btn.on_click(on_del)

        row = HBox([cb, txt, owner, due, del_btn], layout=Layout(gap="8px"))
        rows.append(row)

    # add-new-item controls
    new_txt = Text(placeholder="New action…", layout=Layout(width="45%"))
    new_owner = Text(placeholder="Owner", layout=Layout(width="15%"))
    new_due = Text(placeholder="Due", layout=Layout(width="13%"))

    add_btn = Button(description="Add item", button_style="info")

    def on_add(_):
        next_id = (max((it["id"] for it in items), default=0) + 1)
        items.append({"id": next_id, "text": new_txt.value or "New item",
                      "owner": new_owner.value or "Manager",
                      "due": new_due.value or "TBD",

                      "status": "open"})
        render_checklist_editor(result, save_path)
    add_btn.on_click(on_add)

    # save/export buttons
    save_btn = Button(description="Save EXCEL", button_style="success")
    export_btn = Button(description="Export (download)", button_style="warning")
    msg = HTML("")

    def default_path():
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        safe = re.sub(r"[^a-zA-Z0-9_-]+","-", result.get("title","checklist"))
        return f"{safe}_{result.get('role','role')}_{result.get('level','level')}_{ts}.xlsx"

    def on_save(_):
        path = save_path or default_path()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        msg.value = f"<b>Saved:</b> {path}"

    def on_export(_):
        # In notebooks, this shows JSON; you can right-click & save if needed
        msg.value = "<pre style='white-space:pre-wrap'>" + \
                    xls.dumps(result, ensure_ascii=False, indent=2) + "</pre>"

    save_btn.on_click(on_save)
    export_btn.on_click(on_export)

    controls = HBox([new_txt, new_owner, new_due, add_btn], layout=Layout(gap="8px"))
    actions = HBox([save_btn, export_btn], layout=Layout(gap="8px"))

    update_progress()
    out.children = [header, progress, VBox(rows, layout=Layout(gap="6px")),
                    controls, actions, msg, celebration]

# --- Role + Level pickers (keep your existing role/task controls; we add 'level') ---
role_dd = Dropdown(options=[("IT","it"),("HR","hr"),("Finance","finance")],
                   value="it", description="Role")
level_dd = Dropdown(options=[("Junior","junior"),("Specialist","specialist"),("Senior","senior")],
                    value="junior", description="Level")
hire_dd  = Dropdown(options=[("External","external"),("Internal","internal")],
                    value="external", description="Hire type")
task_txt = Text(value="Onboard a new employee in the Espoo office (30 days)",
                description="Task", layout=dict(width="80%"))
go = Button(description="Generate Checklist", button_style="primary")

def on_click(_):
    chain = build_chain(role_dd.value, level_dd.value)
    res = chain.invoke({"role": role_dd.value, "level": level_dd.value, "hire_type": hire_dd.value, "task": task_txt.value})

    # Attach references (nice to show provenance)
    docs = get_retriever(role_dd.value, level_dd.value, hire_dd.value).get_relevant_documents(task_txt.value)
    refs = []
    for d in docs:
        s = d.metadata.get("source") or d.metadata.get("url") or d.metadata.get("file_path")
        if s and s not in refs:
            refs.append(s)
    res["references"] = refs

    render_checklist_editor(res, save_path=f"checklist_{res['role']}_{res['level']}_{res['hire_type']}.xlsx")

go.on_click(on_click)
display(VBox([HBox([role_dd, level_dd, hire_dd]), task_txt, go, out]))
