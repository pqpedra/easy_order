import os

for root, dirs, files in os.walk("."):
    level = root.count(os.sep)
    indent = "    " * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = "    " * (level + 1)
    for f in files:
        print(f"{subindent}{f}")