# TeleTracker

TeleTracker tracks the online/offline status of a specified Telegram user and logs status changes with timestamps.

There are two ways to use it:
- **main.py**: Edit this file in a text editor to enter your credentials directly in the code (recommended for convenience and automation). See the section below for details.
- **noedit.py**: Run this script if you don't want to edit code; it will prompt you for credentials each time.

> **Tip:** Both scripts can be used interchangeably.

### Editing Credentials in Code (main.py)
1. Open `main.py` in any text editor (Notepad, VS Code, etc.).
2. Find the lines for `api_id`, `api_hash`, `phone_number`, and `tracked_user` and enter your details.
3. Save the file. Now you can run `main.py` without entering credentials each time.

If you prefer not to store credentials in the code, use `noedit.py` instead.


## Features
- Track a Telegram user's online/offline status in real-time
- Log status changes with timestamps and duration
- Output logs to both the console and a text file (`user_status_report.txt`)
- Customizable refresh interval and timezone

## Requirements
- Python 3.8+
- Telegram API credentials (API ID, API Hash, and phone number)
- Required packages: `telethon`, `tzdata`


## Installation

### Cloning the Repository on Windows
1. Open Command Prompt or PowerShell.
2. Navigate to the folder where you want to clone the repository.
3. Run:
   ```powershell
   git clone https://github.com/an229-h/TeleTracker.git
   cd TeleTracker
   ```

### Installing Requirements
Run:
   ```sh
   pip install -r requirements.txt
   ```
## Termux Users

You can also run TeleTracker on Android using Termux:

1. Install [Termux](https://f-droid.org/packages/com.termux/) from F-Droid.
2. Open Termux and update packages:
   ```sh
   pkg update && pkg upgrade
   ```
3. Install Python and Git:
   ```sh
   pkg install python git
   ```
4. Clone the repository:
   ```sh
   git clone https://github.com/an229-h/TeleTracker.git
   cd TeleTracker
   ```
5. Install requirements:
   ```sh
   pip install -r requirements.txt
   ```
6. Run the script:
   ```sh
   python main.py
   ```

## Setup
1. Create a new Telegram application at [my.telegram.org](https://my.telegram.org) to obtain your API ID and API Hash.
2. Open `main.py` and fill in the following fields with your credentials:
   - `api_id`
   - `api_hash`
   - `phone_number` (in international format, e.g., `+91...`)
   - `tracked_user` (username or user ID to track)


## Usage

To run with credentials saved in the code:
```sh
python main.py
```
To be prompted for credentials each time:
```sh
python noedit.py
```
Both scripts log the tracked user's status changes to the console and to `user_status_report.txt`.

## Notes
- The refresh interval is set to 1 second by default. You can change this in `main.py` (see the `asyncio.sleep(1)` line).
- Make sure your credentials are correct and you have access to the Telegram account.
- The log file will be created automatically in the script directory.

## License

This project is licensed under the MIT License.

