# coding: utf8
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from properties import Skills, Student
from root import Root


class ProjectZApp(App):
    data_input = ObjectProperty(JsonStore('data/inputs.json'))
    
    def build(self):
        student_list = self.get_students()
        skills = Skills(**self.get_skills())
        root = Root(orientation='vertical',
                    skills=skills, app=self,
                    student_list=student_list)
        return root

    def get_students(self):
        student_list = []
        for key in self.data_input.keys():
            if key != 'skills':
                for name, level in self.data_input.get(key).items():
                    student = Student(name=name, level=level)
                    student_list.append(student)
        return student_list

    def get_skills(self):
        dic = self.data_input.get('skills')
        skills = {}
        for title, summary in dic.items():
            skills[title] = summary
        return skills

    def export_data(self, data):
        file_name = 'export.txt'
        path = '/'.join([self.user_data_dir, file_name])
        a_file = open(path, 'w')
        a_file.write(data.encode('utf-8'))
        a_file.close()
        return path

    def on_pause(self):
        return True


if __name__ == '__main__':
    ProjectZApp().run()
