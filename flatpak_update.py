import subprocess
import datetime

def update_flatpak_packages():
    start_time = datetime.datetime.now()

    # Update Flatpak repositories
    subprocess.run(["flatpak", "update", "-y"], check=True)

    # Check if any Flatpak packages are outdated
    result = subprocess.run(["flatpak", "update", "-p", "-l"], capture_output=True, text=True)
    output = result.stdout.strip()

    if not output:
        # All packages are up to date
        print("\n - All Flatpak packages are up to date\n")
    else:
        # Some packages are outdated
        print("\n - Not all Flatpak packages are up to date\n")

    end_time = datetime.datetime.now()
    execution_time = end_time - start_time
    print("Date and Time:", end_time)
    print("Execution Time:", execution_time)

update_flatpak_packages()
