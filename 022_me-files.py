import os

folder = os.path.expanduser("~/Desktop/python-projects/python")
os.chdir(folder)

# Get all files in folder
files = os.listdir(folder)

for filename in files:
    # Check if file starts with numeric prefix (001_, 002_, etc.)
    if filename[0].isdigit() and "_" in filename[:4]:
        # Remove the numeric prefix
        new_name = filename[4:]  # Remove "###_"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        
        if os.path.isfile(old_path):
            os.rename(old_path, new_path)
            print(f"✓ {filename} → {new_name}")

print("\nUndo complete!")