class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def grade(self):
        if self.mark>=90:
            print(self.name,"got on A grade")
        if self.mark>=75:
            print(self.name,"got on B grade")
        else:
            print(self.name,"got a C grade")
s1=Student("Anu",92)
s2=Student("Rahul",80)
s3=Student("Meera",60)
s1.grade()
s2.grade()
s3.grade()
