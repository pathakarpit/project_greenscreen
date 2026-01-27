import streamlit as st
import os
import json

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Project Greenscreen: Autonomous AI Engineer",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- FILE PATHS ---
AGENT_LOGS_FILE = "agent_logs.json"
RAW_LOGS_FILE = "logs.txt"
QUESTION_FILE = "question.md"
SOLUTION_FILE = "solution.py"
EXPLANATION_FILE = "explanation.md"

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { padding-top: 2rem; }
    h1 { color: #2E7D32; }
    .stExpander { border: 1px solid #e0e0e0; border-radius: 5px; }
    .stCodeBlock { border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🟢 Project Greenscreen")
st.markdown("**Autonomous Software Engineering Agent | RAG & Vector Search | Multi-Agent Orchestration**")
st.markdown("---")

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs([
    "🛠️ System Architecture & Logs", 
    "📅 Today's Problem", 
    "💡 Solution & Analysis"
])

# =========================================================
# TAB 1: ARCHITECTURE, TECH STACK & LOGS
# =========================================================
with tab1:
    st.subheader("🚀 System Architecture")
    
    col_desc, col_dia = st.columns([1, 1])
    
    with col_desc:
        st.markdown("""
        ### **How It Works (The "Green Screen" Protocol)**
        This system is a fully autonomous loop running on a local server, triggered daily via **Cron Jobs**.

        #### **1. Automation Layer (Cron)**
        * **Trigger:** A Linux `crontab` schedule executes the pipeline daily at 8:00 AM.
        * **Environment:** Runs inside a dedicated Conda environment.

        #### **2. The Intelligence Layer (RAG & Vector Search)**
        * **Deduplication:** Queries a **PostgreSQL (pgvector)** database using embedding models to skip semantically similar questions solved in the last 30 days.

        #### **3. Multi-Agent Orchestration (CrewAI)**
        * 🕵️ **Researcher:** Scrapes web content (handling 403 blocks).
        * 🏗️ **Architect:** Formats messy HTML into exam-standard questions.
        * 👨‍💻 **Engineer:** Writes optimized O(n) Python code.
        * 🎓 **Professor:** Analyzes time/space complexity.

        #### **4. Persistence (Git)**
        * Commits code and logs to GitHub daily to maintain the contribution graph.
        """)

    with col_dia:
        st.subheader("Data Flow Pipeline")
        st.graphviz_chart("""
            digraph {
                rankdir=TB;
                node [shape=box, style="filled,rounded", fontname="Arial", margin=0.2];
                Cron [label="⏰ Cron Job", fillcolor="#ffe0b2"];
                Orchestrator [label="⚙️ Orchestrator", fillcolor="#bbdefb"];
                Postgres [label="🗄️ Vector DB", fillcolor="#c8e6c9", shape=cylinder];
                Agents [label="🤖 AI Crew", fillcolor="#e1bee7"];
                GitHub [label="☁️ GitHub", fillcolor="#cfd8dc"];

                Cron -> Orchestrator;
                Orchestrator -> Postgres [label="Semantic Check"];
                Orchestrator -> Agents [label="Execute Task"];
                Agents -> GitHub [label="Push Code"];
            }
        """)

    st.markdown("---")
    
    # --- LOGS SECTION ---
    st.subheader("🤖 Agent Execution Trace")
    
    col_logs_header, col_download = st.columns([4, 1])
    with col_logs_header:
        st.info("Below is the structured Chain of Thought from the AI Agents.")
    with col_download:
        # Check for RAW logs (logs.txt) for downloading
        if os.path.exists(RAW_LOGS_FILE):
            with open(RAW_LOGS_FILE, "r") as f:
                st.download_button(
                    label="📥 Raw Logs (.txt)",
                    data=f.read(),
                    file_name="full_execution_log.txt",
                    mime="text/plain"
                )

    # Check for STRUCTURED logs (agent_logs.json) for display
    if os.path.exists(AGENT_LOGS_FILE):
        with open(AGENT_LOGS_FILE, "r") as f:
            try:
                logs = json.load(f)
                for entry in logs:
                    # Create an expander for each agent's action
                    with st.expander(f"**{entry['agent']}** - {entry['task_name']}"):
                        
                        st.caption("**Input Task:**")
                        st.text(entry['full_prompt'])
                        
                        st.markdown("---")
                        
                        st.caption("**Agent Response:**")
                        # Markdown rendering ensures code blocks and headers look good
                        st.markdown(entry['response']) 
            except json.JSONDecodeError:
                st.error("Error reading JSON logs. The file might be corrupted.")
    else:
        st.warning(f"⚠️ Log file `{AGENT_LOGS_FILE}` not found. Please run `main.py` once to generate it.")

# =========================================================
# TAB 2: TODAY'S PROBLEM
# =========================================================
with tab2:
    if os.path.exists(QUESTION_FILE):
        with open(QUESTION_FILE, "r") as f:
            content = f.read()
            st.markdown(content, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No problem file generated today.")

# =========================================================
# TAB 3: SOLUTION & ANALYSIS
# =========================================================
with tab3:
    col_code, col_analysis = st.columns([1, 1])
    
    with col_code:
        st.header("🐍 Solution Code")
        if os.path.exists(SOLUTION_FILE):
            with open(SOLUTION_FILE, "r") as f:
                code_content = f.read()
                st.code(code_content, language="python")
        else:
            st.warning("Solution file missing.")
            
    with col_analysis:
        st.header("🎓 Complexity Analysis")
        if os.path.exists(EXPLANATION_FILE):
            with open(EXPLANATION_FILE, "r") as f:
                expl_content = f.read()
                st.markdown(expl_content)
        else:
            st.warning("Explanation file missing.")