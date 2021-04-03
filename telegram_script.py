from telegram import *
from telegram.ext import *

uutoken = "1737211793:AAF8Gl1HUPQXXzD46UU3MauyRwam7pV0aN4"
mytoken = "1621258257:AAHlDNPCSnVyPEVTwdTEkKenbwMZMFGdYho"
allowed_usernames = ["mnilanga_bot","SuitedLongbot","sam_uhlbot","fifthfinancebot"]
token = uutoken

bot = Bot(token)
print(bot.get_me())

updater = Updater(token,use_context=True)
dispatcher = updater.dispatcher

is_started = True
balance = float(0)

# def f_start(update, context):
#     if(is_started==True):
#         bot.send_message(
#             chat_id=update.effective_chat.id,
#             text="replying from bot ..."
#         )
# dispatcher.add_handler(CommandHandler('gg',f_start))

def f_start(update:Update, context:CallbackContext):
    try:
        if(bot.getMe().username in allowed_usernames):
            global is_started
            is_started= True
    except:
        print("something wrong in /start")
dispatcher.add_handler(CommandHandler('start',f_start,pass_args=True))

# def f_balance(update, context):
#     text = str(update.message.text).lower()
#     if len(text)>4 and text[:4] == "bal@":
#         update.message.reply_text("replying to balance")
#         bot.pinChatMessage(update.effective_chat.id, update.message.message_id)
# dispatcher.add_handler(MessageHandler(Filters.text,f_balance))

def f_record(update, context):
    if(is_started==True):
        try:
            val = float(context.args[0])
            global balance
            balance = balance + val
            update.message.reply_text("Entry accepted")
            update.message.reply_text("bal @ "+str(balance))
        except:
            update.message.reply_text("Entry rejected")
dispatcher.add_handler(CommandHandler('record', f_record))

def f_undo(update, context):
    if(is_started==True):
        try:
            print(update.message.reply_to_message.text)
            val = float(update.message.reply_to_message.text.split()[1])
            global balance
            balance = balance - val
            update.message.reply_text("Reverted:"+update.message.reply_to_message.text)
            update.message.reply_text("bal @ " + str(balance))

        except:
            update.message.reply_text("Undo rejected")
dispatcher.add_handler(CommandHandler('undo',f_undo))

def f_square(update, context):
    if(is_started==True):
        try:
            global balance
            balance = float(0)
            update.message.reply_text("bal @ " + str(balance))

        except:
            update.message.reply_text("Square rejected")
dispatcher.add_handler(CommandHandler('square',f_square))

def f_balance(update, context):
    if(is_started==True):
        try:
            update.message.reply_text("bal @ " + str(balance))

        except:
            update.message.reply_text("Balance rejected")
dispatcher.add_handler(CommandHandler('balance',f_balance))


updater.start_polling()