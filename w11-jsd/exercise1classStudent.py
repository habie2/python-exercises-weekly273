class Student:
    def __init__(self, name: str, surname: str, programming_mark, algebra_mark,
    calculus_mark, physics_mark, skills_mark, humanities_mark):
        self.name = name
        self.surname = surname

        if programming_mark >= 0 and programming_mark <= 10:
            self.programming_mark = programming_mark
        else:
            self.programming_mark = 0

        if algebra_mark >= 0 and algebra_mark <= 10:
            self.algebra_mark = algebra_mark
        else:
            self.algebra_mark = 0
            
        if calculus_mark >= 0 and calculus_mark <= 10:
            self.calculus_mark = calculus_mark
        else:
            self.calculus_mark = 0
        
        if physics_mark >= 0 and physics_mark <= 10:
            self.physics_mark = physics_mark
        else:
            self.physics_mark = 0

        if skills_mark >= 0 and skills_mark <= 10:
            self.skills_mark = skills_mark
        else:
            self.skills_mark = 0
            
        if humanities_mark >= 0 and humanities_mark <= 10:
            self.humanities_mark = humanities_mark
        else:
            self.humanities_mark = 0

    def __str__(self):
        result = (f"""
name: {self.name}
surname: {self.surname}
programming mark: {self.programming_mark}
algebra mark: {self.algebra_mark}
calculus mark: {self.calculus_mark}
physics mark: {self.physics_mark}
skills mark: {self.skills_mark}
humanities mark: {self.humanities_mark}
        """
        )
        return result
