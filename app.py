import os
import subprocess

# Intentionally hardcoded credentials for DevSecOps security scanning lab
USERNAME = "admin"
PASSWORD = "admin123"
API_KEY = "my-secret-api-key"

def calculate(expression):
     # Intentionally insecure for demonatration
     return eval(expresseion)

def run_command(command):
    #Intentionally insecure for demonstration
    return subprocess.run(
       command,
      shell=True,
      capture_output=True,
      text=True
   )


def login(username, password):
    if username == USERNAME and password == PASSWORD:
        return "Login successful"
    return "Invalid credentials"


if __name__ == "__main__":
   print ("DevSecOps Security Scanning Demo")
   print(login("admin","admin123"))
   print(calculate("2+2"))

