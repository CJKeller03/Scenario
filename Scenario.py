import random

adjectives = ["blue", "red", "good", "bad", "stupid"]
adverbs = ["stupidly", "lazily", "slowly"]
commonNouns = ["cat", "dog", "table", "chair", "flower"]
properNouns = ["Kehoe Center", "White House", "Kennedy Space Center", "Mansfield High School"]
pastVerbs = ["ate", "broke", "slept", "drank", "kicked", "hid"]
gerundVerbs = ["eating", "braking", "sleeping", "drinking", "kicking", "hiding"]
prepositions = ["on", "of", "in", "with"]

rules = {

    "START": ["NounPhrase", "PrepPhrase", "Subject"],
    "NounPhrase": ["PrepPhrase", "VerbPhrase", "END"],
    "PrepPhrase": ["PrepPhrase", "END"],
    "VerbPhrase": ["PrepPhrase", "END"],
    "Subject": ["VerbPhrase", "PrepPhrase", "END"]


}

class Sentence:

    def __init__(self, subject):
        self.structure = ["START"]
        self.text = ""
        self.subject = subject

    def genSentence(self):
        while True:
            next = random.choice(rules[self.structure[-1]])

            if next == "END" and len(self.structure) > 3:
                return
            elif next == "END":
                continue

            self.structure.append(next)

            if next == "NounPhrase":
                self.text += self.getNounPhrase()

            elif next == "PrepPhrase":
                self.text += self.getPrepositionalPhrase()

            elif next == "Subject":
                self.text += self.subject

            elif next == "VerbPhrase":
                self.text += self.getVerbPhrase()

            self.text += " "

            



    def getCommonNoun(self):
        return random.choice(commonNouns)

    def getPluralNoun(self):
        return random.choice(commonNouns) + "s"

    def getProperNoun(self):
        return random.choice(properNouns)


    def getPastVerb(self):
        return random.choice(pastVerbs)

    def getGerundVerb(self):
        return random.choice(gerundVerbs)

    def getAdverb(self):
        return random.choice(adverbs)

    def getAdjective(self):
        return random.choice(adjectives)


    def getNounPhrase(self):
        out = []
        if (bool(random.getrandbits(1))):
            out.append("the")
            out.append(self.getProperNoun())

        else:
            out.append("a")
            if (random.randint(0, 3) == 0):
                out.append(self.getAdjective())
            out.append(self.getCommonNoun())


        if (random.randint(0,5) == 0):
            out.append(self.getPrepositionalPhrase())

        return " ".join(out)


    def getPrepositionalPhrase(self):
        out = []
        if self.structure[-2] == "Subject":
            out.append("was")
        
        out.append(random.choice(prepositions))
        out.append(self.getNounPhrase())

        return " ".join(out)

    
    def getVerbPhrase(self):
        out = []
        if (bool(random.getrandbits(1))):
            out.append("was")
            if (random.randint(0,2) == 0):
                out.append(self.getAdverb())

            out.append(self.getGerundVerb())
        else:
            if (random.randint(0,2) == 0):
                out.append(self.getAdverb())
                
            out.append(self.getPastVerb())

        return " ".join(out)

        

x = Sentence("Caleb")
x.genSentence()
print(x.text)

