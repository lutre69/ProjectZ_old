# coding: utf8


class Skills(object):
    """This class contains the skills that you wish to evaluate.
    
    
    It's a dynamic class so you can give it any attribute you want,
    but the way the program works, yous should give it the title of
    the skill as the name of the attribute, and the summary of this
    skill as a value, all of them have to be strings.
    
    The instance of this class is called when the app starts during
    its build method.
    
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Student(object):

    def __init__(self, **kwargs):
        self.student_name = kwargs.get('name')
        self.student_surname = kwargs.get('surname')
        self.student_level = kwargs.get('level')
