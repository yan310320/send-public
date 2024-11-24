from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as qt
import bot_

app = qt.QApplication([])
window = qt.QWidget()

window.setWindowTitle("Send by @odigt")
window.resize(700, 510)

main_layout = qt.QVBoxLayout()
id_layout = qt.QHBoxLayout()
msg_layout = qt.QHBoxLayout()
send_btn_layout = qt.QHBoxLayout()
info_layout = qt.QHBoxLayout()
main_layout.addLayout(info_layout)
main_layout.addLayout(id_layout)
main_layout.addLayout(msg_layout)
main_layout.addLayout(send_btn_layout)


chat_id_field = qt.QLineEdit()
msg_text_field = qt.QTextEdit()
send_button = qt.QPushButton("Отправить сообщение")

info_layout.addWidget(qt.QLabel("Программа для отправки сообщения в Telegram-бота [УКАЗАТЬ ЮЗЕРНЕЙМ БОТА]\nПеред отправкой сообщения прочитайте инструкцию в боте.\nВведите данные и отправьте сообщение!"))
id_layout.addWidget(qt.QLabel("ID чата: "))
id_layout.addWidget(chat_id_field)
msg_layout.addWidget(qt.QLabel("Ваше сообщение: "))
msg_layout.addWidget(msg_text_field)
send_btn_layout.addWidget(send_button)




def send_msg():
    global chat_id
    global msg_text
    chat_id = str(chat_id_field.text())
    msg_text = msg_text_field.toPlainText()
    with open(file="ids.txt", mode="r", encoding="utf-8") as ids:
        ids_ = ids.read()
    ids_list = ids_.split("\n", -1)
    if chat_id in ids_list:
        bot_.send_msg_(chatid=int(chat_id), text_msg=msg_text)
        suc_alert = qt.QMessageBox()
        suc_alert.setText(f"Сообщение успешно отправлено для ID {chat_id}:\n\n{msg_text}")
        suc_alert.exec()
    else:
        fail_alert = qt.QMessageBox()
        fail_alert.setText(f"Сообщение не отправлено. ID {chat_id} не зарегистрирован. Пожалуйста, следуйте инструкциям из бота.")
        fail_alert.exec()
    
          
send_button.clicked.connect(send_msg)



window.setLayout(main_layout)

window.show()
app.exec()