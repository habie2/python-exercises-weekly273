import random 

class Dice:
    def __init__(self, name: str, num_throws: int):
        self.name = name
        self.rolls = []

        for _ in range(num_throws):
            self.rolls.append(random.randint(1, 6))
    
    def __str__(self):
        return self.name + str(self.rolls)

    def __eq__(self, another):
        counter1 = 0
        counter2 = 0
        for i in range(len(self.rolls)):
            if self.rolls.count(self.rolls[i]) > counter1:
                counter1 =  self.rolls.count(self.rolls[i])
        for i in range(len(another.rolls)):
            if another.rolls.count(another.rolls[i]) > counter2:
                counter2 =  another.rolls.count(another.rolls[i])

        if counter1 > counter2:
            winner = self.name
        elif counter1 < counter2:
            winner = another.name
        else:
            suma1, suma2 = 0, 0
            for i in range(len(self.rolls)):
                suma1 += self.rolls[i]
            for i in range(len(another.rolls)):
                suma2 += another.rolls[i]
            
            if suma1 > suma2:
                winner = self.name
            elif suma1 < suma2:
                winner = another.name
            else:
                winner =  'They are tied'

        return (f'{self.name}: {counter1}\n{another.name}: {counter2}\nWinner: {winner}')