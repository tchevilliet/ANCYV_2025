import os
import sys
import venv
import subprocess

# Nom de l'environnement virtuel et fichier de dépendances
ENV_DIR = "acv_env"
PACKAGES = [
    "brightway25",
    "pypardiso",
    "notebook",
    "jupyterlab",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
]

def run(cmd):
    print(f"> {cmd}")
    subprocess.check_call(cmd, shell=True)

def main(python_min_version="3.11"):
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

    # Paths
    if os.name == "nt":
        pip_path = os.path.join(ENV_DIR, "Scripts", "pip.exe")
        python_path = os.path.join(ENV_DIR, "Scripts", "python.exe")
        activate_hint = rf"{ENV_DIR}\Scripts\activate"
    else:
        pip_path = os.path.join(ENV_DIR, "bin", "pip")
        python_path = os.path.join(ENV_DIR, "bin", "python")
        activate_hint = f"source {ENV_DIR}/bin/activate"

    # Upgrade pip/setuptools/wheel
    run(f'"{python_path}" -m pip install --upgrade pip setuptools wheel')

    # Install each package individually
    for pkg in PACKAGES:
        print(f"Installing: {pkg}")
        run(f'"{pip_path}" install {pkg}')

    print("Configuration réussie !")
    print("Pour accéder aux notebooks, entrer:")
    if os.name == "nt":
        print(r"  acv_env\Scripts\activate")
    else:
        print("  source acv_env/bin/activate")
    print("  jupyter notebook")

if __name__ == "__main__":
    main()