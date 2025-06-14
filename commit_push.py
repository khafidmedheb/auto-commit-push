#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Commit Push Assistant - Version corrigée
Script intelligent pour initialiser un dépôt Git local et le pousser automatiquement sur GitHub
avec des messages de commit générés par IA locale via Langchain + Ollama.

Auteur: Khalid HAFID-MEDHEB
Date: Juin 2025 test test 1 test 2 test3
"""

import subprocess
import sys
import os
from pathlib import Path

# Configuration du dépôt
REPO_NAME = "auto-commit-push"
USERNAME = "khafidmedheb"
REMOTE_URL = f"git@github.com:{USERNAME}/{REPO_NAME}.git"
# REMOTE_URL = f"https://github.com/{USERNAME}/{REPO_NAME}.git"

def run_command(command, capture_output=True, check=True):
    """Exécute une commande système avec gestion d'erreurs."""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=capture_output, 
            text=True, 
            check=check
        )
        return result.stdout.strip() if capture_output else None
    except subprocess.CalledProcessError as e:
        if capture_output:
            print(f"❌ Erreur lors de l'exécution: {command}")
            print(f"   Code retour: {e.returncode}")
            if e.stderr:
                print(f"   Erreur: {e.stderr}")
        return None

def check_changes():
    """Vérifie s'il y a des changements à commiter."""
    # Vérifier les fichiers non suivis
    untracked = run_command("git ls-files --others --exclude-standard")
    # Vérifier les fichiers modifiés
    modified = run_command("git diff --name-only")
    # Vérifier les fichiers stagés
    staged = run_command("git diff --cached --name-only")
    
    return bool(untracked or modified or staged)

def generate_commit_message():
    """Génère un message de commit intelligent via IA locale."""
    try:
        # Import des nouvelles classes LangChain
        from langchain_ollama import OllamaLLM
        
        # Obtenir le diff des changements
        diff = run_command("git diff --cached --name-only") or run_command("git diff --name-only")
        if not diff:
            diff = run_command("git ls-files --others --exclude-standard")
        
        # Prompt optimisé pour génération de message
        prompt = f"""
Analyse ces changements Git et génère un message de commit concis (max 50 caractères) avec un emoji approprié.

Fichiers modifiés:
{diff}

Règles:
- 1 emoji + description courte en anglais
- Types: ✨ (feat), 🐛 (fix), 📝 (docs), 🔧 (config), ⚡ (perf), 🎨 (style), 🔒 (security)
- Format: "emoji description"
- Exemple: "✨ Add user authentication"

Message de commit:"""

        # Utilisation de la nouvelle API
        llm = OllamaLLM(model="mistral")  # Nouvelle classe sans warning
        message = llm.invoke(prompt).strip()  # Nouvelle méthode invoke
        
        # Nettoyage du message
        if message.startswith('"') and message.endswith('"'):
            message = message[1:-1]
        
        # Validation de la longueur
        if len(message) > 50:
            message = message[:47] + "..."
            
        return message
        
    except ImportError:
        print("⚠️ langchain-ollama non installé. Installation automatique...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "langchain-ollama"])
            print("✅ langchain-ollama installé avec succès!")
            # Retry après installation
            return generate_commit_message()
        except subprocess.CalledProcessError:
            print("❌ Impossible d'installer langchain-ollama")
            return None
            
    except Exception as e:
        print(f"⚠️ Erreur IA : {e}")
        return None

def init_and_push():
    """Workflow principal : init, commit et push."""
    print("🚀 Initialisation du dépôt Git local...")
    
    # Vérifier si c'est un dépôt Git
    if not Path(".git").exists():
        run_command("git init", capture_output=False)
        print("📁 Dépôt Git initialisé")
    
    # Vérifier s'il y a des changements
    if not check_changes():
        print("ℹ️  Aucun changement détecté dans le dépôt.")
        print("✨ Votre dépôt est déjà à jour !")
        return
    
    print("📁 Changements détectés, ajout des fichiers...")
    
    # Ajouter tous les fichiers
    run_command("git add .", capture_output=False)
    
    # Générer le message de commit via IA
    print("🤖 Génération du message de commit via IA...")
    ai_message = generate_commit_message()
    
    # Message de fallback si l'IA échoue
    commit_message = ai_message if ai_message else "🚀 Auto commit"
    
    if ai_message:
        print(f"✅ Message généré : {commit_message}")
    else:
        print(f"📝 Message alternatif utilisé : {commit_message}")
    
    # Créer le commit
    run_command(f'git commit -m "{commit_message}"', capture_output=False)
    print(f"✅ Commit créé : {commit_message}")
    
    # Configuration de la branche principale
    print("🔄 Configuration de la branche principale...")
    run_command("git branch -M main", capture_output=False)
    
    # Ajouter le remote si nécessaire
    print("🔗 Configuration du remote GitHub...")
    existing_remote = run_command("git remote get-url origin")
    
    if not existing_remote:
        run_command(f"git remote add origin {REMOTE_URL}", capture_output=False)
        print(f"📡 Remote configuré : {REMOTE_URL}")
    else:
        print(f"📡 Remote existant : {existing_remote}")
    
    # Push vers GitHub
    print("🚀 Push vers GitHub en cours...")
    push_result = run_command("git push -u origin main", capture_output=True, check=False)

    if push_result is not None or "Everything up-to-date" in str(push_result):
        print("✅ Projet poussé sur GitHub avec succès !")
    else:
        print("⚠️ Erreur lors du push. Vérifiez votre connexion SSH et les permissions du dépôt.")

def main():
    """Point d'entrée principal."""
    try:
        init_and_push()
    except KeyboardInterrupt:
        print("\n⏹️ Opération annulée par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()