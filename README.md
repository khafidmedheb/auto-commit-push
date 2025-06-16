## ✅ `README.md` — Format Premium

<!-- BANNER -->
<p align="center">
  <img src="https://readme-hero-stats.vercel.app/api?username=khafidmedheb&title=CommitPush%20%7C%20AI-powered%20Git%20Automation&font=Source+Code+Pro&show=followers,repositories&showIcons=true&iconColor=1f6feb&bgColor=000000&textColor=ffffff&borderColor=1f6feb" alt="CommitPush Banner">
</p>

# 🚀 Enhanced Commit Push Assistant

[![Lang](https://img.shields.io/badge/lang-Python3.8+-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)](#)
[![GitHub last commit](https://img.shields.io/github/last-commit/khafidmedheb/auto-commit-push?style=flat-square)](https://github.com/khafidmedheb/auto-commit-push)
[![Contact](https://img.shields.io/badge/Contact-khafid1506@gmail.com-red?logo=gmail&logoColor=white)](mailto:khafid1506@gmail.com)

> ⚡️ Advanced AI-powered Git automation tool with intelligent commit message generation, pre-commit hooks, and comprehensive repository management via Langchain + Ollama.

---

## 📦 Features

### 🧠 **Smart AI Integration**
- **AI-powered commit messages**: Professional English messages using conventional commit format
- **Contextual analysis**: Analyzes file changes, types, and recent commits for better messages
- **Multiple LLM support**: Compatible with Mistral, CodeLlama, Phi, and other Ollama models
- **Intelligent fallback**: Generates descriptive messages when AI is unavailable

### 🔧 **Pre-commit Hooks & Quality Assurance**
- **Automatic hook installation**: One-command setup for pre-commit validation
- **Large file detection**: Prevents commits of files >10MB with Git LFS suggestions
- **Secret scanning**: Detects potential credentials, tokens, and sensitive data
- **Code quality checks**: Python syntax validation and basic linting
- **Interactive warnings**: User confirmation for suspicious changes

### 📊 **Advanced Repository Analysis**
- **Comprehensive status tracking**: Untracked, modified, staged, deleted, and renamed files
- **Change statistics**: Detailed line additions/deletions and file counts
- **File categorization**: Automatic detection of docs, tests, config, and source code
- **Recent commit context**: Uses commit history to improve message generation

### 🛠️ **Enhanced CLI Interface**
- **Multiple operation modes**: Standard, dry-run, custom message, AI-free
- **Flexible configuration**: Customizable models, branches, and commit formats
- **Interactive feedback**: Real-time status updates and progress indicators
- **Error handling**: Robust error management with helpful diagnostics

---

## 🎯 Prerequisites

- ✅ **Python 3.8+** with pip
- ✅ **Git** installed and configured with user credentials
- ✅ **Ollama** installed and running (`ollama run mistral`)
- ✅ **SSH key** configured for GitHub authentication
- ✅ **GitHub repository** (optional - script can initialize)

---

## 🛠️ Installation

```bash
# Clone the repository
git clone git@github.com:khafidmedheb/auto-commit-push.git
cd auto-commit-push

# Install dependencies (auto-installed if missing)
pip install langchain-ollama

# Make script executable (optional)
chmod +x commit_push.py
```

---

## 🚀 Usage

### Basic Usage
```bash
python commit_push.py
```

### Advanced CLI Options
```bash
# Install pre-commit hooks
python commit_push.py --install-hooks

# Dry run (simulation mode)
python commit_push.py --dry-run

# Custom commit message
python commit_push.py -m "feat(auth): add OAuth integration"

# Skip AI generation
python commit_push.py --no-ai

# Use different Ollama model
python commit_push.py --model codellama

# Combine options
python commit_push.py --dry-run --model phi
```

### 💡 Enhanced Workflow

1. **Repository Analysis**: Comprehensive scan of all file changes and types
2. **Pre-commit Validation**: Automatic security and quality checks
3. **Smart Staging**: Intelligent file staging with conflict detection
4. **AI Message Generation**: Context-aware commit message creation
5. **Conventional Commits**: Professional format with proper typing and scoping
6. **Branch Management**: Automatic main branch configuration
7. **Remote Configuration**: Smart GitHub remote setup
8. **Secure Push**: SSH-based authentication and error handling

### ✨ Usage Examples

**Enhanced AI Message Generation**
```bash
🚀 Enhanced Git Commit Push Assistant
📅 2025-06-16 14:30:25
📊 Changes detected: 3 files, +45 -12 lines
📁 Changes staged
🤖 Generating AI commit message...
✅ Commit message: feat(api): add user authentication endpoint
✅ Commit created: feat(api): add user authentication endpoint
🚀 Pushing to GitHub...
✅ Successfully pushed to GitHub!
```

**Pre-commit Hook Installation**
```bash
python commit_push.py --install-hooks
✅ Pre-commit hooks installed
# Hooks now active for: large files, secrets, code quality
```

**Dry Run Mode**
```bash
python commit_push.py --dry-run
📊 Changes detected: 2 files, +23 -5 lines
DRY RUN: Would stage and commit changes
Files to be added: 2
Generated message would be: docs(readme): update installation guide
```

---

## 🎨 Intelligent Commit Messages

The enhanced script generates professional conventional commit messages:

### Conventional Commit Format
```
type(scope): description

Examples:
feat(auth): add user registration endpoint
fix(api): resolve null pointer in validation
docs(readme): update installation instructions
refactor(utils): simplify error handling logic
```

### Message Types & Emojis

| Type | Emoji | Purpose | Example |
|------|-------|---------|---------|
| `feat` | ✨ | New features | `feat(auth): add OAuth login` |
| `fix` | 🐛 | Bug fixes | `fix(api): handle null responses` |
| `docs` | 📝 | Documentation | `docs(readme): add usage examples` |
| `style` | 🎨 | Code formatting | `style(components): fix indentation` |
| `refactor` | ♻️ | Code restructuring | `refactor(utils): extract helper functions` |
| `perf` | ⚡ | Performance improvements | `perf(db): optimize query performance` |
| `test` | ✅ | Testing | `test(auth): add unit tests` |
| `build` | 🔧 | Build system | `build(deps): update dependencies` |
| `ci` | 👷 | CI/CD | `ci(github): add workflow for testing` |
| `chore` | 🔧 | Maintenance | `chore(config): update eslint rules` |
| `security` | 🔒 | Security fixes | `security(auth): fix token validation` |

---

## 🛡️ Pre-commit Hooks & Security

### Automatic Security Checks

```bash
# Large file detection
❌ Large files detected (>10MB):
./data/large_dataset.csv
Consider using Git LFS for large files.

# Secret scanning
⚠️ Potential secrets detected in staged changes:
api_key = "sk-1234567890abcdef"
Please review before committing.
Continue anyway? (y/N):

# Code quality
🐍 Checking Python code quality...
✅ All Python files passed syntax check
```

### Hook Features
- **File size validation**: Prevents accidentally committing large files
- **Credential detection**: Scans for API keys, passwords, tokens
- **Syntax checking**: Validates Python code before commit
- **Interactive prompts**: User confirmation for warnings
- **Automatic installation**: One-command hook setup

---

## 🧠 AI & Technology Stack

### Core Technologies

| Component | Purpose | Version |
|-----------|---------|---------|
| **Python** | Main scripting language | 3.8+ |
| **Git** | Version control operations | Latest |
| **Langchain** | AI orchestration framework | Latest |
| **Ollama** | Local LLM inference | Latest |
| **SSH** | Secure GitHub authentication | - |

### Supported AI Models

| Model | Strengths | Use Case |
|-------|-----------|----------|
| **mistral** | Balanced performance | General purpose (recommended) |
| **codellama** | Code understanding | Development-focused commits |
| **phi** | Fast inference | Quick commit generation |
| **deepseek-coder** | Code analysis | Complex refactoring commits |
| **llama2** | General purpose | Alternative to Mistral |

### Architecture Components

```python
# Enhanced modular architecture
GitOperations          # Git command management
CommitMessageGenerator # AI-powered message creation
PreCommitHooks        # Security and quality validation
Config                # Centralized configuration
```

---

## 🔧 Configuration & Customization

### Script Configuration

```python
# Configuration in commit_push.py
@dataclass
class Config:
    repo_name: str = "auto-commit-push"
    username: str = "khafidmedheb"
    default_branch: str = "main"
    max_commit_length: int = 72
    use_conventional_commits: bool = True
    ollama_model: str = "mistral"
```

### Environment Variables

```bash
# Optional customization
export OLLAMA_MODEL="codellama"
export GITHUB_USERNAME="your-username"
export GIT_DEFAULT_BRANCH="main"
```

### Custom Configuration File

```json
{
  "repo_name": "my-project",
  "username": "myusername",
  "model": "mistral",
  "max_commit_length": 72,
  "use_conventional_commits": true,
  "pre_commit_hooks": {
    "check_file_size": true,
    "scan_secrets": true,
    "validate_syntax": true
  }
}
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

## 🛡️ Security & Best Practices

### Security Features
- 🔐 **SSH-only authentication**: No tokens or passwords stored
- 🔍 **Pre-commit scanning**: Automatic credential detection
- 📝 **Message validation**: Prevents sensitive data in commit messages
- 🚫 **Large file protection**: Prevents accidental large file commits
- ⚡ **Safe operations**: Dry-run mode for testing changes

### Best Practices
- **Conventional commits**: Professional, standardized commit messages
- **Atomic commits**: Single-purpose commits with clear descriptions
- **Branch protection**: Automatic main branch configuration
- **Error recovery**: Graceful handling of network and authentication issues
- **User feedback**: Clear status messages and progress indicators

---

## 🚀 Advanced Features

### Planned Enhancements

- 🎯 **Multi-platform support**: GitLab, Bitbucket integration
- 📋 **Custom templates**: Project-specific commit message templates
- 🌐 **Web interface**: Browser-based configuration and monitoring
- 📊 **Analytics dashboard**: Commit statistics and patterns
- 🔄 **Workflow integration**: GitHub Actions, CI/CD pipeline support
- 🤖 **Advanced AI**: GPT-4, Claude integration options

### Extensibility

```python
# Plugin system for custom hooks
class CustomPreCommitHook:
    def validate(self, files):
        # Custom validation logic
        pass

# Custom AI providers
class CustomAIProvider:
    def generate_message(self, context):
        # Custom AI integration
        pass
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help improve the project:

### Development Setup
```bash
git clone git@github.com:khafidmedheb/auto-commit-push.git
cd auto-commit-push
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements-dev.txt
```

### Contribution Guidelines
- 🔧 **Code quality**: Follow PEP 8 and include type hints
- ✅ **Testing**: Add tests for new features
- 📝 **Documentation**: Update README and docstrings
- 🎯 **Conventional commits**: Use the format this tool generates!

### Priority Areas
- AI model integrations (OpenAI, Anthropic, Cohere)
- Additional pre-commit hooks (ESLint, Prettier, Black)
- Configuration management improvements
- Cross-platform compatibility testing
- Performance optimizations

---

## 🪪 License

MIT License — Free to use, please credit the author 🙏

---

## ✍️ Author

**Khalid HAFID-MEDHEB**  
Senior AI Developer & Automation Specialist  
📧 [khafid1506@gmail.com](mailto:khafid1506@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/khalid-hafid-medheb-40451aa8/)  
🏢 Kallitests · June 2025

---

## 📚 Resources & Documentation

### Official Documentation
- [Ollama Documentation](https://ollama.com/docs) - Local LLM setup and models
- [Langchain Documentation](https://python.langchain.com/docs/) - AI orchestration framework
- [Conventional Commits](https://www.conventionalcommits.org/) - Commit message standards
- [Pre-commit Hooks Guide](https://pre-commit.com/) - Code quality automation

### Tutorials & Guides
- [Git Best Practices](https://git-scm.com/book) - Official Git documentation
- [GitHub SSH Setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) - SSH key configuration
- [Python Type Hints](https://docs.python.org/3/library/typing.html) - Code quality improvement

### Community & Support
- 💬 **Issues**: [GitHub Issues](https://github.com/khafidmedheb/auto-commit-push/issues)
- 🚀 **Discussions**: [GitHub Discussions](https://github.com/khafidmedheb/auto-commit-push/discussions)  
- 📧 **Direct Contact**: [khafid1506@gmail.com](mailto:khafid1506@gmail.com)

---

<p align="center">
  <i>Built with ❤️ for developers who value automation and code quality</i>
</p>