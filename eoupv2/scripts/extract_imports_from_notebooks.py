
import json
import re
from pathlib import Path

def extract_imports_from_notebooks(notebook_dir="./notebooks"):
    """
    Scan all notebooks and extract package imports.
    
    Args:
        notebook_dir: Directory containing .ipynb files
        
    Returns:
        Set of package names
    """
    imports = set()
    
    for notebook_path in Path(notebook_dir).glob("*.ipynb"):
        try:
            with open(notebook_path, encoding='utf-8') as f:
                notebook = json.load(f)
        except UnicodeDecodeError:
            # Fallback to latin-1 if utf-8 fails
            with open(notebook_path, encoding='latin-1') as f:
                notebook = json.load(f)
        
        # Scan all cells
        for cell in notebook.get("cells", []):
            if cell["cell_type"] != "code":
                continue
            
            source = "".join(cell["source"])
            
            # Find import statements
            import_lines = re.findall(
                r'(?:from|import)\s+([a-zA-Z_][a-zA-Z0-9_.]*)',
                source
            )
            
            for imp in import_lines:
                # Get top-level package name
                package = imp.split('.')[0]
                imports.add(package)
    
    return sorted(imports)

if __name__ == "__main__":
    packages = extract_imports_from_notebooks()
    
    print("Detected packages:")
    for pkg in packages:
        print(f"  - {pkg}")
    
    # Remove standard library modules
    stdlib = {
        'os', 'sys', 'json', 're', 'pathlib', 'urllib', 
        'math', 'datetime', 'collections', 'itertools'
    }
    
    third_party = [p for p in packages if p not in stdlib]
    
    print("\nThird-party packages for setup.py:")
    print(f"install_requires={third_party}")