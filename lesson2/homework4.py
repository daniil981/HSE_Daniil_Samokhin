import itertools


#Напишите функцию для валидации ИНН (идентификационного номера налогоплательщика),
#которая принимает в качестве аргумента строку, содержащую ИНН или просто набор цифр, похожий на ИНН.
#Функция возвращает True в случае, если ИНН прошёл проверку, и False, если проверка не пройдена.
#Для удобства лучше разбить код на несколько взаимосвязанных функций.

#Проверяет валидность инн для организаций
def verOrg(nmInn):
    sumIn = 0
    t =0
    koef =  [2, 4, 10, 3, 5, 9, 4, 6, 8]

    while(t <= len(koef)-1):
        sumIn += koef[t] * nmInn[t]
       # print(str(sumIn))
        t += 1

    cntDig = sumIn%11

    #print(cntDig)

    if cntDig>9:
        trCnt = cntDig % 10

        if trCnt == nmInn[9]:
            print("True inn")

        else:
            print("False inn")
    else:
        if cntDig == nmInn[9]:
            print("True inn")

        else:
            print("False inn")



#Проверяет валидность инн для физ.лиц и ИП
def verPh(nmInn):
    sumIn = 0
    t = 0
    koef = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

    while (t <= len(koef)-1):
        sumIn += koef[t] * nmInn[t]
        #print(str(sumIn))
        t += 1

    cntDig = sumIn % 11

    #print(cntDig)

    if cntDig > 9:
        trCnt = cntDig % 10

        if trCnt == nmInn[11]:
            print("True inn")

        else:
            print("False inn")
    else:
        if cntDig == nmInn[10]:
            print("True inn")

        else:
            print("False inn")











def verfInn(numberInn):
    inn = []
    if(type(numberInn) is type(6)):
        trInn = str(numberInn)
        l = 0
        while (l <= len(trInn) - 1):
            inn.append(int(trInn[l]))
            l += 1
        if (len(inn) == 12):
            verPh(inn)
        elif (len(inn) == 10):
            verOrg(inn)
        else:
            print("Пожалуйста, введите корректный инн и перезапустите программу")

    else:
        print("Пожалуйста, введите число и перезапустите программу")






verfInn(543345433312)
