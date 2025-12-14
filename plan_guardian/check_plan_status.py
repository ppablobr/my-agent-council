import os
import json
import datetime

def get_file_modification_timestamp(filepath):
    """Returns the modification timestamp of a file."""
    if not os.path.exists(filepath):
        return None
    return datetime.datetime.fromtimestamp(os.path.getmtime(filepath))

def generate_plan_md_content(plan_data):
    """Gera o conteúdo Markdown do PLAN.md a partir do plan_data."""
    md_content = "# Plano do projeto\n\n"
    md_content += "Este documento descreve o plano para criar um sistema multiagente para desenvolvimento de software.\n\n"

    for phase in plan_data.get("phases", []):
        md_content += f"## {phase.get('name', 'Fase sem nome')}\n\n"
        for step in phase.get("steps", []):
            status_marker = "[x]" if step.get("status") == "completed" else "[ ]"
            md_content += f"- {status_marker} {step.get('name', 'Passo sem nome')}\n"
        md_content += "\n"
    return md_content

def check_and_update_plan_md():
    """
    Verifica se PLAN.md está desatualizado em relação ao plan.json e atualiza se necessário.
    """
    plan_json_path = "plan.json"
    plan_md_path = "PLAN.md"

    plan_json_timestamp = get_file_modification_timestamp(plan_json_path)
    plan_md_timestamp = get_file_modification_timestamp(plan_md_path)

    if plan_json_timestamp is None:
        print(f"Erro: {plan_json_path} não encontrado. Não foi possível verificar o status do plano.")
        return False

    if plan_md_timestamp is None or plan_json_timestamp > plan_md_timestamp:
        print(f"{plan_md_path} está desatualizado ou não existe. Regenerando a partir de {plan_json_path}...")
        try:
            with open(plan_json_path, 'r') as f:
                plan_data = json.load(f)
            
            md_content = generate_plan_md_content(plan_data)
            with open(plan_md_path, 'w') as f:
                f.write(md_content)
            print(f"{plan_md_path} regenerado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao regenerar {plan_md_path}: {e}")
            return False
    else:
        print(f"{plan_md_path} está atualizado.")
        return True

if __name__ == "__main__":
    check_and_update_plan_md()
