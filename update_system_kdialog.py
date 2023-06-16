import subprocess
import datetime

def update_arch_system():
    start_time = datetime.datetime.now()

    # Run the update command
    update_process = subprocess.run(['sudo', 'pacman', '-Syu', '--noconfirm'], capture_output=True, text=True)

    # Check if any packages were upgraded
    if "Packages (including foreign)" in update_process.stdout:
        update_status = "System fully updated"
    else:
        update_status = "No updates available"

    end_time = datetime.datetime.now()
    execution_time = (end_time - start_time).total_seconds()

    # Send notification using KDE notification center
    send_notification("Update Arch Script", f"Status: {update_status}\nExecution Time: {execution_time} seconds")

def send_notification(title, message):
    subprocess.run(['kdialog', '--title', title, '--passivepopup', message, '10'])

update_arch_system()

#### In this updated script, the send_notification function uses the kdialog command with the --title option to specify the title of the notification and the --passivepopup option to display the message as a passive popup notification. The 10 argument represents the timeout in seconds for the notification to automatically disappear.

## Make sure you have the kdialog command installed on your KDE desktop environment. You can test it by running kdialog --passivepopup "Test notification" 10 in a terminal.
