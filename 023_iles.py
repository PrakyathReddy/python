import os

folder = os.path.expanduser("~/Desktop/python-projects/python")
os.chdir(folder)

# Get all files in folder
files = os.listdir(folder)

for filename in files:
    # Remove first 12 characters (the prefix like "001_001_001_")
    if len(filename) > 12 and os.path.isfile(os.path.join(folder, filename)):
        new_name = filename[12:]  # Remove first 12 chars
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        
        if new_name and new_name != filename:  # Make sure we have a new name
            os.rename(old_path, new_path)
            print(f"✓ {filename} → {new_name}")

print("\nUndo complete!")