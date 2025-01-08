from telethon import TelegramClient, events

# Replace with your API credentials
api_id = '23304954'  # Your API ID from my.telegram.org
api_hash = '3a8f553bc00ba914d6ce7d1c37d973d1'  # Your API Hash from my.telegram.org
phone_number = '+601116145569'  # Your personal Telegram phone number

# THIS IS TO GENERATE ID FOR CHANNEL


# Create the client and connect
client = TelegramClient('test_session', api_id, api_hash)

# This function will print the chat ID of any message received
@client.on(events.NewMessage)
async def message_handler(event):
    print(f"Message from chat ID: {event.chat_id}")
    print(f"Message content: {event.message.message}")

# Start the client
async def main():
    await client.start(phone=phone_number)
    print("Listening for messages...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
