import schedule
import time
import subprocess


def job():
    subprocess.run(["python3", "/ev-odoo/deploy/license-verification/src/main.py"])


# Run the job every minute
schedule.every(6).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
