import subprocess
import datetime

website = "google.com"
file_name = "ping_log.txt"
#Run ping command(2requests)
result = subprocess.run(["ping","-n","2",website],capture_output=True,text=True)
#for linux/mac
#result = subprocess.run(["ping", "-c", "2", website], capture_output=True, text=True)
#log the file with timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(file_name,"a") as f:
    f.write(f"==Ping Test at {timestamp} == \n")
    if result.returncode == 0:
     f.write(result.stdout)
    else:
       f.write(f"Error {result.stderr}")
print("Ping test logged")
