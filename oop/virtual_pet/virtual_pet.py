class Pet:
    def __init__(self, petName, type):
        self.petName = petName
        self.bored = 0
        self.hunger = 0
        self.intelligence = 1
        self.type = type

    def feed(self):
        self.hunger = 0
        print("Hunger is at " + str(self.hunger) + "%. Hunger is eliminated!")

    def play(self):
        self.bored = 0
        print("Boredom is at " + str(self.bored) + "%. Boredom is eliminated!")

    def read(self):
        self.intelligence = self.intelligence * 1.006
        print("Intelligence is at " + str(self.intelligence) + "%.")

    def output_greeting(self):
        print("Hello user! My name is " + self.petName + " and I am a " + self.type )

    def get_boredom(self):
        return self.bored

    def get_intelligence(self):
        return self.intelligence

    def get_type(self):
        return self.type

    def get_hunger(self):
        return self.hunger




pet = Pet("Fred", "Tiger")
pet.output_greeting()
pet.feed()
pet.play()
pet.read()



