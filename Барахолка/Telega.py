def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я твой новый бот!")

def main():
    updater = Updater(token='6238054093:AAGDpk23M6ACzh-FRpV87tjLTzrwmtoYavg', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
# функция для обработки команды /start
def start(update, context):
    # создаем кнопки и добавляем их в меню
    keyboard = [[InlineKeyboardButton("Button 1", callback_data='menu1'),
                 InlineKeyboardButton("Button 2", callback_data='menu2')],
                [InlineKeyboardButton("Cancel", callback_data='cancel')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

# функция для обработки нажатия кнопок
def button(update, context):
    query = update.callback_query
    if query.data == 'menu1':
        # создаем подменю для кнопки 1
        keyboard = [[InlineKeyboardButton("Submenu 1-1", callback_data='submenu1'),
                     InlineKeyboardButton("Submenu 1-2", callback_data='submenu2')],
                    [InlineKeyboardButton("Back", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Button 1 menu", reply_markup=reply_markup)
    elif query.data == 'menu2':
        # создаем подменю для кнопки 2
        keyboard = [[InlineKeyboardButton("Submenu 2-1", callback_data='submenu3'),
                     InlineKeyboardButton("Submenu 2-2", callback_data='submenu4')],
                    [InlineKeyboardButton("Back", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Button 2 menu", reply_markup=reply_markup)
    elif query.data == 'back':
        # возвращаемся к основному меню
        keyboard = [[InlineKeyboardButton("Button 1", callback_data='menu1'),
                     InlineKeyboardButton("Button 2", callback_data='menu2')],
                    [InlineKeyboardButton("Cancel", callback_data='cancel')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Please choose:", reply_markup=reply_markup)
    else:
        query.edit_message_text(text="Selected: {}".format(query.data))

# функция для обработки команды /cancel
def cancel(update, context):
    update.message.reply_text('Canceled')

# создаем обработчики
updater = Updater('TOKEN')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel))

# запускаем бота
updater.start_polling()
updater.idle()
