import os
import discord
import openai

openai.api_key = 'insert your openai key here'
token = 'insert your discord bot token here'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/gpt"):
        text = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are ChatGPT, a helpful assisstant"},
                {"role": "user",
                    "content": f"Please respond to the following query\n\n{message.content[5:]}"}
            ]
        )

        await message.channel.send(text['choices'][0]['message']['content'])

client.run(token)
