import subprocess

def inputClear(prompt):
    x = subprocess.call('clear', shell=True)
    userInput = input(prompt)
    return(userInput)
