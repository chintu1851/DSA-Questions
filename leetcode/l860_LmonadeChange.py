def lemonade(bills):
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False
            else:
                if ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True
bills=[5,5,10,10,20]
print(lemonade(bills))