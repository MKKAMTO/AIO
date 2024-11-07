from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply_text("Welcome to the Music Download Bot! Use /help to see available commands.")

@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    help_text = """
    Available commands:
    /start - Start the bot
    /help - Show this help message
    /auth <service> - Authenticate with a music service
    /download <url> - Download a track or album
    /settings - Change bot settings
    """
    await message.reply_text(help_text)
