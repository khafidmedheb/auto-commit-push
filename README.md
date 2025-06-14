## ✅ `README.md` — Format Premium

<!-- BANNER -->
<p align="center">
  <img src="https://readme-hero-stats.vercel.app/api?username=khafidmedheb&title=CommitPush%20%7C%20AI-powered%20Git%20Automation&font=Source+Code+Pro&show=followers,repositories&showIcons=true&iconColor=1f6feb&bgColor=000000&textColor=ffffff&borderColor=1f6feb" alt="CommitPush Banner">
</p>

# 🚀 Commit Push Assistant

[![Lang](https://img.shields.io/badge/lang-Python3-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)](#)
[![GitHub last commit](https://img.shields.io/github/last-commit/khafidmedheb/testojarvis-playwright?style=flat-square)](https://github.com/khafidmedheb/testojarvis-playwright)
[![Contact](https://img.shields.io/badge/Contact-khafid1506@gmail.com-red?logo=gmail&logoColor=white)](mailto:khafid1506@gmail.com)

> ⚡️ Script intelligent pour initialiser un dépôt Git local et le pousser automatiquement sur GitHub avec des messages de commit générés par IA locale via Langchain + Ollama.

---

## 📦 Fonctionnalités

- 🧠 **Génération IA intelligente** : Messages de commit générés par LLM local (`mistral`, `phi`, etc.)
- 🔍 **Détection automatique** : Vérification des changements avant traitement
- 📏 **Messages optimisés** : Respect des bonnes pratiques Git (≤ 50 caractères)
- 🔐 **Connexion sécurisée** : GitHub via SSH (clé préconfigurée)  
- 🧱 **Workflow complet** : `init`, `add`, `commit`, `branch`, `remote`, `push`
- 🤖 **Fallback robuste** : Message alternatif si l'IA échoue
- ✨ **Arrêt intelligent** : Pas d'action si aucun changement détecté
- 🧑‍💻 **Dev-friendly** : Parfait pour indie devs, agents IA, automatisations

---

## 🎯 Prérequis

- ✅ Python 3.8+
- ✅ [Git](https://git-scm.com/) installé et configuré
- ✅ [Ollama](https://ollama.com/) installé (`ollama run mistral`)
- ✅ Clé SSH active pour GitHub
- ✅ Dépôt Git existant (initialisé) - *optionnel, le script peut initialiser*

---

## 🛠️ Installation

```bash
git clone git@github.com:khafidmedheb/testojarvis-playwright.git
cd testojarvis-playwright
pip install -r requirements.txt
```

---

## 🚀 Utilisation

```bash
python commit_push.py
```

### 💡 Workflow automatique

1. **Vérification préalable** : Le script vérifie s'il y a des changements à commiter
2. **Arrêt intelligent** : Si aucun changement → message informatif et arrêt propre
3. **Initialisation Git** : Création du dépôt .git si inexistant
4. **Ajout des fichiers** : `git add .` de tous les fichiers modifiés
5. **Génération IA** : Analyse du diff et création d'un message de commit intelligent
6. **Commit automatique** : Création du commit avec le message généré
7. **Configuration branche** : Définition de la branche principale (`main`)
8. **Configuration remote** : Ajout du remote GitHub
9. **Push automatique** : Envoi vers GitHub

### ✨ Exemple d'utilisation

**Cas 1 : Aucun changement détecté**
```bash
🚀 Initialisation du dépôt Git local...
ℹ️  Aucun changement détecté dans le dépôt.
✨ Votre dépôt est déjà à jour !
```

**Cas 2 : Changements détectés et traités**
```bash
🚀 Initialisation du dépôt Git local...
📁 Changements détectés, ajout des fichiers...
🤖 Génération du message de commit via IA...
✅ Message généré : ✨ Add user authentication
✅ Commit créé : ✨ Add user authentication
🔄 Configuration de la branche principale...
🔗 Configuration du remote GitHub...
📡 Remote configuré : git@github.com:khafidmedheb/auto-commit-push.git
🚀 Push vers GitHub en cours...
✅ Projet poussé sur GitHub avec succès !
```

**Cas 3 : Erreur IA avec fallback**
```bash
🚀 Initialisation du dépôt Git local...
📁 Changements détectés, ajout des fichiers...
🤖 Génération du message de commit via IA...
⚠️ Erreur IA : Connection timeout
📝 Message alternatif utilisé : 🚀 Auto commit
✅ Commit créé : 🚀 Auto commit
[...suite du processus...]
```

---

## 🎨 Messages de commit intelligents

Le script génère des messages suivant les conventions Git :

| Emoji | Type | Exemple |
|-------|------|---------|
| ✨ | Nouvelle fonctionnalité | `✨ Add login feature` |
| 🐛 | Correction de bug | `🐛 Fix authentication error` |
| 🔧 | Configuration/maintenance | `🔧 Update config settings` |
| 🚀 | Déploiement/release | `🚀 Deploy v1.2.0` |
| 📝 | Documentation | `📝 Update README` |
| ⚡ | Performance | `⚡ Optimize database queries` |
| 🎨 | Style/format | `🎨 Refactor code structure` |
| 🔒 | Sécurité | `🔒 Fix security vulnerability` |

---

## 🧠 Stack Technique

| Technologie | Rôle |
|-------------|------|
| **Python** | Script principal et logique Git |
| **Git** | Initialisation, commit, branche, push |
| **Langchain** | Orchestration de prompt IA |
| **Ollama + Mistral** | LLM local pour messages intelligents |
| **SSH GitHub** | Connexion sécurisée pour le dépôt distant |
| **Subprocess** | Exécution des commandes Git système |

---

## 🔧 Configuration

### Personnalisation du dépôt

```python
# Repository configuration dans commit_push.py
REPO_NAME = "auto-commit-push"  # Nom du dépôt GitHub
USERNAME = "khafidmedheb"       # Votre nom d'utilisateur GitHub
REMOTE_URL = f"git@github.com:{USERNAME}/{REPO_NAME}.git"
```

### Modèles LLM supportés

- `mistral` (recommandé)
- `phi`
- `llama2`
- `codellama`
- `deepseek-coder`

### Variables d'environnement

```bash
# Optionnel : personnaliser le modèle IA
export OLLAMA_MODEL="mistral"

# Optionnel : configurer votre username GitHub
export GITHUB_USERNAME="votre-username"
```

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=khafidmedheb&show_icons=true&theme=tokyonight&count_private=true&include_all_commits=true&hide_border=true&custom_title=GitHub%20Statistics&disable_animations=false" alt="GitHub Stats" width="48%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=khafidmedheb&layout=compact&theme=tokyonight&langs_count=10&hide_border=true&card_width=320&exclude_repo=khafidmedheb" alt="Top Languages" width="48%" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=khafidmedheb&theme=tokyonight&hide_border=true&stroke=0000&background=0D1117&ring=1F6FEB&fire=1F6FEB&currStreakLabel=FFFFFF&sideNums=FFFFFF&currStreakNum=1F6FEB&dates=70A5FD" alt="GitHub Streak Stats" width="60%" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=khafidmedheb&theme=tokyo-night&bg_color=0D1117&color=1F6FEB&line=1F6FEB&point=FFFFFF&area=true&hide_border=true" alt="Contribution Graph" width="95%" />
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=khafidmedheb&theme=tokyonight" alt="Profile Summary" width="95%" />
</p>

---

## 🛡️ Sécurité et Bonnes Pratiques

- 🔐 **SSH Keys** : Utilise uniquement des clés SSH pour l'authentification GitHub
- 🔍 **Détection intelligente** : Vérification des changements avant traitement
- 📝 **Messages descriptifs** : Génération automatique de messages explicites
- 🚫 **Pas de tokens** : Aucun token ou mot de passe stocké dans le code
- ⚡ **Arrêt propre** : Pas d'action inutile si aucun changement
- 🔧 **Gestion d'erreurs** : Fallback robuste en cas d'échec IA

---

## 🤝 Contribuer

Tu veux améliorer ce script, ajouter d'autres modèles, ou en faire une action GitHub ? N'hésite pas à ouvrir une PR ou une issue 💡

### Idées d'améliorations

- 🎯 Support pour d'autres plateformes Git (GitLab, Bitbucket)
- 🔍 Contrôles qualité pré-commit (linting, tests)
- 📋 Templates de messages personnalisables
- 🌐 Interface web pour configuration
- ✏️ Mode interactif pour éditer les messages IA
- 📊 Statistiques de commits et historique

---

## 🪪 Licence

MIT — libre d'utilisation, merci de créditer l'auteur 🙏

---

## ✍️ Auteur

Développé par [Khalid HAFID-MEDHEB](https://www.linkedin.com/in/khalid-hafid-medheb-40451aa8/)  
Kallitests · Juin 2025

---

## 📚 Ressources

- [Documentation Ollama](https://ollama.com/docs)
- [Guide GitPython](https://gitpython.readthedocs.io/)
- [Langchain Documentation](https://python.langchain.com/docs/)
- [Conventions de commit](https://www.conventionalcommits.org/)