
def deckcardds(deck):
        count = Counter(deck)
    
    # Find the GCD of all the frequencies
        g = 0
        for val in count.values():
            g = math.gcd(g, val)
    
    # If GCD is greater than 1, we can partition the deck
        return g > 1

deck = [1,1,1,2,2,2,3,3]
deckcardds(deck)
