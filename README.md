# View WiFi Password

This Python script retrieves and displays WiFi passwords stored on your device. It extracts WiFi profile information using the `netsh` command-line utility and presents it in a user-friendly format.

## Key Features

*   **Password Retrieval:** Extracts WiFi passwords from stored profiles.
*   **Profile Listing:** Lists all available WiFi profiles on the system.
*   **Formatted Output:** Presents the retrieved information in a clear, tabular format.
*   **Validation Key:** Requires a validation key to run the script.
*   **Colorized Output:** Uses `colorama` for enhanced readability with colored text.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/versaagonon/view-wifi-password-.git
    cd view-wifi-password-
    ```

2.  **Install dependencies:**

    ```bash
    pip install colorama
    ```

## Usage

1.  **Run the script:**

    ```bash
    python WifiPassviewBy@versaagonon.py
    ```

2.  **Enter the validation key:**

    When prompted, enter the validation key: `versaagonon`.

3.  **View the WiFi passwords:**

    The script will display a table containing the WiFi profile names, SSIDs, authentication methods, encryption types, and passwords.

## Tech Stack and Dependencies

*   **Python:** Programming language.
*   **subprocess:** Used to execute command-line commands (`netsh`).
*   **os:** Used for interacting with the operating system (not explicitly used, but imported).
*   **time:** Used for time-related tasks (not explicitly used, but imported).
*   **colorama:** Used for adding color to the terminal output.

## Suggestions for Improvements

1.  **Error Handling:** Implement more robust error handling to gracefully handle cases where WiFi profiles are missing or the `netsh` command fails.  Specifically, handle `subprocess.CalledProcessError` exceptions.

2.  **Cross-Platform Compatibility:**  The script currently relies on the `netsh` command, which is specific to Windows.  Consider adding support for other operating systems (e.g., macOS, Linux) by using appropriate command-line tools (e.g., `airport` on macOS, `nmcli` on Linux).

3.  **Security Enhancement:**  Storing the validation key directly in the script is not secure.  Implement a more secure method for validation, such as reading the key from an environment variable or a configuration file.  Consider removing the validation key entirely, or replacing it with a warning about the potential risks of running the script.  Also, add a disclaimer about the ethical implications of using such a tool.
