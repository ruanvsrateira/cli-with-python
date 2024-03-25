from subprocess import Popen

folder_names = list(range(0, 500))

def create_folders():
  for fn in folder_names:
    Popen(f"mkdir {fn}", shell=True)

def remove_folders():
  for fn in folder_names:
    Popen(f"rd {fn}", shell=True)

create_folders()