# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
 
# # Створюємо программу
# app = QApplication([])
 
# # створюємо головне вікно
# main_win = QWidget()
 
# # Заголовок вікна
# main_win.setWindowTitle("Проект")
# main_win.setFixedWidth(500)
# main_win.setFixedHeight(500)
 
# # Віджети
# but1 = QPushButton("PHP")
# but2 = QPushButton("JavaScript")
# but3 = QPushButton("Python")
# but4 = QPushButton("Pascal")
# but5 = QPushButton("SQL")
# but6 = QPushButton("C++")
 
# # Розмітка(вертикальна)
# line = QVBoxLayout()
 
 
# # віджети на розмітку
# line.addWidget(but1, alignment=Qt.AlignLeft)
# line.addWidget(but2, alignment=Qt.AlignRight)
# line.addWidget(but3, alignment=Qt.AlignLeft)
# line.addWidget(but4, alignment=Qt.AlignRight)
# line.addWidget(but5, alignment=Qt.AlignLeft)
# line.addWidget(but6, alignment=Qt.AlignRight)
 
 
# # Розмітка головного вікна
# main_win.setLayout(line)
 
 
# # Запускаємо головне вікно та програму
# main_win.show()
# app.exec_()



from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton
 
# Створюємо программу
app = QApplication([])
 
# створюємо головне вікно
main_win = QWidget()
 
# Заголовок вікна
main_win.setWindowTitle("Проект")
main_win.setFixedWidth(500)
main_win.setFixedHeight(500)
 
# Віджети
but1 = QRadioButton("1")
but2 = QRadioButton("2")
but3 = QRadioButton("3")
but4 = QPushButton("Перевірити число")

def show_number():
    if but4 
# Розмітка(вертикальна)
line = QVBoxLayout()
 
 
# віджети на розмітку
line.addWidget(but1, alignment=Qt.AlignLeft)
line.addWidget(but2, alignment=Qt.AlignLeft)
line.addWidget(but3, alignment=Qt.AlignLeft)
line.addWidget(but4, alignment=Qt.AlignCenter)
 

# Розмітка головного вікна
main_win.setLayout(line)
 
 
# Запускаємо головне вікно та програму
main_win.show()
app.exec_()



