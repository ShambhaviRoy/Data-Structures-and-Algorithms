# Best Average Grade
# Given a list of student names and grades, find the best average grade 
# Round average to greatest integer
# Sample input:
# input = [["Archie" , "20"], ["Betty", "30", "5"], ["Veronica", "40"], ["Reggie", "10"], ["Archie", "80"]]
# Best average grade = 50 (scored by Archie)

# Time Complexity = O(n_rows), Space Complexity = O(n_students), n = no. of rows <= no. of students

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.avg = 0

    def calc_avg(self):
        if(len(self.grades) > 0):
            self.avg = sum(self.grades) / len(self.grades)



def best_average_grade(input):
    if len(input) < 1:
        return 0
    students = {} # {"name" : student_obj}
    for row in input:
        if len(row) < 2:
            print('Malformed row, ignore')
        student_name = row[0]
        if student_name not in students:
            student_obj = Student(student_name)
            students[student_name] = student_obj
            student_obj.grades = [float(x) for x in row[1:]]
        else:
            student_obj = students[student_name]
            student_obj.grades.extend([float(x) for x in row[1:]])
        

    # find all averages
    best_avg = float('-inf')
    for name, student in students.items():
        student.calc_avg()
        print(f"Name = {name}, Grades = {student.grades}, Average = {student.avg}")
        if best_avg < student.avg:
            best_avg = student.avg

    return int(best_avg)



input = [["Archie" , "20"], ["Betty", "30", "5"], ["Veronica", "40"], ["Reggie", "10"], ["Archie", "80"]]

print(best_average_grade(input))

        
