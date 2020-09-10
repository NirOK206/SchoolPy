#
# CatOS-tiny based SchoolPy v. 1.0.0 
# 
# SchoolPy Main Script. CHANGE ONLY CONFIGURATION!
# Бот-помощник для школьных бесед v. 1.0.0
# (c) aGrIk Software.
# CatOS: (c) Catware Development. All rights reserved.

##############################################################
##############################################################
########CONFIGURATION#########################################
##############################################################
##############################################################

# Токен - API-ключ, сгенерированный в "Настройки -> Работа с API"

token = "ТОКЕН"

# gid - ID группы бота в разделе "Настройки". Просто число без club.

gid = "ID группы"

# admins - числовые айди администраторов бота, перечисленные через запятую. Имеют доступ ко всем функциям бота.

admins = "Администрация"

# moders - числовые айди модераторов бота, перечисленные через запятую. Имеют доступ к изменению расписания, домашних заданий, объявлений, к команде "alive?",
# к команде "freeze". Если модерировать бота не сможет никто, кроме админа/ов - оставьте поле пустым.

moders = "Модерация"

# group_name - название группы, в которой появится бот.

group_name = "Название группы"

# mention - упоминание бота для реагирования на кнопки. Измените лишь КОРОТКОЕ ИМЯ ГРУППЫ на её короткий адрес.

mention = "[club" + gid + "|@" + "КОРОТКОЕ ИМЯ ГРУППЫ" + "] "

##############################################################
##############################################################
########CONFIGURATION#########################################
##############################################################
##############################################################



###############
# Definitions #
###############

def mainKeyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button("📚 Расписание", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("📝 Домашние задания", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("🗣 Объявления", color=VkKeyboardColor.PRIMARY)
    vk.messages.send(
    peer_id=peer_id,
    random_id=randd.randint(-2147483647, 2147483647),
    keyboard=keyboard.get_keyboard(),
    message="Клавиатура сгенерирована.")

def clearKeyboard():
    vk.messages.send(
    peer_id=peer_id,
    random_id=randd.randint(-2147483647, 2147483647),
    keyboard='{"buttons":[],"one_time":true}',
    message="Клавиатура убрана.")

def messagecust(message, peer_id):
    log("Issued messagecust() with parameters: {} {}. No output.".format(str(message), str(peer_id)))
    vk.messages.send(random_id=randd.randint(-2147483647, 2147483647),peer_id=peer_id, message=str(message), dont_parse_links=1)

def log(text):
    try:
        txt = "[ " + str("-".join(deunix(time.time()))) + " UTC ] [" + str(__name__) + "] [" + str(__file__) + "] " + text + "\n"
    except:
        txt = "[ " + str("-".join(deunix(time.time()))) + " UTC ] [" + str(__name__) + "] [" + str(__file__) + "] Здесь могла бы быть ваша реклама..." + "\n"
    PlusWrite(txt, "system.log")

def getid(sname):
    unamea = vk.users.get(user_ids=sname)
    log("Issued getid() with parameter {}. Output: {}".format(sname, str(unamea[0]['id'])))
    return unamea[0]['id']

def getmention(uid):
    unamee = vk.users.get(user_id=uid)[0]
    log("Issued getmention() with parameter {}. Output: {}".format(str(uid), "[id" + str(unamee["id"]) + "|" + unamee["first_name"] + " " + unamee["last_name"] + "]"))
    return "[id" + str(unamee["id"]) + "|" + unamee["first_name"] + " " + unamee["last_name"] + "]"

def deunix(integer):
    return datetime.datetime.utcfromtimestamp(integer).strftime('%Y %m %d %H %M %S').split(" ")

def getname(uid):
    unamee = vk.users.get(user_id=uid)[0]
    log("Issued getname() with parameter: {}. Output: {}".format(str(uid), str(unamee["first_name"] + " " + unamee["last_name"])))
    return unamee["first_name"] + " " + unamee["last_name"]

def succ():
    print("[ \033[92mok\033[0m ]")

def procmsg(text):
    rows, columns = os.popen('stty size', 'r').read().split()
    intm = int(columns) - 13 - len(text)
    txt = " " * intm
    print("\033[94m>>>\033[0m " + text + "..." + txt, end="")

def PlusWrite(text, target):
    file = open(str(target), 'a', encoding='utf-8')
    file.write(str(text))
    file.close()

def ReadFF(file): # Read From File
    try:
        log("Reading {}...".format(file))
        Ff = open(file, 'r', encoding='UTF-8')
        Contents = Ff.read()
        Ff.close()
        log("File content:\n=====================\n" + Contents + "\n=====================")
        return Contents
    except:
        log("File not found.")
        return None

def FailMsg(text): # FAIL message
    print("[ fail ] " + text)

def mta(text,noLinks=0):
    try:
        vk.messages.send(
            random_id=randd.randint(-2147483647, 2147483647),
            user_ids=admins,
            message=str(text)[:4000],
            dont_parse_links=1
            )
        log("Sended an message to admins: " + str(text))
    except Exception as e:
        FailMsg('Не удалось вызвать MTA: ' + str(e))

def writeTo(text, target):
    file = open(str(target), 'w', encoding='utf-8')
    file.write(str(text))
    file.close()
    log("Wrote <" + str(text) + "> to " + target)

def message(text):
    text = str(text)
    try:
        if str(user_id) not in ReadFF("restricted.txt"):
            messagecust(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], peer_id)
            log("Sent message: " + text + " Peer ID: " + str(peer_id))
        else:
            messagecust(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], user_id)
            log("Sent message: " + text + " Peer ID: " + str(user_id))
    except Exception as e:
        print("Нашел свой покой в message: ", e)

