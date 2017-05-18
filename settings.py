# coding: utf8
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock
from popups import ClassPopupLayout, NumberPopupLayout


class SettingsContent(FloatLayout):
    """This class represents the Settings screen
    
    
    attributes:
        - 'name' is a StringProperty used by the Menu class in order to
        display it.
        - 'active_class' is a StringProperty that is used on a label to
        show the user which class is active.
        - 'class_list' is the list of classes passed to the object when
        it is created, it's used by the class popup when the user has
        made a choice.
        
    methods:
        - 'open_class_popup' opens a popup for the user to pick a class.
        - 'clear_student_skills' is erasing all data from the 
        'skills_output' concerning the evaluations on students.
        - 'clear_student_behaviour' is erasing all data from the
        'behave_output' concerning the behaviour of students.
        - 'display_student_skills' displays the evaluations that are 
        stored in 'skills_output'.
        - 'display_student_behaviour' displays the disobedience that are 
        stored in 'behave_output'.
        
    This class's parent is a Root class.
    
    """
    name = StringProperty('Accueil')
    active_class = StringProperty('Choisir une classe')
    random_students = ListProperty()

    def __init__(self, **kwargs):
        super(SettingsContent, self).__init__(**kwargs)
        self.root_instance = kwargs.get('root_instance')

    def start(self):
        Clock.schedule_once(self.open_class_popup)

    def open_class_popup(self, dt):
        Popup(content=ClassPopupLayout(cols=2,
              class_list=self.root_instance.class_list,
              caller=self),
              title='Faites votre choix',
              size_hint_y=0.2,
              size_hint_x=0.8,
              auto_dismiss=False).open()

    def random_pick_popup(self, label_instance):
        self.popup = Popup(content=NumberPopupLayout(cols=4,
                           label_instance=label_instance,
                           caller=self,
                           root_instance=self.root_instance),
                           title="Nombre d'élèves à tirer au sort",
                           size_hint_y=0.4,
                           size_hint_x=0.8,).open()



