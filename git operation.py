import os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d")

print("횟수 입력")
num = input()

os.system("git add .")
os.system("git commit -m \"{0} | {1}\"".format(current_time, num))
os.system("git push origin master")


