# 🚀 Template de Prompt pour Mise à Jour du Script Commit Push Assistant

## CONTEXTE
Tu es un expert en développement Python et automatisation Git/GitHub. Je vais te fournir mon script `commit_push.py` qui automatise l'initialisation de dépôts Git locaux et leur push sur GitHub avec des messages de commit générés par IA locale (Langchain + Ollama).

**Script actuel :** Commit Push Assistant - Version corrigée
**Fonctionnalités existantes :**
- Initialisation automatique de dépôt Git
- Détection intelligente des changements
- Génération de messages de commit via IA (Ollama + Langchain)
- Push automatique vers GitHub avec gestion SSH/HTTPS
- Gestion d'erreurs et messages informatifs

## OBJECTIFS DE LA MISE À JOUR
Améliore le script selon ces priorités :

### 🎯 PRIORITÉ 1 - Fonctionnalités Core
- [ ] **Robustesse** : Améliorer la gestion d'erreurs et les cas edge
- [ ] **Performance** : Optimiser les commandes Git et les appels IA
- [ ] **Flexibilité** : Rendre le script plus configurable et adaptable

### 🎯 PRIORITÉ 2 - Nouvelles Fonctionnalités
- [ ] **Configuration avancée** : Fichier de config JSON/YAML
- [ ] **Modes opérationnels** : Mode interactif, silent, dry-run
- [ ] **Support multi-dépôts** : Gestion de plusieurs projets
- [ ] **Historique des commits** : Logging et suivi des opérations

### 🎯 PRIORITÉ 3 - Expérience Utilisateur
- [ ] **Interface améliorée** : Meilleurs messages, barre de progression
- [ ] **Validation** : Vérifications pré-commit intelligentes
- [ ] **Customisation** : Templates de messages, règles personnalisées

## INSTRUCTIONS TECHNIQUES

### 📋 CONTRAINTES OBLIGATOIRES
1. **Compatibilité** : Python 3.8+ uniquement
2. **Dépendances** : Minimiser les dépendances externes
3. **Portabilité** : Compatible Windows/macOS/Linux
4. **Sécurité** : Validation des entrées, gestion sécurisée des credentials
5. **Performance** : Temps d'exécution < 30 secondes pour projets standards

### 🔧 STANDARDS DE CODE
- **Style** : Respect PEP 8, type hints obligatoires
- **Documentation** : Docstrings détaillées pour toutes les fonctions
- **Tests** : Code testable avec gestion des mocks
- **Logs** : Système de logging professionnel avec niveaux
- **Structure** : Code modulaire, classes bien définies

### 🤖 OPTIMISATIONS IA
- **Prompts** : Améliorer les prompts pour Ollama (plus précis, contextuels)
- **Fallback** : Système de fallback intelligent si IA indisponible
- **Cache** : Mise en cache des réponses IA similaires
- **Modèles** : Support de différents modèles Ollama

### 🛡️ GESTION D'ERREURS
- **Validation** : Vérifier Git, SSH, permissions avant exécution
- **Recovery** : Mécanismes de récupération en cas d'échec
- **Feedback** : Messages d'erreur explicites avec solutions
- **Rollback** : Possibilité d'annuler les opérations en cours

## SPÉCIFICATIONS FONCTIONNELLES

### 🔄 WORKFLOW AMÉLIORÉ
```
1. Configuration initiale (auto-détection environnement)
2. Validation des prérequis (Git, SSH, Ollama)
3. Analyse intelligente des changements
4. Génération de commit optimisée
5. Push sécurisé avec retry automatique
6. Reporting et logging complets
```

### 📁 ARCHITECTURE SUGGÉRÉE
```python
class GitManager:      # Gestion des opérations Git
class AICommitGen:     # Génération de messages IA  
class ConfigManager:   # Configuration et settings
class ValidationSuite: # Validations et vérifications
class Logger:          # Système de logging avancé
```

### 🎛️ OPTIONS DE CONFIGURATION
- Chemins personnalisés (dépôts, configs)
- Templates de messages de commit
- Règles de validation personnalisées
- Intégration avec différents modèles IA
- Profils utilisateur multiples

## EXEMPLES D'AMÉLIORATIONS ATTENDUES

### 💡 FONCTIONNALITÉS INNOVANTES
- **Auto-détection du type de projet** (web, data, ML, etc.)
- **Messages contextuels** selon les fichiers modifiés
- **Intégration CI/CD** avec hooks pré/post-commit
- **Dashboard simple** pour suivi des commits
- **Synchronisation multi-machines**

### 🔍 OPTIMISATIONS DEMANDÉES
- Réduction du temps d'exécution de 30%
- Cache intelligent pour éviter les appels IA redondants
- Parallélisation des opérations Git quand possible
- Compression et optimisation des diffs analysés

## FORMAT DE RÉPONSE ATTENDU

### 📝 STRUCTURE DE TA RÉPONSE
1. **Résumé des améliorations** (3-5 points clés)
2. **Code mis à jour** (complet et fonctionnel)
3. **Nouvelles fonctionnalités détaillées**
4. **Instructions d'installation/migration**
5. **Exemples d'utilisation avancée**

### ✅ CRITÈRES DE QUALITÉ
- Code production-ready immédiatement utilisable
- Documentation inline complète
- Gestion d'erreurs exhaustive
- Performance mesurables améliorées
- Expérience utilisateur fluide

## QUESTIONS POUR ORIENTATION

Avant de commencer les modifications, réponds à ces questions pour orienter tes améliorations :

1. **Quel aspect du script actuel te semble le plus perfectible ?**
2. **Quelles fonctionnalités modernes ajouterais-tu en priorité ?**
3. **Comment améliorerais-tu l'intégration avec l'IA Ollama ?**
4. **Quelles validations de sécurité supplémentaires proposerais-tu ?**

---

**Note finale :** Je recherche une version professionnelle, robuste et extensible du script, avec une attention particulière à l'expérience utilisateur et à la maintenance à long terme.