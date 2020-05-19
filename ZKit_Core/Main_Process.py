import random
import string


def random_string(*size):
    size = random.randint(2, 9)
    chars = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(size))


def random_int(size, max, min):
    ints = string.digits
    while True:
        random_int = ''.join(random.choice(ints) for _ in range(size))
        if random_int <= max and random_int >= min:
            return random_int
        else:
            pass


def random_ip():
    dot = "."
    Result = random_int(4, 255, 1) + dot + random_int(4, 255, 1) + \
        dot + random_int(4, 255, 1) + dot + random_int(4, 255, 1)
    return Result


def Create_File(*self, PATH):
    from colorama import Fore
    Red, Blue, Green, Reset = Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.RESET
    from time import sleep as Sleep
    print("[" + Green + "!" + Reset + "]" + Reset + "Creating File...", end="")
    try:
        f = open(PATH, "x").close()
    except FileExistsError:
        Sleep(0.5)
        choice = str(input(
            "\r[" + Red + "-" + Reset + "]" + Reset + "Creating File...Failed \nFile Already Exists Confirm Overwrite : (N or Y)"))
        Choice = choice.upper()
        if Choice == "Y":
            return PATH
        elif Choice == "N":
            file_name = str(input("Write Down File Name Here : "))
            file_name += ".pyw"

            return file_name
        else:
            print(Red + "\r[!]" + Reset + "In Valid Input", end="")
            return ''
    else:
        file_name = PATH
        print("\r[" + Blue + "+" + Reset + "]" +
              Reset + "Creating File...Done", end="")
        return file_name


def Anti_Anti_Virus(*self, Count):
    from colorama import Fore
    Red, Blue, Green, Reset = Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.RESET
    from time import sleep as Sleep
    print("[" + Green + "!" + Reset + "]" +
          "Generating Random String To Decrease AV Ditection...", end="")
    Sleep(0.2)
    try:
        Result = tuple()
        for i in range(0, Count):
            Result = Result + (random_string(), )
    except:
        print("\r[" + Red + "-" + Reset + "]" +
              "Generating Random String To Decrease AV Ditection...Failed ", end="")
        Sleep(1)
        print("\r[" + Green + "!" + Reset + "]" +
              "Generating Random String To Decrease AV Ditection...Failed -> Passed")
        Sleep(0.2)
        return False
    else:

        print("\r[" + Blue + "+" + Reset + "]" +
              "Generating Random String To Decrease AV Ditection...Done")
        return Result
