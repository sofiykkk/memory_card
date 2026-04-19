from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel
from random import *
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



question_list = []
question_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Испанский', 'Бразильский', 'Английский'))
question_list.append(Question('Какого цвета нет во флаге РФ?', 'зеленый', 'синий', 'красный', 'белый'))
question_list.append(Question('Какого цвета нет во флаге США?', 'зеленый', 'синий', 'красный', 'белый'))
question_list.append(Question('Какой континент самый большой?', 'Евразия', 'СА', 'ЮА', 'Австралия'))
question_list.append(Question('Какого цвета нет во флаге Китая?', 'зеленый', 'оранжевый', 'красный', 'жёлтый'))
question_list.append(Question('Какой язык интернациональный?', 'Английский', 'Русский', 'Французский', 'Итальянский'))
question_list.append(Question('Какая страна самая маленькая?', 'Ватикан', 'Россия', 'Франция', 'Италия'))
question_list.append(Question('Какой язык самый сложный?', 'Китайский', 'Русский', 'Французский', 'Испанский'))
question_list.append(Question('Какой язык самый популярный?', 'Английский', 'Русский', 'Французский', 'Итальянский'))




app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.show()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)



def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

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
        window.score += 1
        print('Статистика\n всего вопроов:', window.total, '\n-Правильных ответов', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг:', (window.score/window.total*100))
    
    


def next_question():
    window.total += 1
    print('Статистика\n всего вопроов:', window.total, '\n-Правильных ответов', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(600,600)
window.show()

app.exec()
