from pyrogram import Client, filters
from pyrogram.types import Message
from bot.services import get_service

@Client.on_message(filters.command("download"))
async def download_command(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a URL to download.")
        return

    url = message.command[1]
    service = get_service(url)
    
    if not service:
        await message.reply_text("Unsupported URL or service.")
        return

    await message.reply_text(f"Starting download from {service.__name__}...")
    # Implement the actual download logic here
