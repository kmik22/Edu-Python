class Player(object):
    score = None
    age = None

    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        if self.score is not None:
            return f"Player {self.name} {self.last_name} -> {self.score}.\n"
        else:
            return f"Player {self.name} {self.last_name}.\n"

    def __str__(self):
        if self.score is not None:
            return f"Player {self.name} {self.last_name} -> {self.score}.\n"
        else:
            return f"Player {self.name} {self.last_name}.\n"

    def set_score(self, value) -> bool:
        if value >= 0:
            self.score = value
            return True
        else:
            print("Invalid Value")
            return False

    def set_age(self, age) -> bool:
        if age >= 0:
            self.age = age
            return True
        else:
            print("Invalid Value")
            return False

    def get_dict_repr(self):
        return {
            "Name": self.name,
            "Last name": self.last_name,
            "Score": self.score
        }


if __name__ == "__main__":  # класс работает только в этом файле - уточнить! В телеге доп.инфа.
    a = Player("Sergey", "Bubka")
    a.set_score(615)
    print(a.score)
    print(dir(a))
    print(a)
