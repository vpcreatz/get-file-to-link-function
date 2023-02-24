from pyrogram import Client, filters

# create a new Pyrogram client
api_id = "20960397"
api_hash = "d68d847d3abb2087bf74f5d0683c2993"
bot_token = "6243344021:AAEJS2Bb05V3YUPrjN_p16O4nOkmsqMa3Uk"

# create a new Pyrogram client
app = Client(
    "app",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

# define a custom filter that checks if the message text contains a given string
def text_contains(text):
    def func(_, message):
        return text in message.text.lower()
    return filters.create(func)

# define a function to get the file ID of a received document
def get_file_id(bot, update):
    file_id = update.message.document.file_id
    return file_id

# define a function to send a message with a file link to the user
def send_link_to_user(bot, update, file_id):
    chat_id = update.message.chat.id
    link = bot.get_file_link(file_id)
    bot.send_message(chat_id=chat_id, text=link)

# create a handler for messages that contain the word "hello"
@app.on_message(text_contains("hello"))
async def handle_hello(client, message):
    await message.reply_text("Hello there!")

# create a handler for incoming messages that contain a document
@app.on_message(filters.private & filters.document & filters.user("specific_username_bot"))
def handle_document(bot, update):
    file_id = get_file_id(bot, update)
    send_link_to_user(bot, update, file_id)

# start the Pyrogram client
app.run()
