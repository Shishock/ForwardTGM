from telethon import TelegramClient, events
from telethon.sessions import StringSession
from dotenv import load_dotenv
import os
load_dotenv()

phone_number = os.getenv('phone_number')
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
SESSION_STRING = os.getenv('SESSION_STRING')
FORWARD_TO_CHAT_ID = os.getenv('FORWARD_TO_CHAT_ID')

# Создаем клиента Telegram
client = TelegramClient(StringSession(SESSION_STRING), api_id, api_hash, system_version="4.16.30-vxMAX")

# Обработчик для всех входящих сообщений
@client.on(events.NewMessage())
async def forward_handler(event):
    # Пересылаем сообщение без каких-либо проверок
    await event.message.forward_to(FORWARD_TO_CHAT_ID)

async def main():
    await client.start(phone_number)
    print("Client started. Listening for new messages...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())