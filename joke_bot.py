
PROMPT = input("What do you want? ").strip().lower()
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her:\nget a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk.\nThe programmer asks why and Sophia replies: 'because they had eggs'."
SORRY = "Sorry, I only tell jokes."

def main():
    if "joke" in PROMPT:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == '__main__':
    main()
