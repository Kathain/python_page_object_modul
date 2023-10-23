class Cat:
    acceptable_percentage_of_dirty_toilet = 50
    def __init__(self,name,age,castr):
        self.name = name
        self.age = age
        self.castr = castr

    def sound(self):
        print(f"Meowwww {self.name}")

    def need_castr(self):
        if self.castr is False:
            if self.age >= 7:
                return False
            else:
                return True
        else:
            return None

    def pipi_outside_of_toilet(self, percentage_dirty):
        if percentage_dirty >= self.acceptable_percentage_of_dirty_toilet:
            print("Fuuuuu Its dyrty , it'll outside")
        else:
            print("Its norm yet")


if __name__ == '__main__':
    Alex = Cat("Alex",3,True)
    print(Alex.need_castr())
    print(Alex.pipi_outside_of_toilet(44))
