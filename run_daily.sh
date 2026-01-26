#!/bin/bash

# 1. Define paths
PROJECT_DIR="/home/arpit/workspace/project_greenscreen"
# Direct path to the python executable in your 'project_gs' environment
PYTHON_EXEC="/home/arpit/anaconda3/envs/project_gs/bin/python3"
LOG_FILE="$PROJECT_DIR/logs.txt"

# Function to log messages to both console and file
log_message() {
    echo "$1" | tee -a "$LOG_FILE"
}

# Move to Project Directory
cd $PROJECT_DIR || { echo "Directory not found" | tee -a "$LOG_FILE"; exit 1; }

log_message ""
log_message "========================================================"
log_message "--- Starting Daily DSA Task: $(date) ---"
log_message "========================================================"

# 2. Check Environment
log_message "Using Python: $PYTHON_EXEC"

# 3. Run the Main Orchestrator
log_message "🚀 Running main.py..."
# Capture errors and output to log file
$PYTHON_EXEC main.py 2>&1 | tee -a "$LOG_FILE"

# 4. Git Operations
log_message "📦 Pushing changes to GitHub..."

# Add only the output files and logs. 
# We REMOVED questions.db/history.json because data is now in PostgreSQL.
git add solution.py question.txt logs.txt

# Commit
git commit -m "Daily DSA: $(date +'%Y-%m-%d %H:%M')" 2>&1 | tee -a "$LOG_FILE"

# Push
git push origin main 2>&1 | tee -a "$LOG_FILE"

log_message "--- Task Completed Successfully at $(date) ---"