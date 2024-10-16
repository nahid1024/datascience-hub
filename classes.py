class Data:
    def __init__(self, name, age) -> None:
        self.old = age
        self.title = name
    def func(self, val):
        print(self.old, self.title, val)
    def func2(self, val):
        self.func("12")

p1 = Data("Nahid", 12)
p1.func2("nann")