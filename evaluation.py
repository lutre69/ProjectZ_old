# coding: utf8
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from popups import StudentPopupLayout, SkillsPopupLayout


class EvaluationContent(BoxLayout):
    name = StringProperty('Evaluation')
    active_student = StringProperty(u'Elève')
    skill_title = StringProperty(u'Compétence')
    skill_summary = StringProperty(u'Description')

    def __init__(self, student_list, skills, **kwargs):
        super(EvaluationContent, self).__init__(**kwargs)
        self.student_list = student_list
        self.skills = skills

    def open_student_popup(self):
        Popup(content=StudentPopupLayout(cols=2,
              student_list=self.student_list,
              caller=self),
              title='Faites votre choix',
              auto_dismiss=False).open()

    def open_skills_popup(self):
        skills_list = ([(title, summary) for (title, summary)
                        in self.skills.__dict__.items()])
        Popup(content=SkillsPopupLayout(cols=2,
              skills_list=skills_list,
              caller=self),
              title='Faites votre choix',
              size_hint_y=0.5).open()

    def set_student_skill(self, name, skill, value):
        dic = {}
        name = name
        skill = skill
        if self.parent.skills_output.exists(name):
            dic = self.parent.skills_output[name]
        dic[skill] = value
        self.parent.skills_output.put(name, **dic)
