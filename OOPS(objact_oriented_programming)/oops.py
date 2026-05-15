class Student:
    def exam(self):
        print("exam conducted on 11-05-26")
    def study(self,name):
        self.n=name
        print(f"hi {self.n}")

print(type(Student))

richu=Student()
print(type(richu))
print(id(richu))

shabin=Student()
print(type(shabin))
print(id(shabin))

print()
richu.exam()
richu.study("najad")
# --------------------------------------------------
class Student1 :
    school="quest"

richu=Student1()
najad=Student1()

print(Student1.school)
print(Student1().school)
print(richu.school)
print(najad.school)

print()
Student1.school="quest inovashion"
print(Student1.school)
print(richu.school)
print(najad.school)

print()
richu.school="kunnamagalam hss"
print(Student1.school)
print(richu.school)
print(najad.school)

print()
del richu.school
print(Student1.school)
print(richu.school)
print(najad.school)


print()
richu.school="kunnamagalam hss"
del Student1.school
# print(Student1.school)           # AttributeError: type object 'Student1' has no attribute 'school'
print(richu.school)                # kunnamagalam hss
# print(najad.school)                # AttributeError: 'Student1' object has no attribute 'school'






