from art import computer, radio

MORSE_CODE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
              "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
              "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..",
              "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
              "8": "---..", "9": "----.", "0": "-----",
              ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.",
              "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
              "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
              }


def to_morse():
    original_message = input("Enter text to translate to morse code:\n")

    translated_morse_list = []
    for char in original_message:
        try:
            translated_morse_list.append(MORSE_CODE[char.upper()])
        except KeyError:
            pass

    translated_message = " ".join(translated_morse_list)
    print(translated_message)


def get_key_from_value(val):
    return [key for (key, value) in MORSE_CODE.items() if value == val][0]


def to_english():
    original_message = input("Enter morse code to translate to English:\n").split(" ")

    translated_english_list = []
    for char in original_message:
        try:
            translated_english_list.append(get_key_from_value(char))
        except KeyError:
            pass

    translated_message = " ".join(translated_english_list)
    print(translated_message)


def selection():
    translate = input("Would you like to translate to ENGLISH or MORSE ?:\n").upper()
    if translate == "ENGLISH":
        to_english()
    elif translate == "MORSE":
        to_morse()
    else:
        print("Invalid input, please enter ENGLISH or MORSE")
        selection()


continue_translating = True
while continue_translating:
    print(radio)
    selection()

    continue_ = input("\nContinue translating? Y/N\n").upper()
    if continue_ == "N":
        print("Thank you for using the morse code translator, have great day!")
        continue_translating = False
