from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
import requests
import urllib.parse
import asyncio
from info import *
from database import *

def ask_query(query, model=None):
    default_model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
    system_prompt = """You are a helpful assistant. Your name is ResponseByAi, and your owner's name is Captain, known as @itzAsuraa"""

    model = model or default_model

    if model == default_model:
        query = f"{system_prompt}\n\nUser: {query}"

    encoded_query = urllib.parse.quote(query)
    url = f"https://darkness.ashlynn.workers.dev/chat/?prompt={encoded_query}&model={model}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("response", "😕 Sorry, no response found.")
    else:
        return f"⚠️ Error fetching response from API. Status code: {response.status_code}"

@Client.on_message(filters.text & filters.group)
async def handle_text_message(client: Client, message: Message):
    if FSUB and not await get_fsub(client, message):
        return

    # Get the text content of the message
    user_text = message.text.strip()

    if user_text:
        # Send typing action to simulate a response delay
        await send_typing_action(client, message.chat.id)

        # Call the ask_query function to process the user query
        reply = ask_query(user_text)
        user_mention = message.from_user.mention
        await message.reply_text(f"{user_mention}, {reply} 🚀")
    else:
        await message.reply("👋 Please type a message! I’m here to help! 😊")

# Simulate Typing Action
async def send_typing_action(client, chat_id, duration=1):
    """
    Simulate typing action.
    """
    await client.send_chat_action(chat_id, ChatAction.TYPING)  # Use ChatAction enum
    await asyncio.sleep(duration)  # Wait for the specified duration
