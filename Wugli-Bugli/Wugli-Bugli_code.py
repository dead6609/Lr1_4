#import os                                                       #просто лишняя докачка
#from pathlib import Path
import sys                                                       #ЗАкрытие проги
from os.path import dirname, join                                #Нахождение относительного пути

from PyQt5.Qt import *                                            # PyQt5
from PyQt5 import uic

class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.current_dir = dirname(__file__)
        self.load_ui()
        
    def load_ui(self):
                                 #Беру путь самого файла python
        file_path = join(self.current_dir, "./Wugli-bugli_form.ui")  #Закидываю туда нужный мне файл (это форма,если что)
        uic.loadUi(file_path , self)                            #Инициализирую саму форму
        self.Load_text.clicked.connect(self.onClicked)          #Load_text - имя кнопки(!!!), по имени кнопки (при нажатии на неё) - присоединяю функцию OnClicked

    # тут тупо логика функции, ничего интересного
    def onClicked(self):
        chet = False
        file_path = join(self.current_dir, "./text.txt")             #То же самое, что и с формной, но с текстовым файлом
        with open(file_path, 'r', encoding="UTF-8") as f:
            for k in f:
                if chet:
                    self.Refresh_text.append(k)  #Добавляю в Edit Text строку k
                    
                chet = not chet
        chet = True
        self.Refresh_text.append("-------------------------------------------------------")
        with open(file_path, 'r', encoding="UTF-8") as f:
            for k in f:
                if chet:
                    self.Refresh_text.append(k)  #Добавляю в Edit Text строку k
                    
                chet = not chet

# Запуск самой программы
if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
