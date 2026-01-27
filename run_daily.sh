#!/bin/bash

# 1. Define paths
PROJECT_DIR="/home/arpit/workspace/project_greenscreen"
PYTHON_EXEC="/home/arpit/anaconda3/envs/project_gs/bin/python3"
LOG_FILE="$PROJECT_DIR/logs.txt"

# Function to log messages
log_message() {
    echo "$1" | tee -a "$LOG_FILE"
}

# Move to Project Directory
cd $PROJECT_DIR || { echo "Directory not found" | tee -a "$LOG_FILE"; exit 1; }

log_message ""
log_message "========================================================"
log_message "--- Starting Daily DSA Task: $(date) ---"
log_message "========================================================"

log_message "Using Python: $PYTHON_EXEC"

# Run the Main Orchestrator
log_message "🚀 Running main.py..."
$PYTHON_EXEC main.py 2>&1 | tee -a "$LOG_FILE"

# Git Operations
log_message "📦 Pushing changes to GitHub..."

# Add Code, Markdown files, AND the JSON logs for the dashboard
git add solution.py question.md explanation.md agent_logs.json

# Force-add raw text logs if needed
git add -f logs.txt

# Remove legacy file if present
if [ -f "question.txt" ]; then
    git rm --cached question.txt 2>/dev/null || true
    rm question.txt 2>/dev/null || true
fi

# Commit
git commit -m "Daily DSA: $(date +'%Y-%m-%d %H:%M')" 2>&1 | tee -a "$LOG_FILE"

# Push
git push origin main 2>&1 | tee -a "$LOG_FILE"

log_message "--- Task Completed Successfully at $(date) ---"