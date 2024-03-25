from subprocess import Popen
import sys

folder_names = list(range(0, 500))

def create_folders():
  for fn in folder_names:
    Popen(f"mkdir {fn}", shell=True)

  print("Processo Automatizado Finalizado com Sucesso!")

def remove_folders():
  for fn in folder_names:
    Popen(f"rd {fn}", shell=True)
  print("Processo Automatizado Finalizado com Sucesso!")

match sys.argv[1]:
  case "add":
    create_folders()
  case "del": 
    remove_folders()
