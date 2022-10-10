from datetime import datetime
import telebot

# https://t.me/GBNumbersBot
TOKEN = "5730573130:AAEftT9bebmuoBJTh8o02AGIucGYVgWofZU"

bot = telebot.TeleBot(TOKEN)

log_file = open('bot_log.txt', 'a')

del_buttons = telebot.types.ReplyKeyboardRemove()

main_menu_buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_buttons.add(telebot.types.KeyboardButton("Рациональные"))
main_menu_buttons.add(telebot.types.KeyboardButton("Комплексные"))

math_actions_buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
math_actions_buttons.row(
    telebot.types.KeyboardButton("+"),
    telebot.types.KeyboardButton("-")
)
math_actions_buttons.row(
    telebot.types.KeyboardButton("*"),
    telebot.types.KeyboardButton("/")
)

rational_num1 = 0
rational_num2 = 0
rational_action = ''

@bot.message_handler(commands=['menu'])
def send_menu(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Выбери режим калькулятора", reply_markup=main_menu_buttons)
    bot.register_next_step_handler(msg, menu_handler)


@bot.message_handler()
def answer(msg: telebot.types.Message):
    log_user_action(msg)
    if msg.text == "/start":
        bot.send_message(chat_id=msg.from_user.id, text="Привет!")

    send_menu(msg)


def menu_handler(msg: telebot.types.Message):
    log_user_action(msg)
    if msg.text.lower() == "рациональные":
        switch_to_rational(msg)
    elif msg.text.lower() == "комплексные":
        switch_to_complex(msg)
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Некорректный вариант", reply_markup=main_menu_buttons)
        bot.register_next_step_handler(msg, menu_handler)


def switch_to_rational(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Калькулятор рациональных чисел", reply_markup=del_buttons)
    bot.send_message(chat_id=msg.from_user.id, text="Введи первое число", reply_markup=del_buttons)
    bot.register_next_step_handler(msg, rational_num1_handler)


def rational_num1_handler(msg: telebot.types.Message):
    global rational_num1
    log_user_action(msg)

    if msg.text.isdigit():
        rational_num1 = int(msg.text)
        bot.send_message(chat_id=msg.from_user.id, text="Выбери действие", reply_markup=math_actions_buttons)
        bot.register_next_step_handler(msg, rational_action_handler)
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Введи корректное число", reply_markup=del_buttons)
        bot.register_next_step_handler(msg, rational_num1_handler)


def rational_action_handler(msg: telebot.types.Message):
    global rational_action
    log_user_action(msg)

    if msg.text in ["+", "-", "*", "/"]:
        rational_action = msg.text
        bot.send_message(chat_id=msg.from_user.id, text="Введи второе число", reply_markup=del_buttons)
        bot.register_next_step_handler(msg, rational_num2_handler)
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Выбери корректное дейстие", reply_markup=math_actions_buttons)
        bot.register_next_step_handler(msg, rational_action_handler)


def rational_num2_handler(msg: telebot.types.Message):
    global rational_num1, rational_action, rational_num2
    log_user_action(msg)

    if msg.text.isdigit():
        rational_num2 = int(msg.text)
        if rational_action == '/' and rational_num2 == 0:
            bot.send_message(chat_id=msg.from_user.id, text="На ноль делиь нельзя", reply_markup=del_buttons)
            bot.register_next_step_handler(msg, rational_num2_handler)
            return
        bot.send_message(
            chat_id=msg.from_user.id,
            text=str(calc_rational(rational_num1, rational_num2, rational_action)),
            reply_markup=math_actions_buttons
        )
        send_menu(msg)
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Введи корректное число", reply_markup=del_buttons)
        bot.register_next_step_handler(msg, rational_num2_handler)


def switch_to_complex(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Калькулятор комплексных чисел", reply_markup=del_buttons)
    bot.register_next_step_handler(msg, complex_handler)


def complex_handler(msg: telebot.types.Message):
    log_user_action(msg)
    print(msg)


def calc_rational(num1, num2, action):
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    else:
        return num1 / num2


def log_user_action(msg: telebot.types.Message):
    global log_file
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    username = msg.from_user.username
    text = msg.text
    print(f'[{date}][{username}] отправил(а) "{text}"')
    log_file.write(f'[{date}][{username}] отправил(а) "{text}"\n')
    log_file.flush()


print("Ready")
bot.polling()
