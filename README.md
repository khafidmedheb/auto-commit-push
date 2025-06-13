## ✅ `README.md` — Format Premium

<!-- BANNER -->
<p align="center">
  <img src="https://readme-hero-stats.vercel.app/api?username=khafidmedheb&title=TestoJarvis%20%7C%20AI-powered%20Git%20Init%20Automation&font=Source+Code+Pro&show=followers,repositories&showIcons=true&iconColor=1f6feb&bgColor=000000&textColor=ffffff&borderColor=1f6feb" alt="TestoJarvis Banner">
</p>

# 🚀 Auto Commit Push Assistant

[![Lang](https://img.shields.io/badge/lang-Python3-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)](#)
[![GitHub last commit](https://img.shields.io/github/last-commit/khafidmedheb/testojarvis-playwright?style=flat-square)](https://github.com/khafidmedheb/testojarvis-playwright)
[![Contact](https://img.shields.io/badge/Contact-khafid1506@gmail.com-red?logo=gmail&logoColor=white)](mailto:khafid1506@gmail.com)

> ⚡️ Script intelligent pour initialiser un dépôt Git local et le pousser sur GitHub avec un message de commit généré automatiquement par une IA locale via Langchain + Ollama.

---

## 📦 Fonctionnalités

- 🧠 **Génération IA intelligente** : Messages de commit générés par LLM local (`mistral`, `phi`, etc.)
- ✏️ **Édition interactive** : Possibilité de modifier manuellement le message proposé par l'IA
- 📏 **Messages optimisés** : Respect des bonnes pratiques Git (≤ 50 caractères)
- 🔐 **Connexion sécurisée** : GitHub via SSH (clé préconfigurée)
- 🧱 **Workflow complet** : `init`, `add`, `commit`, `branch`, `remote`, `push`
- 🤖 **Fallback robuste** : Option manuelle si l'IA échoue
- 🧑‍💻 **Dev-friendly** : Parfait pour indie devs, agents IA, automatisations

---

## 🎯 Prérequis

- ✅ Python 3.8+
- ✅ [Git](https://git-scm.com/) installé et configuré
- ✅ [Ollama](https://ollama.com/) installé (`ollama run mistral`)
- ✅ Clé SSH active pour GitHub

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
python auto_commit_push.py
```

### 💡 Workflow interactif

1. **Génération IA** : Le script analyse les modifications et propose un message
2. **Validation utilisateur** : 
   - `[Entrée]` → Accepter le message proposé
   - `[Texte]` → Saisir un nouveau message personnalisé
3. **Validation automatique** : Ajout d'emoji et limitation à 50 caractères
4. **Commit & Push** : Envoi automatique vers GitHub

### ✨ Exemple d'utilisation

```bash
🚀 Initialisation du dépôt Git local...

🤖 Message proposé par l'IA : ✨ Add user authentication module

Options:
  [Entrée] - Accepter le message proposé
  [Texte]  - Saisir un nouveau message
Votre choix : Fix login bug

✅ Message final : 🔧 Fix login bug
✅ Commit créé : 🔧 Fix login bug
🔗 Remote configuré : git@github.com:khafidmedheb/auto-commit-push.git
✅ Projet poussé sur GitHub avec succès !
```

---

## 🎨 Messages de commit intelligents

Le script génère des messages suivant les conventions Git :

| Emoji | Type | Exemple |
|-------|------|---------|
| ✨ | Nouvelle fonctionnalité | `✨ Add login feature` |
| 🐛 | Correction de bug | `🐛 Fix authentication error` |
| 🔧 | Configuration/maintenance | `🔧 Update config settings` |
| 🚀 | Déploiement/release | `🚀 Initial commit` |
| 📝 | Documentation | `📝 Update README` |
| ⚡ | Performance | `⚡ Optimize database queries` |

---

## 🧠 Stack Technique

| Technologie | Rôle |
|-------------|------|
| **Python** | Script principal et logique Git |
| **Git** | Initialisation, commit, branche, push |
| **Langchain** | Orchestration de prompt IA |
| **Ollama + Mistral** | LLM local pour messages intelligents |
| **SSH GitHub** | Connexion sécurisée pour le dépôt distant |
| **Interface CLI** | Interaction utilisateur en temps réel |

---

## 🔧 Configuration

### Personnalisation du dépôt

```python
# Repository configuration
REPO_NAME = "votre-repo"
USERNAME = "votre-username"
REMOTE_URL = f"git@github.com:{USERNAME}/{REPO_NAME}.git"
```

### Modèles LLM supportés

- `mistral` (recommandé)
- `phi`
- `llama2`
- `codellama`

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=khafidmedheb&show_icons=true&theme=tokyonight&count_private=true&include_all_commits=true&hide_border=true" alt="GitHub Stats" width="48%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=khafidmedheb&layout=compact&theme=tokyonight&langs_count=8&hide_border=true&card_width=320" alt="Top Languages" width="48%" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=khafidmedheb&theme=tokyonight&hide_border=true&stroke=0000&background=0D1117&ring=1F6FEB&fire=1F6FEB&currStreakLabel=FFFFFF" alt="GitHub Streak Stats" width="60%" />
</p>

---

## 🤝 Contribuer

Tu veux améliorer ce script, ajouter d'autres modèles, ou en faire une action GitHub ? N'hésite pas à ouvrir une PR ou une issue 💡

### Idées d'améliorations

- 🎯 Support pour d'autres plateformes Git (GitLab, Bitbucket)
- 🔍 Contrôles qualité pré-commit (linting, tests)
- 📋 Templates de messages personnalisables
- 🌐 Interface web pour configuration

---

## 🪪 Licence

MIT — libre d'utilisation, merci de créditer l'auteur 🙏

---

## ✍️ Auteur

Développé par [Khalid HAFID-MEDHEB](https://www.linkedin.com/in/khalid-hafid-medheb-40451aa8/)  
Kallitests · Juin 2025