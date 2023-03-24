#1
#Поработайте с переменными, создайте несколько, выведите на экран.
#Запросите у пользователя некоторые числа и строки и сохраните в переменные, а затем выведите на экран.
#Используйте функции для консольного ввода input() и консольного вывода print().
#Попробуйте также в ходе выполнения задания через встроенную функцию id() понаблюдать, какие типы объектов могут изменяться и сохранять за собой адрес в оперативной памяти.

def showVariables():
     iamBool = bool(input("Please type 'True' or 'False': "))
     print(id(iamBool))
     iamString= str(input("Please type any sentence: "))
     print(id(iamString))
     iamInt = int(input("Please type any digit: "))
     print(id(iamInt))
     print("We are printing the following variables:" + " Int variable - " +str(iamInt)+ " String variable - '" + iamString + "'  Boolean variable - " + str(iamBool))



showVariables()



#2Пользователь вводит время в секундах.
# Рассчитайте время и сохраните отдельно в каждую переменную количество часов, минут и секунд.
# Переведите время в часы, минуты, секунды и сохраните в отдельных переменных.
#Используйте приведение типов для перевода строк в числовые типы. Предусмотрите проверку строки на наличие только числовых данных через встроенный строковый метод .isdigit()
#Выведите рассчитанные часы, минуты и секунды по отдельности в консоль.

def timeTrans():
    x = input("Please, type time in seconds: ")
    result = x.isdigit()
    while(result == False):
        x = input("Please, type correct time in seconds: ")
        result = x.isdigit()
    sec = int(x)
    min = int(sec/60)
    hor = int(min/60)

    print("Hours: " + str(hor)+", Minutes: "+ str(min) + ", Seconds: " +str(sec))


timeTrans()



#3
#Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#Выведете данные в консоль.



def calcUser():
    userIn = input("Please, type a digit from 1 to 9: ")
    res = int(userIn) + int(userIn + userIn) + int(userIn+userIn+userIn)
    print("The result is: " + str(res))

calcUser()