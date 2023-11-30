# DCS

Welcome to the Discord Cloud Storage Bot! This bot allows users to upload images to a Discord server, which are then converted to text files for storage. Users can later retrieve the original image by sending the bot the corresponding text file.

## Features

- **Image to Text Conversion:** Users can upload images to the Discord server, and the bot will convert them to text files for storage.

- **Text to Image Retrieval:** Users can retrieve their original images by sending the bot the text file generated during the upload.

## Commands

- `!ping`: Check the bot's latency.

- `!citt`: Convert an image to text for storage.

- `!ctti`: Convert a text file back to an image for retrieval.

## Usage

1. **Uploading an Image:**
   - Use the `!citt` command.
   - The bot will prompt you to upload an image.
   - The image will be converted to text, and the text file will be sent back to you.

2. **Retrieving an Image:**
   - Use the `!ctti` command.
   - The bot will prompt you to upload the text file generated during the image upload.
   - The original image will be sent back to you.

## Getting Started

1. **Prerequisites:**
   - Install Python.
   - Install required packages using `pip install -r requirements.txt`.

2. **Bot Token:**
   - Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy the bot token.

3. **Configuration:**
   - Replace `'YOUR_BOT_TOKEN'` in the code with your actual bot token.

4. **Run the Bot:**
   - Run the bot using `python bot.py`.

## Dependencies

- Discord.py
- Other dependencies specified in `requirements.txt`