import time
import datetime
###############
# Definitions #
###############

log("SchoolPy v. 1.0.0 is starting. Definitions was defined right now.")

#
# Modules
#

import os
procmsg("Загрузка datetime")
import datetime
succ()
procmsg("Загрузка json")
import json
succ()
procmsg("Загрузка numpy")
import numpy as np
succ()
procmsg("Загрузка random")
import random as randd
from random import random
succ()
procmsg("Загрузка traceback")
import traceback
succ()
procmsg("Загрузка shutil")
import shutil
succ()
procmsg("Загрузка vk_api")
import vk_api
import vk_api as api2
from vk_api import VkApi
from vk_api import VkUpload
succ()
procmsg("Загрузка time")
import time
succ()
procmsg("Загрузка vk_api [дополнительные библиотеки]")
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
succ()
procmsg("Загрузка sys")
import sys
succ()

procmsg("Авторизация")
vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, gid)
vk = vk_session.get_api()
succ()

procmsg('Финальная подготовка.')
try:
    vk.groups.enableOnline(group_id=gid)
except:
    pass
if not os.path.exists("restricted.txt"): writeTo("", "restricted.txt")
if not os.path.exists("schedule.txt"): writeTo("Расписание не установлено.", "schedule.txt")
if not os.path.exists("hometasks.txt"): writeTo("Домашние задания не установлены.", "hometasks.txt")
if not os.path.exists("hometasks.txt"): writeTo("Объявления не установлены.", "hometasks.txt")
mta("Запускаю ядро...")
succ()

log("SchoolPy v. 1.0.0 started.")
print("SchoolPy v. 1.0.0 запущен и готов к использованию. ")

