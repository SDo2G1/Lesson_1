#Урок второй...словари


#лист как сумка с вещами, достаём и кладём
list1 = [1, 2, 3, 'come as you are']


#обращение ко всему листу
#print(list1)

#исключение повторов в листе (F то больше чем 44 и f то нет =))
list2 = [1, 2, 2, 2, 3, 44, 'f']
#print(list2)

list2 = list(set(list2))
#print(list2)

#цифра 2 значит порядковый номер в листе
#print(list1[2])


#словарь с квадратными скобками
#словари используют для того, чтобы доставать значения по ключу из общего списка dic["first"] = 1
#складывем что угодно 1 словарь в один и т.д.
dic = dict()
#print(dic)


dic["first"] = 1
dic["second"] = 12345

dic["first"] = 'hello!'

#print(dic)

#команды пишут через "пример"
#print(dic.get("second"))
#print(dic["second"])



#составляю словарь
d2 = {"val1": 1,
      "val2": 22,
      1: ['hello', None, True, 1.1],
      "val666": 666
      #запихиваем лист в словарь 1: ['hello', None, True, 1.1]
}

#print(d2)
#print(d2.get(1))
#print(d2.get("val2"))
#keys используют для показа ключей в словаре
#print(d2.keys())
#values позвляет искать по значениям в словаре
#print(d2.values())

#поиск словарь в словаре
d3 = dict()
d3['new'] = d2
d3['old'] = None
#print(d3)

#поиск словаря вложенного в этот словарь
#print(d3.get('new').get('val1'))

#состав словаря в словаре в словаре и ещё в одном словаре требует много времени, и начинает медленнее чем list
#dict как шкаф с полочками, а list как мешок
#value и get две основные функции для использования словаря

#запихиваем словарь в лист
l4 = [d2, d3]

#print(l4)

#поиск по листовым ключам только
l5 = list(d3.keys())
#print(l5)

# когда не знаешь, что лежит в определённом листе или словаре, можно глянуть классы
#print(type(l4))
#print(type(d3))

#и ЛИСТ и СЛОВАРЬ это всё виды одной коллекции
# ниже тайпл, это не то же что лист, и структура хранения данных совсем другая
#п.с. есть много разных типов данных, просто учи дальше)) d3. пиши и смотри список команд достуаных для словаря d3
a = (1, 2, 3)
#print(a)
#print(a[1])


#чтобы создать строку и запихвать в неё всё что угодно
#строка в несколько строк (string)
s3 = """улыбок
тебе
дед
мокар=))))
"""


#словари складывать нельзя (d5 = d2 + d3)
#альтернативный вид поиска

if 123 :
      print('YUUUMM!')
if l5 :
      print("I find")