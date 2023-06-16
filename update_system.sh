## The update_arch_system() function performs the following steps:
## Records the start time using the date command.
## Updates the system using sudo pacman -Syu --noconfirm.
## Checks the exit code of the update command to determine if it was successful ($? stores the exit code).
## Sets the update_status variable based on the exit code.
## Records the end time, calculates the execution time, and prints the date, execution time, and update status.
## The update_arch_system function is then called to execute the update process.

#!/bin/bash

update_arch_system() {
    start_time=$(date +"%Y-%m-%d %H:%M:%S")

    # Update the system
    sudo pacman -Syu --noconfirm

    # Check if updates were successful
    if [[ $? -eq 0 ]]; then
        update_status="Successfully updated"
    else
        update_status="Update failed"
    fi

    end_time=$(date +"%Y-%m-%d %H:%M:%S")
    execution_time=$(($(date -d "$end_time" +%s) - $(date -d "$start_time" +%s)))

    echo "Date and Time: $end_time"
    echo "Execution Time: $execution_time seconds"
    echo "Update Status: $update_status"
}

update_arch_system
