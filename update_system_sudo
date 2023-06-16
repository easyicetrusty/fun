### The getpass module is used to securely prompt for the sudo password without echoing the input. ####
### The sudo_password variable stores the entered sudo password. ####
### The sudo_command variable constructs the complete sudo command with the update command and the sudo password.####
### The subprocess.run function executes the sudo command using the shell and captures the output. ####
### The output is checked to determine if any packages were upgraded, and the update status is set accordingly. ####

import subprocess
import datetime
import getpass

def update_arch_system():
    start_time = datetime.datetime.now()

    # Get the sudo password
    sudo_password = getpass.getpass("Enter the sudo password: ")

    # Construct the sudo command with the update command
    sudo_command = f"echo {sudo_password} | sudo -S pacman -Syu --noconfirm"

    # Run the sudo command
    update_process = subprocess.run(sudo_command, shell=True, capture_output=True, text=True)

    # Check if any packages were upgraded
    if "Packages (including foreign)" in update_process.stdout:
        update_status = "System fully updated"
    else:
        update_status = "No updates available"

    end_time = datetime.datetime.now()
    execution_time = (end_time - start_time).total_seconds()

    print("Date and Time:", end_time)
    print("Execution Time:", execution_time, "seconds")
    print("Update Status:", update_status)

update_arch_system()
