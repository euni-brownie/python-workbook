class Student :
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = float(korean)
        self.english = float(english)
        self.math = float(math)
    
    def get_total_score(self):
        return self.korean+self.english+self.math
    
    def get_average(self):
        return self.get_total_score() / 3.0
    
    