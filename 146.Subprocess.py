# Executando comandos terminal
import subprocess

proc = subprocess.run(['ping', '127.0.0.1', '-c', '4'])

print(proc.returncode)
print(proc.stdout)
print(proc.stderr)
print(proc.args)
