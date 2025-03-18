class EsportsEvent:
    def __init__(self, event_date):
        self.event_date = event_date

    def scheduleMatch(self):
        print(f"Match scheduled on {self.event_date}.")

class StudentDivision(EsportsEvent):
    def __init__(self, event_date):
        super().__init__(event_date)

    def registerTeam(self, team_name):
        print(f"Team '{team_name}' has been registered in the Student Division.")

class FacultyDivision(EsportsEvent):
    def __init__(self, event_date):
        super().__init__(event_date)

    def assignReferee(self, referee_name):
        print(f"Referee '{referee_name}' has been assigned to the Faculty Division.")

# Example usage
if __name__ == "__main__":
    event_date = "2023-11-15"
    
    esports_event = EsportsEvent(event_date)
    esports_event.scheduleMatch()

    student_division = StudentDivision(event_date)
    student_division.scheduleMatch()
    student_division.registerTeam("Team Alpha")

    faculty_division = FacultyDivision(event_date)
    faculty_division.scheduleMatch()
    faculty_division.assignReferee("Referee John")