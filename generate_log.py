"""
generate_log.py
Writes a simple activity log to a timestamped .txt file.
"""

from datetime import datetime


def write_log(entries: list[str]) -> str:
    """Write log entries to a timestamped file and return the filename."""
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    return filename


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    output_file = write_log(log_data)
    print(f"Log written to {output_file}")