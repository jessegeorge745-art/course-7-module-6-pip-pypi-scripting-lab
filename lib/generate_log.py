from datetime import datetime


def generate_log(data):
    """
    Generates a timestamped log file from a list of log entries.

    Args:
        data (list): A list of string log entries to write to the file.

    Returns:
        str: The filename of the created log file e.g. 'log_20250611.txt'

    Raises:
        ValueError: If data is not a list.
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError(
            f"Expected a list of log entries, got {type(data).__name__}."
        )

    # STEP 2: Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write each entry to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation message
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)