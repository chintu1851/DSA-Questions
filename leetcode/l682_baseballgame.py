def baseballgame(ops):
    newsops = []
    for i in range(len(ops)):
        if ops[i] == "C":
            newsops.pop()  # Remove the last element
        elif ops[i] == "D":
            newsops.append(int(newsops[-1]) * 2)  # Double the last element
        elif ops[i] == "+":
            newsops.append(newsops[-1] + newsops[-2])  # Sum of the last two elements
        else:
            newsops.append(int(ops[i]))  # Convert the string to integer and add to the list
    return sum(newsops)

# Test case
ops = ["5", "2", "C", "D", "+"]
baseballgame(ops)  # Output will show the final sequence of operations
