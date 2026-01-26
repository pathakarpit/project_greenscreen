import sys
import traceback
from dsa_loader import DSALoader
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def log(status, msg):
    icons = {
        "PASS": "✅",
        "FAIL": "❌",
        "INFO": "ℹ️"
    }
    print(f"{icons.get(status, '')} [{status}] {msg}")


EXCEL_PATH = os.getenv("INPUT_EXCEL_PATH")  # <-- adjust path
SHEET_NAME = os.getenv("SHEET_NAME")           # <-- adjust sheet


def test_init():
    log("INFO", "Testing DSALoader initialization")
    try:
        loader = DSALoader(EXCEL_PATH, SHEET_NAME)
        log("PASS", "DSALoader initialized")
        return loader
    except Exception as e:
        log("FAIL", f"Initialization failed: {e}")
        traceback.print_exc()
        sys.exit(1)


def test_load_all_questions(loader):
    log("INFO", "Testing load_all_questions()")
    try:
        loader.load_all_questions()
        if loader.questions_cache:
            log("PASS", f"Loaded {len(loader.questions_cache)} questions")
        else:
            log("FAIL", "No questions loaded")
    except Exception as e:
        log("FAIL", f"load_all_questions failed: {e}")
        traceback.print_exc()


def test_question_structure(loader):
    log("INFO", "Validating question structure")
    required_keys = {"title", "link", "topic", "difficulty", "row"}
    sample = loader.questions_cache[0]

    missing = required_keys - sample.keys()
    if not missing:
        log("PASS", "Question structure is valid")
    else:
        log("FAIL", f"Missing keys: {missing}")


def test_difficulty_values(loader):
    log("INFO", "Validating difficulty mapping")
    allowed = {"Easy", "Medium", "Hard"}

    invalid = [
        q for q in loader.questions_cache
        if q["difficulty"] not in allowed
    ]

    if not invalid:
        log("PASS", "All difficulty values are valid")
    else:
        log("FAIL", f"Invalid difficulty values found: {invalid[:3]}")


def test_get_new_question(loader):
    log("INFO", "Testing get_new_question()")

    completed = {loader.questions_cache[0]["title"]}
    q = loader.get_new_question(completed)

    if q is None:
        log("FAIL", "Expected a new question, got None")
    elif q["title"] in completed:
        log("FAIL", "Returned a completed question")
    else:
        log("PASS", f"Returned new question: {q['title']}")


def test_get_new_question_all_completed(loader):
    log("INFO", "Testing get_new_question() when all completed")

    completed = {q["title"] for q in loader.questions_cache}
    q = loader.get_new_question(completed)

    if q is None:
        log("PASS", "Correctly returned None when all questions completed")
    else:
        log("FAIL", f"Expected None, got {q['title']}")


if __name__ == "__main__":
    print("\n===== DSALoader TEST SUITE =====")
    
    loader = test_init()
    test_load_all_questions(loader)
    test_question_structure(loader)
    test_difficulty_values(loader)
    test_get_new_question(loader)
    test_get_new_question_all_completed(loader)

    print("\n===== ALL TESTS COMPLETED =====")