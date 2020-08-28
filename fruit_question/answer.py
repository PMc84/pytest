list_a = ['Orange', 'Apple', 'Raspberry', 'Pear']
list_b = ['Strawberry', 'Apple', 'pear' 'Peach']


class FruitList:
    fruit = []

    def __init__(self, fruit):
        # Let's make sure the fruit list is lowercase or else shit may not match.
        for i in fruit:
            self.fruit.append(i.lower())
        return

    def print(self):
        for i in self.fruit:
            print(i)


list_one = FruitList(list_a)
list_one.print()
