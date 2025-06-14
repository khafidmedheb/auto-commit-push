#!/usr/bin/env python3
import subprocess
import os
from pathlib import Path

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except:
        return False, "", "Commande échouée"

def diagnose_ssh():
    print("🔍 DIAGNOSTIC SSH GITHUB\n" + "="*50)
    
    # 1. Vérifier les clés SSH
    print("1️⃣ Vérification des clés SSH...")
    ssh_dir = Path.home() / ".ssh"
    
    if not ssh_dir.exists():
        print("❌ Dossier ~/.ssh inexistant")
        return False
    
    keys = list(ssh_dir.glob("id_*"))
    public_keys = [k for k in keys if k.suffix == ".pub"]
    
    if not public_keys:
        print("❌ Aucune clé SSH trouvée")
        return False
    
    print(f"✅ Clés trouvées : {[k.name for k in public_keys]}")
    
    # 2. Test de connexion GitHub
    print("\n2️⃣ Test de connexion GitHub...")
    success, stdout, stderr = run_cmd("ssh -T git@github.com")
    
    if "successfully authenticated" in stdout:
        print("✅ Connexion SSH GitHub réussie")
        username = stdout.split("Hi ")[1].split("!")[0] if "Hi " in stdout else "inconnu"
        print(f"👤 Utilisateur connecté : {username}")
    else:
        print("❌ Échec de connexion SSH")
        print(f"Erreur : {stderr}")
        return False
    
    # 3. Vérifier la configuration Git
    print("\n3️⃣ Configuration Git...")
    success, stdout, stderr = run_cmd("git config --global user.name")
    if success and stdout:
        print(f"✅ Nom utilisateur : {stdout}")
    else:
        print("⚠️ Nom utilisateur Git non configuré")
    
    success, stdout, stderr = run_cmd("git config --global user.email")
    if success and stdout:
        print(f"✅ Email : {stdout}")
    else:
        print("⚠️ Email Git non configuré")
    
    # 4. Vérifier le remote
    print("\n4️⃣ Configuration du remote...")
    success, stdout, stderr = run_cmd("git remote -v")
    if success and stdout:
        print(f"✅ Remotes configurés :\n{stdout}")
    else:
        print("⚠️ Aucun remote configuré")
    
    # 5. Vérifier le statut Git
    print("\n5️⃣ Statut du dépôt...")
    success, stdout, stderr = run_cmd("git status --porcelain")
    if success:
        if stdout:
            print(f"📝 Changements détectés :\n{stdout}")
        else:
            print("✅ Dépôt propre")
    
    return True

def fix_common_issues():
    print("\n🔧 CORRECTIONS AUTOMATIQUES\n" + "="*50)
    
    # Configurer Git si nécessaire
    success, stdout, stderr = run_cmd("git config --global user.name")
    if not success or not stdout:
        print("🔧 Configuration du nom utilisateur...")
        run_cmd('git config --global user.name "khafidmedheb"')
    
    success, stdout, stderr = run_cmd("git config --global user.email")
    if not success or not stdout:
        print("🔧 Configuration de l'email...")
        run_cmd('git config --global user.email "khafid1506@gmail.com"')
    
    # Démarrer l'agent SSH
    print("🔧 Démarrage de l'agent SSH...")
    run_cmd("eval $(ssh-agent -s)")
    
    # Ajouter les clés SSH
    ssh_dir = Path.home() / ".ssh"
    for key_file in ["id_ed25519", "id_rsa"]:
        key_path = ssh_dir / key_file
        if key_path.exists():
            print(f"🔧 Ajout de la clé {key_file}...")
            run_cmd(f"ssh-add ~/.ssh/{key_file}")

if __name__ == "__main__":
    if diagnose_ssh():
        print("\n✅ Diagnostic terminé avec succès!")
        
        choice = input("\n🤔 Voulez-vous appliquer les corrections automatiques ? (o/N): ")
        if choice.lower() in ['o', 'oui', 'y', 'yes']:
            fix_common_issues()
    else:
        print("\n❌ Problèmes détectés. Consultez les solutions ci-dessous.")
        fix_common_issues()