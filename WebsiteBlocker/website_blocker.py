import time
from datetime import datetime as dt

# Linux and Mac hosts
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.abola.pt", "abola.pt", "www.record.pt"]

while True:
  if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
    print("Working hours...")
  else:
    print("Fun hours...")
  time.sleep(5)