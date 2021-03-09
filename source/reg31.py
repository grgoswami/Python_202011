
class StudentReportCard:
    def __init__(self, name, middle_name, grade):
        self.name = name
        self.middle_name = middle_name
        self.grade = grade        
        self.report_card = {}
        
    def add_grade_unit(self, subject, grade_unit):
        self.report_card[subject] = grade_unit
        
    def show_report_card(self):
        print(f'This is the report card for {self.name}, {self.middle_name}')
        print(f'{self.name} goes to grade {self.grade}')
        for subject, grade_unit in self.report_card.items():
            print(f'{subject}: {grade_unit}')
            
s0 = StudentReportCard('Jane Doe', 'TheGreat', 1)
s0.add_grade_unit('Math', 95)
s0.add_grade_unit('English', 90)
s0.add_grade_unit('Art', 93)
s0.show_report_card()

s1 = StudentReportCard('John Doe', 'TheAwesome', 2)
s1.add_grade_unit('Math', 90)
s1.add_grade_unit('English', 95)
s1.add_grade_unit('Art', 93)
s1.show_report_card()





            
        
        
        
    