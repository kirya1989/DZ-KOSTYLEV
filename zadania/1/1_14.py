class MyInt:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if self.val == 2 and other.val == 2:
            return MyInt(5)
    
    def __str__(self):
        return str(self.val)
    
class MyList:
    def __init__(self, content):
        content = list(content)
        if len(content) > 10:
            print('Больше 10 нельзя!')
        self.contents = content[:10]

    def append(self, data):
        if len(self.contents) == 10:
            print('Больше 10 нельзя!')
            return

        self.contents.append(data)

    def __str__(self):
        return str(self.contents)
    
class MyUniqueList:
    def __init__(self, content):
        content = list(content)
        self.contents = []

        for elem in content:
            if elem not in self.contents:
                self.contents.append(elem)

    def append(self, data):
        if data not in self.contents:
            self.contents.append(data)

    def __str__(self):
        return str(self.contents)

print(MyInt(2) + MyInt(2))

print(MyList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

ml = MyUniqueList([1, 1, 1, 2, 2, 3, 3, 3, 3, 3])
ml.append(4)
ml.append(1)
print(ml)