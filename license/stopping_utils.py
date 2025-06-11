import subprocess
import os
import signal
import time

LOG_TAG = ">> EXPERTS-VISION LICENSE >>"


def get_listening_pids():
    try:
        output = subprocess.check_output(["lsof", "-t", "-i"]).decode()
        pids = sorted(set(int(pid) for pid in output.strip().split()))
        print(f"{LOG_TAG} Found listening processes PIDs: {str(pids)}")
        return pids
    except subprocess.CalledProcessError:
        return []


def kill_processes_gracefully(pids, grace_seconds=10):
    print(f"{LOG_TAG} Sending SIGTERM to all listening processes ...")
    for pid in pids:
        try:
            os.kill(pid, signal.SIGTERM)
            print(f"{LOG_TAG} SIGTERM sent to process {pid}")
        except ProcessLookupError:
            print(f"Process {pid} already stopped")
        except PermissionError:
            print(f"No permission to kill process {pid}")

    print(f"Waiting {grace_seconds} seconds for processes to shut down gracefully ...")
    time.sleep(grace_seconds)

    remaining_pids = []
    for pid in pids:
        try:
            os.kill(pid, 0)  # Ping the process to check if it is still running
            remaining_pids.append(pid)
        except ProcessLookupError:
            continue
    return remaining_pids


def force_kill(pids):
    print(f"{LOG_TAG} Sending SIGKILL to all remaining listening processes ...")
    for pid in pids:
        try:
            os.kill(pid, signal.SIGKILL)
            print(f"{LOG_TAG} SIGKILL sent to process {pid}")
        except ProcessLookupError:
            print(f"Process {pid} already stopped")
        except PermissionError:
            print(f"No permission to kill process {pid}")


def shutdown():
    print(f"{LOG_TAG} Shutdown network processes including Odoo ...")
    pids = get_listening_pids()
    print(pids)
    # if not pids:
    #     print(f"{LOG_TAG} No processes listening on network ports")
    # else:
    #     remaining = kill_processes_gracefully(pids)
    #     if not remaining:
    #         print(f"{LOG_TAG} All processes terminated gracefully")
    #     else:
    #         force_kill(remaining)
    #         print(f"{LOG_TAG} All processes terminated")
    # print(f"{LOG_TAG} Exit container ...")
    # sys.exit(1)
