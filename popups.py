# coding: utf8
from random import sample
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class ClassPopupLayout(GridLayout):

    def __init__(self, **kwargs):
        super(ClassPopupLayout, self).__init__(**kwargs)
        self.class_list = kwargs.get('class_list')
        self.caller = kwargs.get('caller')
        map(self.add_button, self.class_list)

    def add_button(self, element):
        button = Button(text=element, font_size='20sp', bold=True)
        self.add_widget(button)
        button.bind(on_release=self.select)

    def select(self, obj):
        self.caller.parent.active_class = obj.text
        self.parent.parent.parent.dismiss()


class SkillsPopupLayout(GridLayout):
    def __init__(self, skills_list, **kwargs):
        super(SkillsPopupLayout, self).__init__(**kwargs)
        self.skills_list = skills_list
        self.caller = kwargs.get('caller')
        map(self.add_button, [s[0] for s in self.skills_list])

    def add_button(self, element):
        button = Button(text=element, font_size='20sp', bold=True)
        self.add_widget(button)
        button.bind(on_release=self.select)

    def select(self, obj):
        selection = filter(lambda x: x[0] == obj.text, self.skills_list)[0]
        self.caller.skill_title, self.caller.skill_summary = selection
        self.parent.parent.parent.dismiss()


class StudentPopupLayout(GridLayout):
    def __init__(self, **kwargs):
        super(StudentPopupLayout, self).__init__(**kwargs)
        self.student_list = kwargs.get('student_list')
        self.caller = kwargs.get('caller')
        for s in self.student_list:
            button = Button(text=s.student_name)
            self.add_widget(button)
            button.bind(on_release=self.select)

    def select(self, obj):
        self.caller.active_student = obj.text
        self.parent.parent.parent.dismiss()


class NumberPopupLayout(GridLayout):
    def __init__(self, **kwargs):
        super(NumberPopupLayout, self).__init__(**kwargs)
        self.label_instance = kwargs.get('label_instance')
        self.caller = kwargs.get('caller')
        self.root_instance = kwargs.get('root_instance')
        for x in range(16):
            button = Button(text=str(x+1))
            self.add_widget(button)
            button.bind(on_release=self.select)

    def select(self, obj):
        name_list = [s.student_name for s in self.root_instance.student_list
                     if s.student_level == self.caller.active_class]
        pick = "\n".join(sample(name_list, int(obj.text)))
        self.label_instance.text = pick
        self.caller.popup.dismiss()
