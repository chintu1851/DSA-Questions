def finaldiscount(prices):
        stack=[]

        for i in range(len(prices)):
            
            print("this is stack",stack)
            print("prices",prices)
            while stack and prices[stack[-1]]>=prices[i]:
                print("-------inside--------")
                prices[stack.pop()]-=prices[i]
            
            stack.append(i)

        print(prices)
prices = [8,4,6,2,3]
finaldiscount(prices)