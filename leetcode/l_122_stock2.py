def stockprice(prices):
    maxprofit=0
    total=prices[0]
    maxvalue=0
    for i in range(1,len(prices)):
        total = min(total,prices[i])
        maxprofit = prices[i]-total
        
        maxvalue=max(maxvalue,maxprofit)
    print(maxvalue) 
      
prices=[1,2,3,4,5]
stockprice(prices)
