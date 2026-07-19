import re, random
from colorama import Fore, Style , init

init(autoreset=True)

destinations= {
    "mountains" : ["Shimla", "Mussorie", "Nepal", "Madhya Pradesh", "Ladakh"],
    "beaches" : ["Goa", "Thailand", "Andaman", "Bali", "Maldives", "USA"], 
    "cities" : ["Delhi", "Mumbai", "Kolkata", "New York", "Paris", "Berlin", "London"]
}

Jokes= ["Why dont Programmers Like Nature, Because they too many bugs", 
        "Why did the computer go to the Doctor, Because is had a virus!",
        "Why do travelers always feel warm, Because of all their hot spots"]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def reccomend():
    print(Fore.CYAN + "Bot: Beaches, Mountains or Cities?")
    preference=input(Fore.YELLOW + "You: ")
    preference= normalize_input(preference)

    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.GREEN + f"Bot: how about {suggestion} ?")
        print(Fore.CYAN + "Bot: Do you like it \n Yes or No")

        answer=input(Fore.YELLOW + "You: ").lower()
        if answer=='yes':
            print(Fore.GREEN + f"Bot: Enjoy your {suggestion}")
        elif answer=='no':
            print(Fore.RED + "Bot: Lets try another one")
            reccomend()
        else:
            print(Fore.RED + "Bot: I suggest another one")
            reccomend
    else:
        print(Fore.RED + "Bot: Sorry i dont have that kind of desttination")
        reccomend()

def packing():
    print(Fore.CYAN + "Bot: Where to?")
    location=normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "Bot: How many days?")
    days=input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"Bot: Packing tips for {location} and {days} days: \n - Pack Versatile Clothes. \n - Pack a charger. \n - Check the forecast beforehand. ")

def tell_joke():
    print(Fore.YELLOW + f"Bot: {random.choice(Jokes)}")

def show_help():
    print(Fore.MAGENTA + "Bot: I can: ")
    print(Fore.GREEN + "- Tell a travel spot(say reccomendation). \n- Give packing tips(say packing). \n- Tell Jokes(say jokes).")
    print(Fore.CYAN + ("Bot: Type exit or bye to end."))

def chat():
    print(Fore.CYAN + "Bot: I am your chatbot")
    print(Fore.GREEN + "Bot: Whats Your name.")
    name=input(Fore.YELLOW + ("You: "))
    print(Fore.CYAN + f"Nice to meet you {name}")

    show_help()

    while True:
        user_input= normalize_input(input(Fore.YELLOW + name + ": "))
        if "reccomendation" in user_input:
            reccomend()
        elif "packing" in user_input:
            packing()
        elif "jokes" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" or "bye" in user_input:
            print(Fore.CYAN + f"Safe travels {name}")
            break
        else:
            print(Fore.RED + "Bot: Could you rephrase")

if __name__ == '__main__':
    chat()