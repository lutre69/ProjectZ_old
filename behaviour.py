# coding: utf8
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from popups import StudentPopupLayout
from datetime import datetime


class BehaviourContent(FloatLayout):
    name = StringProperty('Comportement')
    active_student = StringProperty(u'Elève')

    def __init__(self, student_list, **kwargs):
        super(BehaviourContent, self).__init__(**kwargs)
        self.student_list = student_list

    def open_student_popup(self):
        Popup(content=StudentPopupLayout(cols=2,
              student_list=self.student_list,
              caller=self),
              title='Faites votre choix',
              auto_dismiss=False).open()

    def set_student_disobedience(self, name, nature):
        month = datetime.now().month
        day = datetime.now().day
        hour = datetime.now().hour
        minute = datetime.now().minute
        sec = datetime.now().second
        time = u'{}/{} {}:{}:{}'.format(day, month, hour, minute, sec)
        dic = {}
        if self.parent.behave_output.exists(name):
            dic = self.parent.behave_output[name]
        dic[time] = nature.decode('utf-8')
        self.parent.behave_output.put(name, **dic)
