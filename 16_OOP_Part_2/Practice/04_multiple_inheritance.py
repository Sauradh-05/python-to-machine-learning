class Father:
    def father_skill(self):
        print("Father can drive.")


class Mother:
    def mother_skill(self):
        print("Mother can cook.")


class Child(Father, Mother):
    def child_skill(self):
        print("Child can play football.")


child = Child()

child.father_skill()
child.mother_skill()
child.child_skill()