# coding: utf-8
from kivy.properties import ObjectProperty, ListProperty, \
    StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from behaviour import BehaviourContent
from evaluation import EvaluationContent
from menu import Menu
from settings import SettingsContent


class Root(BoxLayout):
    menu = ObjectProperty()
    contents = ListProperty()
    _active_content = ObjectProperty()
    _active_class = StringProperty()
    skills_output = ObjectProperty(JsonStore("data/skills.json"))
    behave_output = ObjectProperty(JsonStore("data/behave.json"))

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.app = kwargs.get('app')
        self.skills = kwargs.get('skills')
        self.student_list = kwargs.get('student_list')
        self.class_list = set([c.student_level for c in self.student_list])
        self.settings = SettingsContent(class_list=self.class_list,
                                        root_instance=self)
        evaluation = EvaluationContent(student_list=self.student_list,
                                       skills=self.skills)
        behaviour = BehaviourContent(student_list=self.student_list)
        self.contents = [self.settings, evaluation, behaviour]
        self.menu = Menu()
        self.add_widget(self.menu)
        self.add_widget(self.settings)
        self._active_content = self.settings
        self.settings.start()

    def get_active_content(self):
        return self._active_content

    def set_active_content(self, new_content):
        self.remove_widget(self._active_content)
        for c in self.contents:
            if c.name == new_content:
                self.add_widget(c)
                self._active_content = c

    active_content = property(get_active_content,
                              set_active_content)

    def get_active_class(self):
        return self._active_class

    def set_active_class(self, new_class):
        new_list = []
        for st in self.student_list:
            if st.student_level == new_class:
                new_list.append(st)
        for ch in self.contents:
            try:
                ch.student_list = new_list
            except AttributeError:
                pass
            try:
                ch.active_class = new_class
            except AttributeError:
                pass
        self._active_class = new_class

    active_class = property(get_active_class,
                            set_active_class)

    def format_students_skills(self):
        string = ''
        for student in self.skills_output.keys():
            string += student + u"\n"
            skill = self.skills_output.get(student)
            for title, grade in skill.items():
                string += u" -{} {}\n".format(title, str(grade))
        return string

    def format_students_behaviour(self):
        string = ''
        for student in self.behave_output.keys():
            string += student + u"\n"
            behaviour = self.behave_output.get(student)
            for time, nature in behaviour.items():
                string += u" -{} {}\n".format(nature, time)
        return string

    def gather_data(self):
        skills = self.format_students_skills()
        behave = self.format_students_behaviour()
        data = u"Compétences :\n\n{}\n\nAttitude :\n\n{}".format(skills,
                                                                 behave)
        return self.app.export_data(data)

    def clear_students_skills(self):
        for key in self.skills_output.keys():
            self.skills_output.delete(key)
        return ''

    def clear_students_behaviour(self):
        for key in self.behave_output.keys():
            self.behave_output.delete(key)
        return ''
