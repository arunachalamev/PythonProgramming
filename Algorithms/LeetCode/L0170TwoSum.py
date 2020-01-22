class TwoSum:
    def __init__(self):
        self.data = {}

    def add(self,number):
        if number in self.data:
            self.data[number] += 1
        else:
            self.data[number] = 1

    def find(self,value):

        for x in self.data.keys():
            y = value-x
            if y != x:
                if y in self.data:
                    return True
            elif self.data[x] > 1:
                return True

        return False

obj = TwoSum()
obj.add(1)
obj.add(3)
print(obj.find(4))
print(obj.find(7))

