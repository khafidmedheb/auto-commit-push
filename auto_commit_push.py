#!/usr/bin/env python3
"""
🚀 Auto Commit Push Assistant
Script intelligent pour initialiser un dépôt Git local et le pousser sur GitHub
avec un message de commit généré automatiquement par une IA locale.
"""

import os
import subprocess
import sys
from pathlib import Path

try:
    # ✅ Import modernisé pour LangChain 0.3+
    from langchain_ollama import OllamaLLM
except ImportError:
    print("❌ Installation requise: pip install -U langchain-ollama")
    print("📦 Commande: pip install langchain-ollama")
    sys.exit(1)

# 🔧 Configuration du dépôt
REPO_NAME = "auto-commit-push"
USERNAME = "khafidmedheb"
REMOTE_URL = f"git@github.com:{USERNAME}/{REPO_NAME}.git"
BRANCH_NAME = "main"

# 🎨 Emojis pour les types de commits
COMMIT_EMOJIS = {
    'feat': '✨',
    'fix': '🐛', 
    'docs': '📝',
    'style': '💄',
    'refactor': '♻️',
    'test': '✅',
    'chore': '🔧',
    'init': '🚀',
    'update': '⬆️',
    'perf': '⚡'
}

def run_command(command, cwd=None, capture_output=True):
    """Exécute une commande shell avec gestion d'erreurs"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd, 
            capture_output=capture_output,
            text=True,
            check=True
        )
        return result.stdout.strip() if capture_output else ""
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'exécution : {command}")
        print(f"   Code d'erreur : {e.returncode}")
        if e.stderr:
            print(f"   Détails : {e.stderr}")
        return None

def generate_ai_commit_message():
    """Génère un message de commit intelligent via Ollama"""
    try:
        # 📋 Récupération des modifications Git
        git_status = run_command("git status --porcelain")
        git_diff = run_command("git diff --cached --name-only")
        
        if not git_status and not git_diff:
            git_status = run_command("git ls-files")
        
        # 🤖 Prompt optimisé pour l'IA
        prompt = f"""
Analysez les modifications Git suivantes et générez un message de commit court et précis (max 50 caractères).

Fichiers modifiés/ajoutés :
{git_status or git_diff or "Nouveaux fichiers"}

Règles :
- Format : <type>: <description>
- Types : feat, fix, docs, style, refactor, test, chore, init
- Description en anglais, concise et claire
- Sans emoji (sera ajouté automatiquement)
- Exemple : "feat: add user authentication"

Message de commit :"""

        # ✅ Utilisation modernisée de LangChain
        llm = OllamaLLM(model="mistral")
        message = llm.invoke(prompt).strip()
        
        # 🧹 Nettoyage du message
        message = message.replace('"', '').replace("'", '')
        if message.lower().startswith('message de commit'):
            message = message.split(':', 1)[-1].strip()
        
        return message[:50] if len(message) > 50 else message
        
    except Exception as e:
        print(f"⚠️  Erreur IA : {e}")
        return None

def add_emoji_to_commit(message):
    """Ajoute l'emoji approprié au message de commit"""
    message_lower = message.lower()
    
    # 🎯 Détection du type de commit
    for commit_type, emoji in COMMIT_EMOJIS.items():
        if message_lower.startswith(f"{commit_type}:"):
            return f"{emoji} {message[len(commit_type)+1:].strip()}"
    
    # 🎲 Emoji par défaut selon le contenu
    if any(word in message_lower for word in ['add', 'create', 'new']):
        return f"{COMMIT_EMOJIS['feat']} {message}"
    elif any(word in message_lower for word in ['fix', 'bug', 'error']):
        return f"{COMMIT_EMOJIS['fix']} {message}"
    elif any(word in message_lower for word in ['update', 'upgrade']):
        return f"{COMMIT_EMOJIS['update']} {message}"
    elif any(word in message_lower for word in ['doc', 'readme']):
        return f"{COMMIT_EMOJIS['docs']} {message}"
    else:
        return f"{COMMIT_EMOJIS['init']} {message}"

def get_user_commit_message(ai_message):
    """Interface utilisateur pour valider/modifier le message"""
    print(f"\n🤖 Message proposé par l'IA : {ai_message}")
    print("\nOptions:")
    print("  [Entrée] - Accepter le message proposé")
    print("  [Texte]  - Saisir un nouveau message")
    
    user_input = input("Votre choix : ").strip()
    
    if user_input:
        return user_input
    else:
        return ai_message

def init_git_workflow():
    """Workflow complet d'initialisation Git"""
    current_dir = Path.cwd()
    print(f"📁 Répertoire courant : {current_dir}")
    
    # 🚀 Initialisation Git
    print("🚀 Initialisation du dépôt Git local...")
    if not (current_dir / ".git").exists():
        if run_command("git init") is None:
            return False
    
    # 📋 Ajout des fichiers
    print("📋 Ajout des fichiers...")
    if run_command("git add .") is None:
        return False
    
    # 🤖 Génération du message de commit
    ai_message = generate_ai_commit_message()
    
    if ai_message:
        final_message = get_user_commit_message(ai_message)
    else:
        print("⚠️  L'IA n'est pas disponible, saisie manuelle :")
        final_message = input("Message de commit : ").strip()
        if not final_message:
            final_message = "Initial commit"
    
    # 🎨 Ajout de l'emoji
    final_message = add_emoji_to_commit(final_message)
    print(f"✅ Message final : {final_message}")
    
    # 💾 Commit
    commit_cmd = f'git commit -m "{final_message}"'
    if run_command(commit_cmd) is None:
        return False
    print(f"✅ Commit créé : {final_message}")
    
    # 🌿 Création/changement de branche
    current_branch = run_command("git branch --show-current")
    if current_branch != BRANCH_NAME:
        if run_command(f"git checkout -b {BRANCH_NAME}") is None:
            return False
    
    # 🔗 Configuration du remote
    remotes = run_command("git remote")
    if "origin" not in (remotes or ""):
        if run_command(f"git remote add origin {REMOTE_URL}") is None:
            return False
        print(f"🔗 Remote configuré : {REMOTE_URL}")
    
    # 🚀 Push vers GitHub
    push_cmd = f"git push -u origin {BRANCH_NAME}"
    print("🚀 Push vers GitHub...")
    if run_command(push_cmd, capture_output=False) is None:
        return False
    
    print("✅ Projet poussé sur GitHub avec succès !")
    print(f"🌐 URL : https://github.com/{USERNAME}/{REPO_NAME}")
    return True

def main():
    """Fonction principale"""
    print("=" * 50)
    print("🚀 AUTO COMMIT PUSH ASSISTANT")
    print("=" * 50)
    
    # ✅ Vérifications préalables
    if not run_command("git --version"):
        print("❌ Git n'est pas installé ou accessible")
        return
    
    if not run_command("ollama --version"):
        print("⚠️  Ollama non détecté - l'IA ne sera pas disponible")
    
    # 🚀 Lancement du workflow
    if init_git_workflow():
        print("\n🎉 Workflow terminé avec succès !")
    else:
        print("\n❌ Erreur lors du workflow")
        sys.exit(1)

if __name__ == "__main__":
    main()