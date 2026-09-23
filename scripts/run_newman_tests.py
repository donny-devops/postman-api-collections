"""Automated collection runner and validator."""
import json
import os
import sys

def validate_collection(file_path: str) -> bool:
    print(f"Validating collection: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert "info" in data
        assert "schema" in data["info"]
        assert "item" in data
        assert len(data["item"]) > 0
        print(f"  -> Valid! ({len(data['item'])} requests found)")
        return True
    except Exception as e:
        print(f"  -> Invalid collection {file_path}: {e}")
        return False

def validate_environment(file_path: str) -> bool:
    print(f"Validating environment: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert "values" in data
        print(f"  -> Valid! ({len(data['values'])} variables defined)")
        return True
    except Exception as e:
        print(f"  -> Invalid environment {file_path}: {e}")
        return False

def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    success = True

    # Validate all collections
    cols_dir = os.path.join(root, "collections")
    for r, _, files in os.walk(cols_dir):
        for f in files:
            if f.endswith(".json"):
                if not validate_collection(os.path.join(r, f)):
                    success = False

    # Validate all environments
    envs_dir = os.path.join(root, "environments")
    for r, _, files in os.walk(envs_dir):
        for f in files:
            if f.endswith(".json"):
                if not validate_environment(os.path.join(r, f)):
                    success = False

    if not success:
        sys.exit(1)
    print("\nAll Postman collections and environments passed schema validation.")

if __name__ == "__main__":
    main()
