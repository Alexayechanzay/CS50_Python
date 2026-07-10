class Package:
    def __init__(self, id, sender, recipient, weight):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return(f"Package number: {self.id}\nSender: {self.sender}\nRecipient: {self.recipient}\nWeight: {self.weight}\n----------------")

    def cost(self, cost_per_kg):
        return cost_per_kg * self.weight

def main():
    packages = [
        Package(1,"Alice", "Bob", 10), 
        Package(2, "Bob", "Charlie", 5)
        ]
    
    for pkg in packages:
        print(pkg)
        print(f"Total cost ${pkg.cost(cost_per_kg=10)}")
        print("---------------")
main()