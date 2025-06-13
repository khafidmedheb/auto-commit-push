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

- 🧠 Génération dynamique du message de commit avec un LLM local (`mistral`, `phi`, etc.)
- 🔐 Connexion GitHub via SSH (clé préconfigurée)
- 🧱 Workflow Git complet : `init`, `add`, `commit`, `branch`, `remote`, `push`
- 🤖 Fallback manuel si l'IA échoue à générer un message
- 🧑‍💻 Parfait pour indie devs, agents IA, automatisations intelligentes

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
````

---

## 🚀 Utilisation

```bash
python init_git_testojarvis.py
```

✅ Le script :

* Initialise le dépôt si nécessaire
* Met en scène tous les fichiers (`git add .`)
* Génère un message de commit intelligent (diff → résumé → message)
* Commit + push vers GitHub (branche `main`)
* Configure automatiquement l'origine SSH (`origin`)

---

## ✨ Exemple de commit généré

```bash
✨ Ajout de la configuration automatique du remote SSH GitHub
```

---

## 🧠 Stack Technique

| Technologie      | Rôle                                                       |
| ---------------- | ---------------------------------------------------------- |
| Python           | Script principal et logique Git                            |
| Git              | Initialisation, commit, branche, push                      |
| Langchain        | Orchestration de prompt IA                                 |
| Ollama + Mistral | LLM local pour générer des messages de commit intelligents |
| SSH GitHub       | Connexion sécurisée pour le dépôt distant                  |

---

## 📊 GitHub Stats

<p align="left">
  <img src="https://github-readme-stats.vercel.app/api?username=khafidmedheb&show_icons=true&theme=radical" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=khafidmedheb&layout=compact&theme=radical" alt="Top Languages" />
</p>

---

## 🤝 Contribuer

Tu veux améliorer ce script, ajouter d’autres modèles, ou en faire une action GitHub ? N’hésite pas à ouvrir une PR ou une issue 💡

---

## 🪪 Licence

MIT — libre d'utilisation, merci de créditer l’auteur 🙏

---

## ✍️ Auteur

Développé par [Khalid HAFID-MEDHEB](https://www.linkedin.com/in/khalid-hafid-medheb-40451aa8/)
TestoJarvis · Juin 2025