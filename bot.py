import os
import openai
from pyrogram import Client, filters, idle

# Set up OpenAI API
openai.api_key = "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"

# Initialize the Telegram bot
bot = Client("question_bot", api_id=16743442, api_hash="12bbd720f4097ba7713c5e40a11dfd2a", bot_token="6206599982:AAECqgU3Os4kTjSuS_Zz-zcM7JZHWdvbI10")

@bot.on_message(filters.command("start"))
def start_command(client, message):
    # Send a welcome message
    client.send_message(
        chat_id=message.chat.id,
        text="Welcome to the Question Bot! Send me your questions and I'll do my best to answer them."
    )

@bot.on_message(filters.text)
def answer_question(client, message):
    # Check if the message is a question
    if message.text.endswith("?"):
        # Generate a response from OpenAI
        headers = {
            "Authorization": f"Bearer {openai.api_key}"
        }
        data = {
            "model": "text-davinci-003",
            "prompt": message.text,
            "temperature": 0,
            "max_tokens": 100,
            "top_p": 1,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
            "stop": ["\n"]
        }
        response = openai.Completion.create(data=data, headers=headers)

        # Extract the answer from the response
        answer = response.choices[0].text.strip()

        # Send the answer back to the user
        client.send_message(
            chat_id=message.chat.id,
            text=answer
        )
    else:
        # Send a message if the input is not a question
        client.send_message(
            chat_id=message.chat.id,
            text="Please ask a question."
        )

# Run the bot
bot.run()
idle() 
