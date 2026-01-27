import streamlit as st
import os
import json
import graphviz

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
        * 🕵️ **Agent 1 (Researcher):** Scrapes LeetCode/GeeksForGeeks for new problems.
        * 👨‍💻 **Agent 2 (Solver):** Writes optimized Python code (O(n) complexity).
        * 📦 **Agent 3 (Reviewer):** Formats documentation and handles Git operations.

        #### **4. Persistence (Git)**
        * Commits code and logs to GitHub daily to maintain the contribution graph.
        """)

    with col_dia:
        st.caption("Real-time visualization of the execution pipeline.")
        
        # --- Graphviz Visualization ---
        pipeline = graphviz.Digraph()
        
        # SETTINGS: 
        # rankdir='TB' = Top to Bottom
        # newrank='true' helps align nodes better in some versions
        pipeline.attr(rankdir='TB', size='8,8', bgcolor='white', newrank='true')
        
        # GLOBAL NODE STYLES: 
        # width='2.5' forces all boxes to be the same width, creating a clean column.
        pipeline.attr('node', shape='box', style='filled, rounded', 
                     fontname='Sans-Serif', fontsize='10', height='0.5', width='2.5', fixedsize='true')
        
        # 1. Define Nodes
        pipeline.node('cron', '⏰ Cron Job', fillcolor='#E3F2FD', color='#1E88E5')
        pipeline.node('scanner', '🔍 Scan Questions\n(main.py)', fillcolor='#FFF9C4', color='#FBC02D')
        
        # Decision Node - Diamonds are naturally wider, so we adjust width/height for visual balance
        pipeline.node('db_check', 'Already in DB?', shape='diamond', style='filled', 
                      height='0.8', width='3.0', fixedsize='true', fillcolor='#E1BEE7', color='#8E24AA')
        
        # Action Agents
        pipeline.node('creator', '📝 Create Question', fillcolor='#FFF9C4', color='#FBC02D')
        pipeline.node('solver', '👨‍💻 Generate Solution', fillcolor='#FFF9C4', color='#FBC02D')
        pipeline.node('update_db', '💾 Update Vector DB', shape='cylinder', fillcolor='#E3F2FD', color='#1E88E5')
        pipeline.node('explainer', '🎓 Generate Docs', fillcolor='#FFF9C4', color='#FBC02D')
        pipeline.node('git', '🚀 Push to Git', shape='folder', fillcolor='#E8F5E9', color='#2E7D32')

        # 2. Define Edges (The Flow)
        # Using weight=100 forces these edges to be short and straight (the main backbone)
        pipeline.edge('cron', 'scanner', weight='100')
        pipeline.edge('scanner', 'db_check', weight='100')
        
        # --- THE FIX FOR ALIGNMENT ---
        # constraint='false': Tells graphviz NOT to use this edge for ranking/layout.
        # This prevents the 'Retry' loop from pushing the column sideways.
        pipeline.edge('db_check', 'scanner', label='Yes (Retry)', color='#ef5350', style='dashed', constraint='false')
        
        # Continue backbone
        pipeline.edge('db_check', 'creator', label='No', color='#66bb6a', weight='100')
        pipeline.edge('creator', 'solver', weight='100')
        pipeline.edge('solver', 'update_db', weight='100')
        pipeline.edge('update_db', 'explainer', weight='100')
        pipeline.edge('explainer', 'git', weight='100')

        # Render
        st.graphviz_chart(pipeline, use_container_width=False)

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
                    with st.expander(f"**{entry.get('agent', 'Unknown Agent')}** - {entry.get('task_name', 'Task')}"):
                        
                        st.caption("**Input Task:**")
                        st.text(entry.get('full_prompt', 'No prompt recorded'))
                        
                        st.markdown("---")
                        
                        st.caption("**Agent Response:**")
                        st.markdown(entry.get('response', 'No response recorded')) 
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