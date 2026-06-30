from pathlib import Path
import tomlkit as tk

__version__ = "0.1.0"
__project__ = "project-template"
__description__ = "Project Description"
__author__ = "Fyllus"
__email__ = "fylluszophia@proton.me"

def main():
    root_dir = Path(__file__).resolve().parents[2]
    pyproject_path = root_dir / "pyproject.toml"
    print("Project Config: ", pyproject_path)    
    
    if pyproject_path.exists():
        config = tk.parse(pyproject_path.read_text(encoding="utf-8"))
    else:
        config = tk.document()

    if "project" not in config:
        config.add("project", tk.table())  
    
    config["project"]["name"] = __project__
    config["project"]["version"] = __version__
    config["project"]["description"] = __description__

    config["project"]["authors"] = [
            {"name": __author__, "email": __email__}
        ]

    pyproject_path.write_text(tk.dumps(config), encoding="utf-8")

if __name__ == "__main__":
    main()
