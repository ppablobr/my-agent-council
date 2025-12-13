import os
import json
import datetime

def get_file_modification_timestamp(filepath):
    """Returns the modification timestamp of a file."""
    if not os.path.exists(filepath):
        return None
    return datetime.datetime.fromtimestamp(os.path.getmtime(filepath))

def generate_plan_md_content(plan_data):
    """Generates markdown content for PLAN.md from plan_data."""
    md_content = "# Project Plan\n\n"
    md_content += "This document outlines the plan for creating a multi-agent system for software development.\n\n"

    for phase in plan_data.get("phases", []):
        md_content += f"## {phase.get('name', 'Unnamed Phase')}\n\n"
        for step in phase.get("steps", []):
            status_marker = "[x]" if step.get("status") == "completed" else "[ ]"
            md_content += f"- {status_marker} {step.get('name', 'Unnamed Step')}\n"
        md_content += "\n"
    return md_content

def check_and_update_plan_md():
    """
    Checks if PLAN.md is outdated compared to plan.json and updates it if necessary.
    """
    plan_json_path = "plan.json"
    plan_md_path = "PLAN.md"

    plan_json_timestamp = get_file_modification_timestamp(plan_json_path)
    plan_md_timestamp = get_file_modification_timestamp(plan_md_path)

    if plan_json_timestamp is None:
        print(f"Error: {plan_json_path} not found. Cannot check plan status.")
        return False

    if plan_md_timestamp is None or plan_json_timestamp > plan_md_timestamp:
        print(f"{plan_md_path} is outdated or does not exist. Regenerating from {plan_json_path}...")
        try:
            with open(plan_json_path, 'r') as f:
                plan_data = json.load(f)
            
            md_content = generate_plan_md_content(plan_data)
            with open(plan_md_path, 'w') as f:
                f.write(md_content)
            print(f"Successfully regenerated {plan_md_path}.")
            return True
        except Exception as e:
            print(f"Error regenerating {plan_md_path}: {e}")
            return False
    else:
        print(f"{plan_md_path} is up-to-date.")
        return True

if __name__ == "__main__":
    check_and_update_plan_md()
