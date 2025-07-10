# TeleTracker

TeleTracker is a simple Python script that tracks the online/offline status of a specified Telegram user and logs status changes with timestamps.

## Features
- Tracks a Telegram user's online/offline status in real-time
- Logs status changes with timestamps and duration
- Outputs logs to both the console and a text file (`user_status_report.txt`)
- Customizable refresh interval and timezone

## Requirements
- Python 3.8+
- Telegram API credentials (API ID, API Hash, and phone number)
- Required packages: `telethon`, `tzdata`

## Installation
1. Clone or download this repository.
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Setup
1. Create a new Telegram application at [my.telegram.org](https://my.telegram.org) to obtain your API ID and API Hash.
2. Open `main.py` and fill in the following fields with your credentials:
   - `api_id`
   - `api_hash`
   - `phone_number` (in international format, e.g., `+91...`)
   - `tracked_user` (username or user ID to track)

## Usage
Run the script using Python:
```sh
python main.py
```

The script will log the tracked user's status changes to the console and to `user_status_report.txt`.

## Notes
- The refresh interval is set to 1 second by default. You can change this in `main.py` (see the `asyncio.sleep(1)` line).
- Make sure your credentials are correct and you have access to the Telegram account.
- The log file will be created automatically in the script directory.

## License

This project is licensed under the MIT License.

```
