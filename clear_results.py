import os
# С помощью цикла перебираем файлы в папке и удаляем
dir ='C:\\Users\\user\\PycharmProjects\\Testing_Automation_and_Python_Programming_Selenium\\test_results\\tests\\test_authorization.py'
for file in os.scandir(dir):
    os.remove(file.path)
