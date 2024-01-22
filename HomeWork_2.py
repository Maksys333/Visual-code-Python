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
# but1 = QPushButton("1")
# but2 = QPushButton("2")
# but3 = QPushButton("3")
# but4 = QPushButton("4")
# but5 = QPushButton("5")
 
# # Розмітка(вертикальна)
# line = QVBoxLayout()
# line1 = QHBoxLayout()
# line2 = QHBoxLayout()
 
# # віджети на розмітку
# line.addWidget(but1, alignment=Qt.AlignLeft)
# line.addWidget(but2, alignment=Qt.AlignRight)
# line.addWidget(but3, alignment=Qt.AlignCenter)
# line.addWidget(but4, alignment=Qt.AlignRight)
# line.addWidget(but5, alignment=Qt.AlignLeft)

# line = QVBoxLayout()
 
 
# # Розмітка головного вікна
# main_win.setLayout(line)
 
 
# # Запускаємо головне вікно та програму
# main_win.show()
# app.exec_()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

# Створюємо програму
app = QApplication([])

# створюємо головне вікно
main_win = QWidget()

# Заголовок вікна
main_win.setWindowTitle("Проект")
main_win.setFixedWidth(500)
main_win.setFixedHeight(500)

# Віджети
but1 = QPushButton("1")
but2 = QPushButton("2")
but3 = QPushButton("3")
but4 = QPushButton("4")
but5 = QPushButton("5")

# Розмітка (вертикальна)
main_layout = QVBoxLayout()

# Перший рядок
row1_layout = QHBoxLayout()
row1_layout.addWidget(but1, alignment=Qt.AlignLeft)
row1_layout.addWidget(but2, alignment=Qt.AlignRight)
main_layout.addLayout(row1_layout)

# Другий рядок
row2_layout = QHBoxLayout()
row2_layout.addWidget(but3, alignment=Qt.AlignCenter)
main_layout.addLayout(row2_layout)

# Третій рядок
row3_layout = QHBoxLayout()
row3_layout.addWidget(but4, alignment=Qt.AlignLeft)
row3_layout.addWidget(but5, alignment=Qt.AlignRight)
main_layout.addLayout(row3_layout)

# Встановлюємо головну розмітку в головне вікно
main_win.setLayout(main_layout)

# Запускаємо головне вікно та програму
main_win.show()
app.exec_()

