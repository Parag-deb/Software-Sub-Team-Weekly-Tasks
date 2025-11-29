import os

project = "ROV_Pro"
folders = [project, f"{project}/logs", f"{project}/reports"]

for f in folders:
    os.makedirs(f, exist_ok=True)

files = [
    "main.py",
    "rov_simulator.py",
    "cli_dashboard.py",
    "mission_analyzer.py"
]

for file in files:
    path = os.path.join(project, file)
    open(path, "a").close()
    print(f"Created → {path}")
    