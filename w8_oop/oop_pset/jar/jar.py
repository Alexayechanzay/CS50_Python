class Jar:
    
    def __init__(self, capacity=12):
        self.num_cookies = 0
        self.capacity = capacity

    def __str__(self):
        return f"{self.num_cookies * "🍪" if self.num_cookies > 0 else ""}"

    def deposit(self, n):
        if n > self.capacity - self.num_cookies:
            raise ValueError("Exceed capacity")
        
        self.num_cookies = self.num_cookies + n

    def withdraw(self, n):
        if n > self.num_cookies:
            raise ValueError("Withdraw amuont exceeds number of cookies")

        self.num_cookies = self.num_cookies - n

    @property
    def capacity(self):
        return self._capacity 

    # setter for capacity
    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Capacity should be non-negative integer")
        self._capacity = n

    @property
    def size(self):
        return self.num_cookies

def main():
    j = Jar()
    j.deposit(10)
    print(j)
    
if __name__ == "__main__":
    main()