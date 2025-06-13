import schedule
import time
import subprocess

def job():
    subprocess.run(["python3", "/ev-odoo/license/main.py"])

# Run the job every minute
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
