client1 = {
  "name": "ООО 'Рога и Копыта'",
  "status": "Истец",
  "inn": 4545454545
}


client2 = {
  "name": "Интерсолюшн",
  "status": "Ответчик",
  "inn": 155667878
}



client3 = {
  "name": "ООО 'Инкорп'",
  "status": "Истец",
  "inn": 452452525
}




client4 = {
  "name": "ООО 'ДиЖи корп'",
  "status": "Ответчик",
  "inn": 535265653
}



thisList =[client1, client2, client3, client4]


def showClients():
    for i in thisList: print(i)


showClients()