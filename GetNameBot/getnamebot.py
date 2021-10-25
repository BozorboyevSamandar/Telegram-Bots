from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
print("Bot ishga tushyapti...")

def ism_manosi(userIsmi):
	ismList = []
	manoList = []
	with open('D://TEST/mano.txt','r' , encoding='utf8') as file: 
			for line in file:
				ismList.append(line.split(None, 1)[0]) # add only first word
				rest = line.split(' ', 1)[1]
				manoList.append(rest)
	ismIndex = ismList.index(userIsmi)
	return f"🔹So'ralgan ism: {userIsmi}\n🔸Ma'nosi:{manoList[ismIndex]}"

def start(update,context):
    update.message.reply_html(
        '<b>Assalomu alaykum, {}</b>\n \nIsmingizni kiriting va uning ma`nosini bilib oling'.format(update.message.from_user.first_name)
    )
  
def help(update,context):
    update.message.reply_text(update.message.from_user.first_name,
                              " agar yordam kerak bo'lsa, googlega yozing")

def handle_message(update,context):
	try:
		tekst = str(update.message.text)
		natija = ism_manosi(tekst)
	except ValueError:
		natija = f'Uzr, sizning ismingiz hali bizning bazamizga qo`shilmabdi, tez orada qo`shib qo`yamiz.✅'
	finally:
		update.message.reply_text(natija)

def main():
    updater = Updater("1654001742:AAF7bqNIqvnUQZrE1c7hF9gqyJ-vvfGcNwU",use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text,handle_message))

    updater.start_polling()
    updater.idle()
    print("botingizda muammo yo'q, tabriklaymiz!")
main()