from pathlib import Path

files_dir = Path('files')

for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()
    new_content = content.replace('amount', 'units')

  with open(filepath, 'w') as file:
    file.write(new_content)
