# import ruandom colores
import colorama
colorama.init(autoreset=True)
import random

class  ReadMePower: #generet class
    # This constructor the attribute
    def __init__(self, lottery, count):
        self.lottery = lottery
        self.count = count
    # This method checking if random numbers not Duplicated and remove Duplicated
    def power_ball(self):
        lotto_numbers = []
        while True:
            numbers = random.randint(1, 20)
            if numbers not in lotto_numbers:
                lotto_numbers.append(numbers,)
                lotto_numbers.sort()
            if len(lotto_numbers) == 5:
                break
        return lotto_numbers

    # This method is only giving from User lucky numbers
    def user_numbers(self):
        user_number = []
        for num in range(5):
           # Generet rundom number to upend the users number
            user_num=random.randint(1,20)

            user_number.append(user_num)
            user_number.sort()
        return user_number

    # this method is we're taking random number strong
    def get_ball_strong(self):
        rand = random.randint(1, 7)
        return rand

    # this method is we're taking strong number from user
    def get_user_strong(self):
       ball=random.randint(1,7)
       return ball


