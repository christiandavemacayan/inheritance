class Educator:
    def __init__(self, name):
        self.name = name

    def prepareLesson(self):
        print(f"{self.name} is preparing a general lesson.")

class ITInstructor(Educator):
    def __init__(self, name):
        super().__init__(name)

    def prepareLesson(self):
        print(f"{self.name} is preparing a technical lesson focused on coding.")

    def teachCoding(self):
        print(f"{self.name} is teaching coding concepts.")

class DatabaseInstructor(ITInstructor):
    def __init__(self, name):
        super().__init__(name)

    def teachCoding(self):
        print(f"{self.name} is teaching coding concepts with a focus on integrating SQL with Python.")

    def demonstrateMySQL(self):
        print(f"{self.name} is demonstrating MySQL database operations.")

# Example usage
if __name__ == "__main__":
    educator = Educator("Alice")
    educator.prepareLesson()

    it_instructor = ITInstructor("Bob")
    it_instructor.prepareLesson()
    it_instructor.teachCoding()

    db_instructor = DatabaseInstructor("Charlie")
    db_instructor.prepareLesson()
    db_instructor.teachCoding()
    db_instructor.demonstrateMySQL()