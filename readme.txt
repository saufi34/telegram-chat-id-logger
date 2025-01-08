# Telegram Client Chat ID Logger

## Overview
This script uses the **Telethon** library to create a Telegram client that listens for incoming messages and logs the chat ID and message content to the console. It is a simple tool for interacting with the Telegram API and can be adapted for various use cases involving Telegram bots or clients.

## Prerequisites

1. **Python Installed**: Ensure you have Python 3.7 or higher installed.
2. **Telethon Library**: Install the Telethon library by running:
   ```bash
   pip install telethon
   ```
3. **Telegram API Credentials**: Obtain your API ID and API Hash from [my.telegram.org](https://my.telegram.org/).
4. **Telegram Phone Number**: Use a valid phone number associated with your Telegram account.

## Configuration
Replace the placeholder values in the script with your own:
- `api_id`: Your API ID from Telegram.
- `api_hash`: Your API Hash from Telegram.
- `phone_number`: Your personal Telegram phone number.

Example:
```python
api_id = '123456'
api_hash = 'abcdef1234567890'
phone_number = '+123456789'
```

## Features
- Connects to your Telegram account using Telethon.
- Listens for new messages.
- Logs the chat ID and message content to the console.

## How to Run
1. Save the script to a file (e.g., `telegram_chat_id_logger.py`).
2. Run the script using Python:
   ```bash
   python telegram_chat_id_logger.py
   ```
3. Upon running, the script will:
   - Authenticate your Telegram account.
   - Start listening for messages.
   - Print the chat ID and content of each incoming message to the console.

## Example Output
When a message is received, the script logs details like this:
```
Message from chat ID: 123456789
Message content: Hello, World!
```

## Notes
- Ensure you do not share your API credentials publicly to avoid security risks.
- This script is for personal use and experimentation. Use responsibly and in compliance with Telegram's terms of service.

## Dependencies
- **Telethon**: A Python library for interacting with Telegram's API.

## Troubleshooting
If you encounter issues:
1. Verify your API ID, API Hash, and phone number are correct.
2. Check your network connection.
3. Ensure Telethon is installed correctly.
