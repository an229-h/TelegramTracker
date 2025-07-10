from telethon import TelegramClient
from telethon.tl.types import UserStatusOffline, UserStatusOnline
from datetime import datetime, timedelta
import asyncio

# Credentials:



api_id = int(input("Enter your API ID: "))  # Replace with your API ID
api_hash = input("Enter your API Hash: ")  # Replace with your API Hash
phone_number = input("Enter your Phone Number in international format: ")  # Replace with your Phone Number
tracked_user = input("Enter the Username or User ID to Track: ")  # Replace with the Username or User ID to Track
log_file = "user_status_report.txt"   #DO not mess up with this file, it will be created automatically

TIMEZONE_OFFSET = (5, 30)
TIMEZONE_NAME = 'IST'
last_status = None
last_time = None

def log_status_change(user, status):
    import zoneinfo
    global last_status, last_time
    
    now_utc = datetime.now(tz=zoneinfo.ZoneInfo('UTC'))
    
    local_time = now_utc + timedelta(hours=TIMEZONE_OFFSET[0], minutes=TIMEZONE_OFFSET[1])
    current_time_str = local_time.strftime('%d.%m.%Y %H:%M:%S')
    elapsed_str = ''
    if last_status is not None and last_time is not None:
        elapsed = local_time - last_time
        total_seconds = int(elapsed.total_seconds())
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        if hrs > 0:
            elapsed_str = f" | {user.username or user.id} was {last_status.lower()} for {hrs}h {mins}m {secs}s"
        elif mins > 0:
            elapsed_str = f" | {user.username or user.id} was {last_status.lower()} for {mins}m {secs}s"
        else:
            elapsed_str = f" | {user.username or user.id} was {last_status.lower()} for {secs}s"
    with open(log_file, "a") as file:
        file.write(f"{current_time_str} {TIMEZONE_NAME} - {user.username or user.id} is {status}{elapsed_str}\n")
    print(f"{current_time_str} {TIMEZONE_NAME} - {user.username or user.id} is {status}{elapsed_str}")
    last_status = status
    last_time = local_time

client = TelegramClient('session_name2', api_id, api_hash)

async def check_user_status():
    await client.start(phone=phone_number)
    
    
    while True:
        user = await client.get_entity(tracked_user)
        if isinstance(user.status, UserStatusOnline):
            current_status = 'Online'
        elif isinstance(user.status, UserStatusOffline):
            current_status = 'Offline'
        else:
            current_status = 'Unknown'

        
        global last_status
        if current_status != last_status:
            log_status_change(user, current_status)

        await asyncio.sleep(1)  # Adjust the interval as needed

async def main():
    try:
        async with client:
            await check_user_status()
    except asyncio.CancelledError:
        print("\n[INFO] Program stopped by user.")
    except KeyboardInterrupt:
        print("\n[INFO] Program interrupted by user.")


# main
if __name__ == "__main__":
    asyncio.run(main())
