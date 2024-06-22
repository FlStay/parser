import requests
from bs4 import BeautifulSoup as bs
import time
import telebot
from fake_useragent import UserAgent

bot = telebot.TeleBot("7371050628:AAFX6QK3I_YqQfq0NI35-jlcnZF6wZgJX18")
@bot.message_handler(commands=['start'])
def startBot(message):
    def startParser():
        head = {"UserAgent": UserAgent().random}
        url = 'https://freelance.habr.com/tasks?q=Парс'
        r = requests.get(url, headers=head)
        soup_1 = bs(r.text, "lxml")
        order = soup_1.find_all('li', class_ = "content-list__item")

        list_order_1 = []
        list_order_2 = []

        while True:
            for item in order:
                title_1 = item.find('div', class_ = "task__title").text
                link_1 = item.find('div', class_ = "task__title").find('a').get('href')
                try:
                    price_1 = item.find('span', class_ = "count").text
                except:
                    price_1 = 'договорная'
                mess_1 = f"{title_1} |\n{price_1} |\nhttps://freelance.habr.com/{link_1}"
                list_order_1.append(mess_1)
            time.sleep(600)
            for item in order:
                title_2 = item.find('div', class_ = "task__title").text
                link_2 = item.find('div', class_ = "task__title").find('a').get('href')
                try:
                    price_2 = item.find('span', class_ = "count").text
                except:
                    price_2 = 'договорная'
                mess_2 = f"{title_2} |\n{price_2} |\nhttps://freelance.habr.com/{link_2}"
                glux = "--------------"
                list_order_2.append(mess_2)

            for item_1 in list_order_1:
                for item_2 in list_order_2:
                    if item_1 != item_2:
                        print(item_1, item_2)
                        for i in list_order_2:
                            bot.send_message(message.chat.id, i, parse_mode='html', disable_web_page_preview=True)
                            bot.send_message(message.chat.id, glux, parse_mode='html')
                            break
                        break
                    break
                break

            list_order_1.clear()
            list_order_2.clear()

    startParser()
bot.infinity_polling()
