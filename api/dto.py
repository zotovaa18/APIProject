class WeakPointDTO:
    def __init__(self, name_les: str, completed: int, total: int, data: list):
        self.name_les = name_les
        self.completed = completed
        self.total = total
        self.data = data


class WeakExerciseDTO:
    def __init__(self, count: int, type_les: str):
        self.count = count
        self.type = type_les
