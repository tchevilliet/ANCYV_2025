import os
import sys
import venv
import subprocess

# Nom de l'environnement virtuel et fichier de dépendances
ENV_DIR = "acv_env"
REQ_FILE = "requirements.txt"

def run(cmd):
    print(f"> Running: {cmd}")
    subprocess.check_call(cmd, shell=True)

def main(python_min_version="3.8"):
    # Check Python version
    python_version = int(python_min_version.split('.')[0])
    python_subversion = int(python_min_version.split('.')[1])
    if sys.version_info < (python_version, python_subversion):
        print(f"Python {python_min_version}+ is required !")
        sys.exit(1)

    # Create venv
    if not os.path.exists(ENV_DIR):
        print("Création de l'environnement virtuel...")
        venv.EnvBuilder(with_pip=True).create(ENV_DIR)
    else:
        print("L'environnement virtuel existe déjà !")
    
    # Locate executables
    if os.name == "nt":  # Windows
        pip_path = os.path.join(ENV_DIR, "Scripts", "pip.exe")
        python_path = os.path.join(ENV_DIR, "Scripts", "python.exe")
    else:  # Linux/Mac
        pip_path = os.path.join(ENV_DIR, "bin", "pip")
        python_path = os.path.join(ENV_DIR, "bin", "python")

    # Activate path
    if os.name == "nt":  # Windows
        pip_path = os.path.join(ENV_DIR, "Scripts", "pip.exe")
        python_path = os.path.join(ENV_DIR, "Scripts", "python.exe")
    else:  # Linux/Mac
        pip_path = os.path.join(ENV_DIR, "bin", "pip")
        python_path = os.path.join(ENV_DIR, "bin", "python")

    # Upgrade pip
    run(f"{python_path} -m pip install --upgrade pip")

    # Install requirements
    run(f'"{pip_path}" install -r {REQ_FILE}')

    print("Configuration réussie !")
    print("Pour lancer accéder aux notebooks, entrer:")
    if os.name == "nt":
        print(r"  venv\Scripts\activate")
    else:
        print("  source venv/bin/activate")
    print("  jupyter notebook")

if __name__ == "__main__":
    main()