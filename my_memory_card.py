from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
                            QHBoxLayout, QVBoxLayout, QGroupBox, 
                            QRadioButton, QPushButton, QLabel,
                            QButtonGroup)
from random import shuffle, randint

class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Бразильский', 'Итальянский'))
question_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Какой цвет не учавствует в RGB расцветке', 'Белый', 'Красный', 'Синий', 'Зелёный'))

app = QApplication([])

'''Интерфейс приложения Memory Card'''
# Создаем панель вопроса
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('') # текст вопроса


RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')


RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout() 

layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)

layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке


RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)




layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)


layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым




def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score +=1 #УРОК 4
        print('Статистика \n Всего вопросов:',window.total, '\n Правильных ответов:', window.score)#УРОК 4
        print('Рейтинг:', (window.score/window.total * 100), '%')#УРОК 4
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Статистика \n Всего вопросов:',window.total, '\n Правильных ответов:', window.score)#УРОК 4
            print('Рейтинг:', (window.score/window.total * 100), '%')#УРОК 4


def next_question():
    window.total+=1#УРОК 4
    
    cur_question = randint(0,len(question_list)-1)#УРОК 4

    q = question_list[cur_question]#УРОК 4
    ask(q)

def click_ok() :
    ''' определяет, надо ли показывать другой вопрос ли проверить ответ на этот вопрос'''
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()


window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(800, 400)  # Установка размеров окна
window.setLayout(layout_card)




btn_OK.clicked.connect(click_ok) # проверяем, что панель ответов показывается при нажатии на кнопку
window.score = 0 #УРОК 4
window.total = 0 #УРОК 4
next_question()
window.show()
app.exec()
