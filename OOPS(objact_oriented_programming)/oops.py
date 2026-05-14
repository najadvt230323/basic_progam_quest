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
