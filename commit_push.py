#!/usr/bin/env python3
"""
================================================================================
Git Repository Initialization Script for TestoJarvis Playwright Assistant
================================================================================
Modifié pour générer dynamiquement le message de commit à l'aide d'un LLM local

Dépendances :
- pip install langchain openai tiktoken
- Ollama installé avec un modèle : `ollama run mistral`
- tests tests balala

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

def check_git_changes():
    """
    Vérifie s'il y a des changements à commiter.
    Retourne True s'il y a des changements, False sinon.
    """
    try:
        # Vérifier les fichiers modifiés, ajoutés ou supprimés
        status = run_cmd("git status --porcelain", capture_output=True)
        return bool(status.strip())
    except subprocess.CalledProcessError:
        return False

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
- La première lettre prend une majuscule.
- Ne pas terminer le sujet par un point.
- Utiliser une même forme verbale pour tous les commits.
- Le message doit expliquer le pourquoi.                                        

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

    # Vérifier s'il y a des changements avant de faire quoi que ce soit
    if not check_git_changes():
        print("ℹ️  Aucun changement détecté dans le dépôt.")
        print("✨ Votre dépôt est déjà à jour !")
        return

    print("📁 Changements détectés, ajout des fichiers...")
    run_cmd("git add .")

    # Génération du commit message seulement s'il y a des changements
    try:
        diff = get_git_diff()
        if not diff.strip():
            print("⚠️ Aucun fichier en staging après git add.")
            return
            
        print("🤖 Génération du message de commit via IA...")
        commit_message = generate_commit_message_with_ai(diff)
        print(f"✅ Message généré : {commit_message}")
    except Exception as e:
        print(f"⚠️ Erreur IA : {e}")
        commit_message = "🚀 Auto commit"
        print(f"📝 Message alternatif utilisé : {commit_message}")

    try:
        escaped_message = commit_message.replace('"', '\\"')
        run_cmd(f'git commit -m "{escaped_message}"')
        print(f"✅ Commit créé : {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Erreur lors du commit : {e}")
        return

    print("🔄 Configuration de la branche principale...")
    run_cmd("git branch -M main")

    try:
        run_cmd("git remote remove origin", check=False)
    except subprocess.CalledProcessError:
        pass

    print("🔗 Configuration du remote GitHub...")
    run_cmd(f"git remote add origin {REMOTE_URL}")
    print(f"📡 Remote configuré : {REMOTE_URL}")
    
    try:
        print("🚀 Push vers GitHub en cours...")
        run_cmd("git push -u origin main")
        print("✅ Projet poussé sur GitHub avec succès !")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du push : {e}")
        print("🔧 Vérifiez votre configuration SSH GitHub.")

if __name__ == "__main__":
    main()