# mon_script.py
import subprocess
import sys

# Vérifiez si le nom du dépôt est passé en argument
if len(sys.argv) == 2:
    repo_name = sys.argv[1]
else:
    # Si le nom du dépôt n'est pas passé en argument, demandez à l'utilisateur de le fournir
    repo_name = input("Veuillez fournir le nom du dépôt : ")

# Exécutez la commande Terraform avec le nom du dépôt en tant que variable
subprocess.run(["terraform", "apply", "-auto-approve", "-var", f"nom_du_repo={repo_name}"])
