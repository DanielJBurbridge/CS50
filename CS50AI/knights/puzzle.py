from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")



def createBasicRules(players, knowledge):


    for player in players:
        knowledge.add(Or(player[0], player[1]))
        knowledge.add(Not(And(player[0], player[1])))

    return knowledge
        


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And()
#Creating Basic Rules of the game for all players
knowledge0 = createBasicRules([[AKnight, AKnave]], knowledge0)

#Testing A's Statement
knowledge0.add(Implication(AKnight, And(AKnight, AKnave)))

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And()

#Creating Basic Rules of the game for all players
knowledge1 = createBasicRules([[AKnight, AKnave], [BKnight, BKnave]], knowledge1)

# Testing A's Statement
knowledge1.add(Implication(AKnight, And(AKnave, BKnave))),
knowledge1.add(Implication(AKnave, Not(And(AKnave, BKnave))))

# Testing B's Statement
# No statement to test.

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And()

#Creating Basic Rules of the game for all players
knowledge2 = createBasicRules([[AKnight, AKnave], [BKnight, BKnave]], knowledge2)

# Testing A's Statement
knowledge2.add(Implication(AKnight, And(AKnave, BKnave)))
knowledge2.add(Implication(AKnight, And(AKnight, BKnight)))

# Testing B's Statement
knowledge2.add(Implication(BKnight, And(AKnight, BKnave)))
knowledge2.add(Implication(BKnight, And(AKnave, BKnight)))


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And()

# Creating Basic Rules of the game for all players
knowledge3 = createBasicRules([[AKnight, AKnave], [BKnight, BKnave], [CKnight, CKnave]], knowledge3)

# Testing A's statement
# N/A

# Testing B's statements
# A said 'I am a knave.'
knowledge3.add(
    Implication(BKnight, And(
      Implication(AKnight, AKnave),
      Implication(AKnave, Not(AKnave)),
    )))
knowledge3.add(Implication(BKnave, And(
      Implication(AKnight, AKnight),
      Implication(AKnave, Not(AKnight))
    )))

# "C is a K
# nave"
knowledge3.add(Implication(BKnight, CKnave))
knowledge3.add(Implication(BKnave, Not(CKnave)))
knowledge3.add(Implication(CKnave, BKnight))
knowledge3.add(Implication(CKnight, BKnave))

# Testing C's statement
knowledge3.add(Implication(CKnight, AKnight))
knowledge3.add(Implication(CKnave, Not(AKnight)))

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
