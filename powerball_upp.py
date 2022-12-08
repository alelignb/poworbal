import colorama
from colorama import Fore
colorama.init(autoreset=True)
# we are import class from file read me
from powerball_utiles import ReadMePower


class condation:
    #  object [get_powerball_class] gives us Access to get all method created in the class PowerBoll
    get_powerball_class = ReadMePower("", "")

    print(Fore.GREEN + "You Think you have lucky let's Tray")
    print("---------------------------------")
    # we're Declare Variables they takin all method created in the class PowerBoll by object [get_powerball_class]
    lucky_numbers = get_powerball_class.power_ball()
    user_lucky_nums = get_powerball_class.user_numbers()
    user_strong = get_powerball_class.get_user_strong()
    ball_strong = get_powerball_class.get_ball_strong()

    #  here Declare counter
    count_numbers = 0

    # this is output when the program end should Appear
    print("---------------------------------------")
    print(Fore.GREEN+str ("Today's Powerball Winning Numbers:\n") ,
          Fore.MAGENTA+str (lucky_numbers), "",Fore.YELLOW+ str( ball_strong))
    print(Fore.MAGENTA+str("Your lucky numbers:\n"),Fore.MAGENTA+str( user_lucky_nums),
          "",Fore.YELLOW+str( user_strong))
    for lucky in lucky_numbers:
        for user in user_lucky_nums:
            if user == lucky:
                count_numbers = count_numbers + 1
    print("------------------")

    # we are show for user how math numbers found in the game powerball
    if count_numbers == 0:
        print("The Amount of numbers you found =", count_numbers)
    else:
        print("The Amount of numbers you found =", count_numbers)
    print("-----------------------")

    # Here all action this is condition show for user results when the program end
    if count_numbers == 5 and user_strong == ball_strong:
        print(count_numbers, "Correct While Balls And the powerball:324,000,000$")

    elif count_numbers == 5 and user_strong != ball_strong:
        print(count_numbers, "Correct While Balls Not powerball:1,000,000$")

    elif count_numbers == 4 and user_strong == ball_strong:
        print(count_numbers, "Correct While Balls And the powerball:", 10 * 1000, "$")

    elif count_numbers == 4 and user_strong != ball_strong:
        print(count_numbers, "Correct While Balls Not powerball:", 1 * 100, "$")

    elif count_numbers == 3 and user_strong == ball_strong:
        print(count_numbers, "Correct While Balls And the powerball:", 1 * 100, "$")

    elif count_numbers == 3 and user_strong != ball_strong:
        print(count_numbers, "Correct While Balls Not powerball:", 1 * 7, "$")

    elif count_numbers == 2 and user_strong == ball_strong:
        print(count_numbers, "Correct While Balls And the powerball:", 1 * 7, "$")

    elif count_numbers == 1 and user_strong == ball_strong:
        print(count_numbers, "Correct While Balls And the powerball:", 1 * 4, "$")

    elif count_numbers == 0 and user_strong == ball_strong:
        print(count_numbers, "Correct While Balls And the powerball:", 1 * 4, "$")

    else:
        print(Fore.RED+str("Please tray again! you didn't get points"))


condationn = condation()