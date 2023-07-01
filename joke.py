import random
import telebot

# Jokes and memes
jokes = [
    "Why don't scientists trust atoms?\nBecause they make up everything!",
    "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
    "I told my wife she should embrace her mistakes.\nShe hugged me.",
    "Why don't skeletons fight each other?\nThey don't have the guts.",
    "Why couldn't the bicycle find its way home?\nIt lost its bearings.",
]

memes = [
    "https://example.com/meme1.jpg",
    "https://example.com/meme2.jpg",
    "https://example.com/meme3.jpg",
    "https://example.com/meme4.jpg",
    "https://example.com/meme5.jpg",
]

# Telegram bot token
TOKEN = "5956711092:AAEh65OjPnQvxOlDT7DW4Zznf60eINmEp2w"

# Create the Telegram bot
bot = telebot.TeleBot(TOKEN)

# Random joke command handler
@bot.message_handler(commands=['joke'])
def joke(message):
    random_joke = random.choice(jokes)
    bot.send_message(message.chat.id, random_joke)

# Random meme command handler
@bot.message_handler(commands=['meme'])
def meme(message):
    random_meme = random.choice(memes)
    bot.send_photo(message.chat.id, random_meme)

# Random joke/meme command handler
@bot.message_handler(commands=['random'])
def random_command(message):
    random_command = random.choice([joke, meme])
    random_command(message)

# Start the bot
bot.polling()
