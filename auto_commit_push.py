#!/usr/bin/env python3
"""
================================================================================
Git Repository Initialization Script for TestoJarvis Playwright Assistant
================================================================================
Modifié pour générer dynamiquement le message de commit à l’aide d’un LLM local

Dépendances :
- pip install langchain openai tiktoken
- Ollama installé avec un modèle : `ollama run mistral`

================================================================================
"""

# TODO

# PROMPT: quels sont les controles qu'on peut mettre dans un commit push classique vers un repo Github. Par exemple, un linter de code qui bloque le push si le code n'est pas propre. 
# Merci.

# RESULTATS:
# Voici les principaux contrôles qu'on peut mettre en place dans un workflow commit/push vers GitHub :

# ## 🔍 Contrôles côté local (Pre-commit hooks)

# ### **Qualité de code**
# - **Linters** : ESLint, Pylint, Flake8, RuboCop, TSLint
# - **Formatters** : Black, Prettier, autopep8, gofmt
# - **Analyseurs statiques** : SonarLint, Bandit (sécurité Python), MyPy (types Python)

# ### **Tests et validation**
# - **Tests unitaires** : Exécution automatique avant commit
# - **Tests de couverture** : Seuil minimum requis
# - **Validation de schémas** : JSON, YAML, XML
# - **Vérification des dépendances** : Vulnérabilités, licences

# ### **Contrôles structurels**
# - **Messages de commit** : Format conventionnel (Conventional Commits)
# - **Taille des fichiers** : Bloquer les gros fichiers binaires
# - **Secrets** : Détection de clés API, mots de passe
# - **Trailing whitespace** : Suppression des espaces en fin de ligne

# ## 🛡️ Contrôles côté GitHub (GitHub Actions/Workflows)

# ### **CI/CD Pipeline**
# - **Build automatique** : Compilation, packaging
# - **Tests d'intégration** : Tests end-to-end
# - **Tests de performance** : Benchmarks
# - **Tests de sécurité** : SAST, DAST, dependency scanning

# ### **Contrôles de branche**
# - **Branch protection rules** : Require PR reviews, status checks
# - **Merge restrictions** : Squash, rebase policies
# - **Required reviewers** : Code owners, équipes spécifiques

# ## 🔧 Outils populaires

# ### **Pre-commit (Python)**
# ```yaml
# repos:
#   - repo: https://github.com/psf/black
#     hooks:
#       - id: black
#   - repo: https://github.com/pycqa/flake8
#     hooks:
#       - id: flake8
# ```

# ### **Husky (JavaScript)**
# ```json
# {
#   "husky": {
#     "hooks": {
#       "pre-commit": "lint-staged",
#       "pre-push": "npm test"
#     }
#   }
# }
# ```

# ### **GitHub Actions exemple**
# ```yaml
# name: Quality Check
# on: [push, pull_request]
# jobs:
#   lint:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v2
#       - name: Run linter
#         run: flake8 .
#       - name: Run tests
#         run: pytest
# ```

# ## ⚠️ Contrôles de sécurité avancés

# - **GitLeaks** : Détection de secrets dans l'historique
# - **Semgrep** : Analyse de sécurité du code
# - **Dependabot** : Mise à jour automatique des dépendances
# - **CodeQL** : Analyse de vulnérabilités GitHub

# Ces contrôles permettent de maintenir une base de code propre, sécurisée et de qualité avant que le code n'atteigne le dépôt principal.

# PROMPT:

# A partir du script .py Python joint, j'envisage de commit push des fichiers sources Cypress (
# .spec.js/.ts, .cy.js/.ts
# .feature + .steps.js/.ts) et Playwright (.spec.js/.ts, .test.js/.ts
# .feature + .steps.js/.ts). Ajoute un contrôle local de qualité de code dans le script joint, pour les cas Cypress et Playwright. Merci.

# RESULTAT: lancer le prompt precedent

# PROMPT: Mets à jour le README joint avec toutes les modifications précédentes dans le script auto_commit_push.py


import os
import subprocess
import sys

# Langchain for AI commit message generation
# from langchain.llms import Ollama
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
        return "🔧 Mise à jour sans modification détectable"

    template = PromptTemplate.from_template("""
Tu es un assistant développeur. Résume les modifications ci-dessous dans un message de commit Git court, clair et utile.

Diff :
{diff}

Règles :
- Ligne unique
- Commence par un emoji (ex: 🐛, ✨, 🔧, 🚀)
- Utilise des verbes d'action (Ajout, Correction, Suppression, Refacto, etc.)
- Pas de termes vagues comme "update"

Message :
""")

    prompt = template.format(diff=diff_text)
    llm = Ollama(model="mistral")  # ⚠️ nécessite que ollama tourne localement
    return llm.predict(prompt).strip()

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
        commit_message = "🚀 Commit auto – fallback"
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
