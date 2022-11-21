import json
import os
import requests
import time
import math


all_zp = 0
all_n = 0

# Получаем перечень ранее созданных файлов со списком вакансий и проходимся по нему в цикле
for fl in os.listdir('F:\data for parcer'):

    # Открываем файл, читаем его содержимое, закрываем файл
    f = open('F:\data for parcer\{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()

    # Преобразуем полученный текст в объект справочника
    jsonObj = json.loads(jsonText)

    # Получаем и проходимся по непосредственно списку вакансий
    for v in jsonObj['items']:
        # Обращаемся к API и получаем детальную информацию по конкретной вакансии
        req = requests.get(v['url'])
        data = req.content.decode()
        req.close()
        data = json.loads(data)
        n = 0
        sum_zp = 0
        # цикл, переберает объекты, т.е перебирает вакансии
        # проверяем есть ли значения в словаре по ключу salary. Т.е проверяем есть ли в вакансии данные по зарплате
        if v['salary'] != None:
            s = v['salary']
            # проверяем есть ли значения по ключу from. Т.е проверяем есть ли в вакансии данные по минимальной зп
            if s['from'] != None:
                n += 1
                # считаем сумму ЗП по вакансиям
                sum_zp += s['from']
        # добавляем сумму зп по итерации цикла
        all_zp += sum_zp
        # добавляем сумму n по итерации цикла
        all_n += n
        # Создаем файл в формате json с идентификатором вакансии в качестве названия
        # Записываем в него ответ запроса и закрываем файл
        fileName = 'F:\data for parcer отработанный\{}.json'.format(v['id'])
        f = open(fileName, mode='w', encoding='utf8')

        f.write(json.dumps(data, indent = 3, ensure_ascii=False))
        f.close()

        time.sleep(0.25)

#считаем среднюю ЗП
av_zp=all_zp/all_n
print("Количество найденных вакансий, содержащих сведения о зп:", all_n)
print("Средняя зп:", math.ceil(av_zp))
print('Вакансии собраны')
