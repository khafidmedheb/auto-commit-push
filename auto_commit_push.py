#!/usr/bin/env python3
"""
================================================================================
Git Repository Initialization Script for TestoJarvis Playwright Assistant
================================================================================
Modifié pour générer dynamiquement le message de commit à l'aide d'un LLM local

Dépendances :
- pip install langchain openai tiktoken
- Ollama installé avec un modèle : `ollama run mistral`

================================================================================
"""

import os
import subprocess
import sys

# Langchain for AI commit message generation
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# Repository configuration
REPO_NAME = "auto-commit-push"
USERNAME = "khafidmedheb"
REMOTE_URL = f"git@github.com:{USERNAME}/{REPO_NAME}.git"

def run_cmd(cmd, check=True, capture_output=False):
    result = subprocess.run(cmd, shell=True, check=check, text=True, capture_output=capture_output)
    return result.stdout.strip() if capture_output else None

def get_git_diff():
    """
    Récupère le diff des fichiers en staging.
    """
    try:
        return run_cmd("git diff --cached", capture_output=True)
    except subprocess.CalledProcessError:
        return ""

def generate_commit_message_with_ai(diff_text):
    """
    Génère un message de commit via un LLM local avec Langchain (ex: Ollama).
    """
    if not diff_text.strip():
        return "🔧 Update"

    template = PromptTemplate.from_template("""
Tu es un assistant développeur. Résume les modifications ci-dessous dans un message de commit Git très court (max 50 caractères).

Diff :
{diff}

Règles :
- Maximum 50 caractères
- Commence par un emoji (🐛, ✨, 🔧, 🚀)
- Verbe d'action court (Add, Fix, Update, Remove)
- Pas de ponctuation finale

Message court :
""")

    prompt = template.format(diff=diff_text)
    llm = Ollama(model="mistral")  # ⚠️ nécessite que ollama tourne localement
    message = llm.predict(prompt).strip()
    
    # Truncate si trop long
    if len(message) > 50:
        message = message[:47] + "..."
    
    return message

def main():
    
    print("🚀 Initialisation du dépôt Git local...")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.isdir(".git"):
        run_cmd("git init")

    run_cmd("git add .")

    # Génération du commit message
    try:
        diff = get_git_diff()
        commit_message = generate_commit_message_with_ai(diff)
        print(f"🤖 Message généré : {commit_message}")
    except Exception as e:
        print(f"⚠️ Erreur IA : {e}")
        commit_message = "🚀 Auto commit"
        print(f"📝 Message alternatif utilisé : {commit_message}")

    try:
        escaped_message = commit_message.replace('"', '\\"')
        run_cmd(f'git commit -m "{escaped_message}"')
        print(f"✅ Commit créé : {commit_message}")
    except subprocess.CalledProcessError:
        print("⚠️ Aucun changement à commiter.")

    run_cmd("git branch -M main")

    try:
        run_cmd("git remote remove origin")
    except subprocess.CalledProcessError:
        pass

    run_cmd(f"git remote add origin {REMOTE_URL}")
    print(f"🔗 Remote configuré : {REMOTE_URL}")
    run_cmd("git push -u origin main")
    print(f"✅ Projet poussé sur GitHub avec succès !")

if __name__ == "__main__":
    main()