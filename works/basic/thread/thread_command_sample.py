import threading
import subprocess


def execute_command(command):
    """
    Function to execute a shell command.
    """
    try:
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Output for '{command}':\n{result.stdout}")
        if result.stderr:
            print(f"Error for '{command}':\n{result.stderr}")
    except Exception as e:
        print(f"Error executing command '{command}': {e}")


def main():
    # List of commands to execute
    commands = [
        "sleep 2 && echo 'Hello, World!'",
        "sleep 2 && ls -l",
        "sleep 2 && pwd",
        "sleep 4 && echo 'Finished sleeping'",
    ]

    # Create a thread for each command
    threads = []
    for command in commands:
        thread = threading.Thread(target=execute_command, args=(command,))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All commands executed.")


if __name__ == "__main__":
    main()
