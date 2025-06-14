#!/usr/bin/env python3
"""
Script de commit push auto pour projets Cypress/Playwright
- Commit intelligent via ChatGPT
"""

import os
import subprocess
import shlex
import sys

# Langchain pour ChatGPT
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Config
REPO_NAME = "auto-commit-push"
USERNAME = "khafidmedheb"
REMOTE_URL = f"git@github.com:{USERNAME}/{REPO_NAME}.git"

# Configuration de l'API OpenAI
os.environ["OPENAI_API_KEY"] = "sk-proj-..."  # À remplacer par votre clé API

def run_cmd(cmd, capture_output=False):
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=capture_output,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )
    return result.stdout.strip() if capture_output else None

def check_git_status():
    try:
        status_output = run_cmd("git status --porcelain", capture_output=True)
        return bool(status_output.strip())
    except subprocess.CalledProcessError:
        return False

def get_git_diff():
    try:
        return run_cmd("git diff --cached", capture_output=True)
    except subprocess.CalledProcessError:
        return ""

def get_staged_files():
    output = run_cmd("git diff --name-only --cached", capture_output=True)
    return output.splitlines()

def generate_commit_message_with_ai(diff_text):
    if not diff_text.strip():
        return "🔧 Mise à jour sans modification détectable"
    
    system_message = """Tu es un assistant développeur. Résume les modifications dans un message de commit Git court, clair et utile.
Règles :
- Ligne unique
- Commence par un emoji (ex: 🐛, ✨, 🔧, 🚀)
- Utilise des verbes d'action (Ajout, Correction, Refacto, etc.)
- Pas de termes vagues comme "update"
"""
    
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"Voici les modifications à résumer :\n{diff_text}"}
    ]
    response = llm.invoke(messages)
    return response.content.strip()

def commit_push():
    if not check_git_status():
        print("📭 Aucun changement détecté.")
        return

    # Ajouter tous les fichiers modifiés
    print("📥 Ajout des fichiers modifiés...")
    run_cmd("git add .")

    # Partie linter temporairement désactivée
    # if not run_linter_on_staged_files():
    #     sys.exit(1)

    diff_text = get_git_diff()
    commit_msg = generate_commit_message_with_ai(diff_text)

    run_cmd(f'git commit -m "{commit_msg}"')
    run_cmd("git push origin main")
    print(f"🚀 Commit & Push : {commit_msg}")

if __name__ == "__main__":
    commit_push()
