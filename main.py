from time import sleep
from subprocess import Popen

while True:
  command = input("\n$(root) ")
  with Popen(command, shell=True) as pop:
    sleep(0.5)   
    continue

