import sys
import traceback
from db_manager import DBManager   # adjust import if filename differs


def log(status, msg):
    icon = {
        "PASS": "✅",
        "FAIL": "❌",
        "INFO": "ℹ️"
    }.get(status, "")
    print(f"{icon} [{status}] {msg}")


def test_init():
    log("INFO", "Testing DBManager initialization & table creation")
    try:
        db = DBManager()
        log("PASS", "Database connected and tables initialized")
        return db
    except Exception as e:
        log("FAIL", f"Initialization failed: {e}")
        traceback.print_exc()
        sys.exit(1)


def test_embedding(db):
    log("INFO", "Testing embedding generation")
    emb = db.get_embedding("Binary Search Tree traversal")
    if emb and len(emb) == 4096:
        log("PASS", "Embedding generated (4096 dimensions)")
    else:
        log("FAIL", f"Invalid embedding length: {len(emb) if emb else 0}")


def test_save_question(db):
    log("INFO", "Testing save_question()")

    sample = {
        "title": "Binary Search in Sorted Array",
        "topic": "Binary Search",
        "link": "https://leetcode.com/problems/binary-search/",
        "json_content": {
            "platform": "LeetCode",
            "id": 704
        }
    }

    try:
        db.save_question(sample)
        log("PASS", "Question inserted successfully")
    except Exception as e:
        log("FAIL", f"Insert failed: {e}")
        traceback.print_exc()


def test_get_completed_titles(db):
    log("INFO", "Testing get_completed_titles()")
    titles = db.get_completed_titles()
    if titles:
        log("PASS", f"Retrieved titles: {titles}")
    else:
        log("FAIL", "No titles returned")


def test_reset_db(db):
    log("INFO", "Testing reset_db()")
    db.reset_db()
    titles = db.get_completed_titles()
    if not titles:
        log("PASS", "Database reset successful")
    else:
        log("FAIL", f"Reset failed, titles still exist: {titles}")


def test_close(db):
    log("INFO", "Testing DB close()")
    try:
        db.close()
        log("PASS", "Database connection closed cleanly")
    except Exception as e:
        log("FAIL", f"Close failed: {e}")


if __name__ == "__main__":
    print("\n===== DBManager INTEGRATION TESTS =====")

    db = test_init()
    test_embedding(db)
    test_save_question(db)
    test_get_completed_titles(db)
    test_reset_db(db)
    test_close(db)

    print("\n===== ALL TESTS COMPLETED =====")
