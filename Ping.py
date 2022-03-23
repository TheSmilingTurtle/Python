import subprocess

p = subprocess.Popen('ping 192.168.1.1')

p.wait()
print(p.poll())