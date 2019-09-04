class School():
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = {}

    def add_student(self, full_name, grade_level):
        if grade_level in self.roster:
            self.roster[grade_level].append(full_name)
        else:
            self.roster[grade_level] = [full_name]

        # Could also be written as:
        # self.roster[grade_level] = self.roster.get(grade_level, []).append(full_name)
        
    def grade(self, grade_level):
        return self.roster[grade_level]
    
    def sort_roster(self):
        sorted_dict = self.roster
        for key in sorted_dict:
            sorted_dict[key].sort()
        return sorted_dict