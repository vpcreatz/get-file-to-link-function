from pyrogram import Client, filters

# create a new Pyrogram client
app = Client("6243344021:AAEJS2Bb05V3YUPrjN_p16O4nOkmsqMa3Uk")

# define a function to forward the file to a bot
def forward_file_to_bot(bot, update):
    # get the username of the bot to forward the file to
    bot_username = "@File_to_pdisk_link_bot"
    
    # get the file ID of the received file
    file_id = update.message.document.file_id
    
    # forward the file to the bot
    bot.send_document(chat_id=bot_username, document=file_id)

# define a function to send the message to a user
def send_message_to_user(bot, update):
    # get the chat ID of the user to send the message to
    user_id = "{}".format(YOUR_USER_ID)

    
    # get the text of the received message
    message_text = update.message.text
    
    # send the message to the user
    bot.send_message(chat_id=user_id, text=message_text)

# create a handler for incoming messages that contain a document
@app.on_message(filters.document & filters.user(username="@File_to_pdisk_link_bot"))
def handle_document(bot, update):
    # forward the received file to the bot
    forward_file_to_bot(bot, update)
    
    # send the received message to the user
    send_message_to_user(bot, update)

# start the Pyrogram client
app.run()