#
# Цикл обработки событий LongPoll
#
while True:
    try:
        for event in longpoll.listen():
            log("New event: " + str(event.type))
            if event.type == VkBotEventType.MESSAGE_NEW or event.type == VkBotEventType.MESSAGE_EDIT:
                # Раскидывание по переменным
                obj = event.object['message'] #Главная информация
                user_id = str(obj['from_id']) #ID автора сообщения
                peer_id = str(obj['peer_id']) #ID беседы, из которой отправлено сообщение
                text = str(obj['text'].replace(mention, "").replace("[club" + gid + "|" + group_name + "] ", "")) #Содержимое сообщения
                attachments = list(obj['attachments']) #Приложения к сообщению
                print("Сообщение от ", getname(user_id), " (", str(user_id), ") в чате ", peer_id, ", вложений: ", str(len(attachments)), ", текст: ", text)
                log("Message from " + getname(user_id) + " (" + str(user_id) + ") in chat " + peer_id + " + attachments: " + str(len(attachments)) + " + text: " + text)

                if text == "📚 Расписание":
                    log("Executed 📚 Расписание")
                    message(ReadFF("schedule.txt"))

                if text == "📝 Домашние задания":
                    log("Executed 📝 Домашние задания")
                    message(ReadFF("hometasks.txt"))

                if text == "🗣 Объявления":
                    log("Executed 🗣 Объявления")
                    message(ReadFF("alerts.txt"))

                # Админское
                if str(user_id) in admins:
                    #exec
                    if text.startswith("exec") or text.startswith("/exec"):
                        try:
                            log("Executed exec, parameter: " + ' '.join(text.split(' ')[1:]))
                            exec(' '.join(text.split(' ')[1:]))
                            message("ok")
                        except:
                            exc_type, exc_value, exc_tb = sys.exc_info()
                            log('Error: ' + str("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb))))
                            message('Error: ' + str("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb))))

                #Модерское
                if str(user_id) in moders or str(user_id) in admins:
                    #setschedule
                    if text.startswith("setschedule"):
                        writeTo(text.replace("setschedule ", ""), "schedule.txt")
                        log("Changed schedule to " + text.replace("setschedule ", ""))
                        message("Расписание сохранено.")

                    #sethometasks
                    if text.startswith("sethometasks"):
                        writeTo(text.replace("sethometasks ", ""), "hometasks.txt")
                        log("Changed hometasks to " + text.replace("sethometasks ", ""))
                        message("Домашнее задание сохранено.")

                    #setalerts
                    if text.startswith("setalerts"):
                        writeTo(text.replace("setalerts ", ""), "alerts.txt")
                        log("Changed alerts to " + text.replace("setalerts ", ""))
                        message("Объявление сохранено.")

                    #freeze
                    if text.startswith("freeze"):
                        target = getid(text.replace("freeze ", ""))
                        if str(target) not in ReadFF("restricted.txt"):
                            PlusWrite(str(target) + "\n", "restricted.txt")
                            log("Freezed " + str(target) + " (" + getname(target) + ")")
                            message(getmention(target) + " теперь будет получать ответы на свои команды в личку с ботом.")
                        else:
                            writeTo(ReadFF("restricted.txt").replace(str(target) + "\n", ""), "restricted.txt")
                            log("Unfreezed " + str(target) + " (" + getname(target) + ")")
                            message(getmention(target) + " теперь будет получать ответы на свои команды как обычно.")

                    #alive
                    if text == "alive?":
                        log("Checked alive")
                        message("Я всё ещё жив, вот прикол?")

            if event.type == VkBotEventType.MESSAGE_ALLOW:
                peer_id = str(obj['peer_id']) #ID беседы, из которой отправлено сообщение
                mainKeyboard()

    except Exception as e:
        try:
            print('Паника ядра: ' + str(e))
            if str(user_id) in admins:
                #exc_type, exc_value, exc_tb = sys.exc_info()
                message('Error: ' + e.__traceback__)
                log('Error: ' + e.__traceback__)
            else:
                #exc_type, exc_value, exc_tb = sys.exc_info()
                mta("Произошла ошибка при выполнении команды \"" + text + "\" с прикреплениями " + attachments + ", вызванной " + getmention(user_id) + " в " + peer_id + "\n\n" + e.__traceback__)
                log('Error: ' + e.__traceback__)
                message("Произошла ошибка при выполнении команды. Администрация бота уже извещена о проблеме.")
        except:
            log("Can't handle exception, skipping...")