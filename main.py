import subprocess
import logging
import json
import time


def get_blocked():
    with open("BLOCKED.json", "r") as file:
        config = json.load(file)
    return config['BLOCKED_APPLICATIONS'], config['BLOCKED_WEBSITES']


def update_process_list():
    result = subprocess.run(["tasklist"], capture_output=True, text=True)
    lines = result.stdout.splitlines()[3:]
    processes = []

    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            name = parts[0]
            pid = parts[1]
            processes.append({"name": name, "pid": pid})

    return processes


def kill_process(PID, name):
    try:
        subprocess.run(["taskkill", "/PID", str(PID), "/F"])
        logging.info(f"Killed process: {name} (PID {PID})")
    except Exception as e:
        logging.error(f"Error killing {name} (PID {PID}): {e}")


def main():
    # BLOCKED WEBSITES is not implemented yet.
    BLOCKED_APPLICATIONS, BLOCKED_WEBSITES = get_blocked()

    try:
        while True:
            processes = update_process_list()
            for process in processes:
                if process['name'] in BLOCKED_APPLICATIONS:
                    kill_process(process['pid'], process['name'])
                    if process['name'] not in update_process_list():
                        break
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopping...")


"""    
    print("# # #")
    for process in update_process_list():
        print(process)
    print("# # #")
"""


if __name__ == '__main__':
    main()

