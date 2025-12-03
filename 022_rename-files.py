import os
import subprocess

folder = os.path.expanduser("~/Desktop/python-projects/python")
os.chdir(folder)

# Get file list sorted by modification time (oldest first)
result = subprocess.run(
    ["ls", "-lt"],
    capture_output=True,
    text=True,
    cwd=folder
)

files_to_rename = []
for line in result.stdout.split('\n')[1:]:  # Skip 'total' line
    if not line.strip():
        continue
    parts = line.split()
    if len(parts) >= 9:
        filename = parts[-1]
        # Skip directories and __pycache__
        if filename != "__pycache__" and os.path.isfile(os.path.join(folder, filename)):
            files_to_rename.append(filename)

# Reverse to get oldest first
files_to_rename.reverse()

# Rename with numeric prefix
for idx, filename in enumerate(files_to_rename, 1):
    ext = os.path.splitext(filename)[1]
    name = os.path.splitext(filename)[0]
    new_name = f"{idx:03d}_{name}{ext}"
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
    print(f"✓ {filename} → {new_name}")

print(f"\nRenamed {len(files_to_rename)} files")