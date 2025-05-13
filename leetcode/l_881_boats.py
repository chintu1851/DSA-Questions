def boats(people,limit):
        count = 0
        sortpeople = sorted(people)
        i = 0
        j = len(sortpeople) - 1

        while i <= j:
            print(sortpeople[i], sortpeople[j])

            # If the lightest and heaviest person can be paired
            if sortpeople[i] + sortpeople[j] <= limit:
                count += 1
                i += 1
                j -= 1
            # If the heaviest person must go alone
            else:
                count += 1
                j -= 1

        print(count)
        
people = [1,3,2,3,2]
limit = 3
boats(people,limit)
