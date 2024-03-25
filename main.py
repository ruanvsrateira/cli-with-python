import pyfiglet
from time import sleep
from subprocess import Popen

exit_commands = ["quit", "exit", "bye", "goodbye"]

print(pyfiglet.figlet_format("Python Custom CLI"))

while True:
  command = input("\n$(root) ")
  
  if command in exit_commands:
    print(pyfiglet.figlet_format("Good Bye."))
    break
  
  with Popen(command, shell=True) as pop:
    sleep(0.3)   
    continue

