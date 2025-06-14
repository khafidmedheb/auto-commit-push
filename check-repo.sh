#!/bin/bash
# Remplacez par vos vraies informations
git config user.name "Khalid HAFID-MEDHEB"
git config user.email "KHAFID1506@gmail.com"
git remote add origin https://github.com/khafidmedheb/auto-commit-push.git

# Vérification
echo "Configuration Git :"
git config --list | grep user
echo "Remotes :"
git remote -v