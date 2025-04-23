class Pet:
    def __init__(self, name, hunger = 5, energy = 5, happiness = 5, pet_type="dog"):
         self.name = name
         self.pet_type = pet_type
         self.hunger = min(max(hunger, 0), 10) 
         self.energy = min(max(energy, 0), 10)
         self.happiness = min(max(happiness, 0), 10)
         self.tricks = []
         self.mood = self.calculate_mood()


    def calculate_mood(self):
        """Calculate the mood based on current status"""     
        avg = (self.happiness + (10 - self.hunger) + self.energy) / 3
        if avg >= 8:
            return "ecstatic 🤩"
        elif avg >= 6:
            return "happy 😊"
        elif avg >= 4:
            return "content 😐"
        elif avg >= 2:
            return "grumpy 😒"
        else:
            return "miserable 😫"

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(self.hunger - 3, 0)
            self.happiness = min(self.happiness + 1, 10)
            print(f"{self.name} is eating.")
        else:
            print(f"{self.name} is not hungry.")
        
    def sleep(self):
        if self.energy < 10:
            self.energy = min(self.energy + 5, 10)
            print(f"{self.name} is sleeping.")
        else:
            print(f"{self.name} is fully rested.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} is playing.")
        else:
            print(f"{self.name} is not in the mood to play.")

    def get_status(self):
       """Display pet status with emojis and a mood indicator"""
       print(f"\n===== {self.name}'s Status ({self.pet_type.capitalize()}) =====")
       print(f"Hunger: {'🟥' * self.hunger}{'⬜' * (10-self.hunger)} ({self.hunger}/10)")
       print(f"Energy: {'🟩' * self.energy}{'⬜' * (10-self.energy)} ({self.energy}/10)")
       print(f"Happiness: {'🟨' * self.happiness}{'⬜' * (10-self.happiness)} ({self.happiness}/10)")
       print(f"Current mood: {self.mood}")
       print(f"=======================================\n")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}.")
    
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}.")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
