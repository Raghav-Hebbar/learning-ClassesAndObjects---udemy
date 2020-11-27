class English():
    def greet(self, name):
        print("Hello",name)

class French():
    def greet(self, name):
        print("Bonjour",name)

def greetings(language, name):
    language.greet(name)

french = French()
english = English()

greetings(english,"Raghav")
greetings(french,"Raghav")
