import discord
from discord.ext import commands, tasks
import asyncio
import base64
import os
import re

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.change_presence(activity=discord.Game(name="MLH Project"))

@bot.command(name='ping', help='Check the bot\'s latency')
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert to milliseconds
    await ctx.send(f'Pong! Latency is {latency}ms')

def image_to_text(image_path, output_text_file):
    try:
        with open(image_path, 'rb') as image_file:
            # Read image file as binary
            image_binary = image_file.read()

            # Encode binary data as base64
            base64_encoded = base64.b64encode(image_binary).decode('utf-8')

            # Write base64 data to text file
            with open(output_text_file, 'w') as text_file:
                text_file.write(base64_encoded)
            print(f"Image to text conversion successful! Output text saved at: {output_text_file}")

    except FileNotFoundError:
        print(f"Error: The specified image file '{image_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred during image to text conversion: {e}")


@bot.command(name='citt')
async def convert_image_to_text(ctx):
    # Ask the user for an image
    await ctx.send("Please provide an image for conversion:")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # Wait for user to upload an image
        user_response = await bot.wait_for('message', check=check, timeout=30)

        # Check if the message has attachments
        if user_response.attachments:
            attachment = user_response.attachments[0]
            image_data = await attachment.read()

            # Save the image locally
            image_path = 'input_image.png'
            with open(image_path, 'wb') as image_file:
                image_file.write(image_data)

            # Convert image to text
            output_text_file = 'output_text.txt'
            image_to_text(image_path, output_text_file)

            # Send the text file
            await ctx.send(file=discord.File(output_text_file))

        else:
            await ctx.send("No image attached. Please try again.")

    except asyncio.TimeoutError:
        await ctx.send('You took too long to respond. Please try again.')



def text_to_image(input_text_file, output_image_path):
    try:
        with open(input_text_file, 'rb') as text_file:
            # Read base64 data from text file
            base64_encoded = text_file.read()

            # Decode base64 data
            image_binary = base64.b64decode(base64_encoded)

            # Create an image from binary data
            with open(output_image_path, 'wb') as image_file:
                image_file.write(image_binary)
            print(f"Text to image conversion successful! Output image saved at: {output_image_path}")

    except FileNotFoundError:
        print(f"Error: The specified text file '{input_text_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred during text to image conversion: {e}")


@bot.command(name='cttia')
async def convert_text_to_image(ctx):
    # Ask the user for a text file
    await ctx.send("Please provide a text file:")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # Wait for the user to upload a text file
        user_response = await bot.wait_for('message', check=check, timeout=30)

        # Check if the message has attachments
        if user_response.attachments:
            # Assuming there's only one attachment, you can modify it for multiple attachments
            attachment = user_response.attachments[0]
            text_data = await attachment.read()

            # Save the text data locally
            input_text_file = 'input_text.txt'
            with open(input_text_file, 'wb') as text_file:
                text_file.write(text_data)

            # Convert text to image
            output_image_path = 'output_image.png'
            text_to_image(input_text_file, output_image_path)

            # Send the image file
            await ctx.send(file=discord.File(output_image_path))

        else:
            await ctx.send("No text file attached. Please try again.")

    except asyncio.TimeoutError:
        await ctx.send('You took too long to respond. Please try again.')




@bot.command()
async def ctti(ctx, message_link):
    # Check if the message link is valid
    match = re.match(r'https?://discord\.com/channels/(\d+)/(\d+)/(\d+)', message_link)
    if not match:
        await ctx.send("Invalid message link.")
        return

    # Extract information from the message link
    guild_id, channel_id, message_id = map(int, match.groups())

    # Get the guild, channel, and message
    guild = bot.get_guild(guild_id)
    if not guild:
        await ctx.send("Bot is not in the specified guild.")
        return

    channel = guild.get_channel(channel_id)
    if not channel:
        await ctx.send("Invalid channel.")
        return

    try:
        message = await channel.fetch_message(message_id)
    except discord.NotFound:
        await ctx.send("Message not found.")
        return

    # Check if the message has attachments
    if message.attachments:
        # Create the "downloads" folder if it doesn't exist
        os.makedirs('downloads', exist_ok=True)

        for attachment in message.attachments:
            # Save the attachment locally
            await attachment.save(f"downloads/{attachment.filename}")
            print(f"Saved {attachment.filename} from message {message.id} locally.")

            # Check if the attachment is a text file
            if attachment.filename.endswith('.txt'):
                # Convert text to image
                output_image_path = 'output_image.png'
                text_to_image(f"downloads/{attachment.filename}", output_image_path)

                # Send the image file
                await ctx.send(file=discord.File(output_image_path))
                return  # Stop processing after sending the image

        await ctx.send("No text file attachment found in the specified message.")
    else:
        await ctx.send("No attachments found in the specified message.")

def text_to_image(input_text_file, output_image_path):
    try:
        with open(input_text_file, 'rb') as text_file:
            # Read base64 data from text file
            base64_encoded = text_file.read()

            # Decode base64 data
            image_binary = base64.b64decode(base64_encoded)

            # Create an image from binary data
            with open(output_image_path, 'wb') as image_file:
                image_file.write(image_binary)
            print(f"Text to image conversion successful! Output image saved at: {output_image_path}")

    except FileNotFoundError:
        print(f"Error: The specified text file '{input_text_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred during text to image conversion: {e}")


bot.run('your token here :))')
