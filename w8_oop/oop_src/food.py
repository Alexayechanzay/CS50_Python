class Food:

    base_hearts = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calcualte_hearts(ingredients)

    @classmethod
    def calcualte_hearts(cls, ingredients):
        hearts = cls.base_hearts  # accessing class variable
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])
        food.hearts = hearts
        return food # obj is returned


def main():
    supply = Food(ingredients=["Mushroom", "Hearty Cake"])
    print(f"New live is {supply.hearts} hearts!")


    skwer = Food.from_nothing(2)
    print(f"New live is {skwer.hearts} hearts!")

main()