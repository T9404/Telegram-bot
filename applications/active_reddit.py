from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

browser = None




def get_reddit(amount):
    global browser
    num_full_pages = int(amount//10) # количество скроллинга страницы
    print('количество скроллинга', num_full_pages)
    #browser = webdriver.Chrome()


    ''' Запуск селениум кода без графического браузера'''
    options = webdriver.ChromeOptions()
    options.add_argument('headless')


    # try:
    #     browser = webdriver.Chrome(chrome_options=options)
    # except:
    #     browser = None
    #     print('Нету браузера')
    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(5)

    browser.get('https://www.reddit.com/r/memes/') # сайт реддита откуда мы будем брать контент
    time.sleep(random.randrange(1, 2))





    if num_full_pages != 0:
        for i in range(0, num_full_pages):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3, 5))

    result = [] # массив с результатами (после выполнения программы)

    hrefs = browser.find_elements_by_tag_name('a')
    print(len(hrefs))
    urls = []
    for item in hrefs:
        if "/r/memes/comments/" in item.get_attribute('href'):
            urls.append(item.get_attribute('href'))
    #urls = [item.get_attribute('href') for item in hrefs if "/r/memes/comments/" in item.get_attribute('href')] # находим ссылки на посты и делаем проверку
    print('Получено ссылок на посты: ', len(urls))

    for url in urls[:amount+6]:

        browser.get(url)  # заходим в пост
        time.sleep(random.randrange(2, 5))

        try:
            description = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[3]/div[1]/div/h1").text # получаем описание
        except:
            description = 'Описание не найдено'

        try:
            image = browser.find_element(By.XPATH,  '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[5]/div/a').get_attribute('href') # получаем картинку
        except:
            image = 'Картинка не найдена'

        try:
            reviews = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[6]/div[1]/a/span').text # получаем количество комментариев записи
        except:
            reviews = "Комментарии не найдены"
        if image != "Картинка не найдена":
            result.append({
                    'description': description,
                    'image': image,
                    'link': url,
                    'statistics': reviews
                 })
            if len(result) == amount: # реализация счетчика
                break

    return result[:amount] # возвращаем список с итоговыми значениями


def close_browser(): # функця для закрытия браузера
    global browser
    #browser.close()
    browser.quit()

# while True: # бесконечный цикл для пользователя
#     user_input = input('Введите количество постов: \nЕсли вы хотите выйти, введите "exit"\n ')
#     if user_input == "exit":
#         if browser != None:
#             close_browser()
#         break
#     else:
#         try:
#             print(get_reddit(int(user_input)))
#         except:
#             print('Вы ввели не число')

