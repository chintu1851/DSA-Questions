def capture(forts):
    # Initialize the variable 'ans' to store the maximum distance
    ans = 0
    
    # 'prev' will store the index of the last non-zero fort (either 1 or -1)
    prev = -1
    
    # Iterate through the 'forts' list with its index and value
    for i, fort in enumerate(forts):
        # If the current fort is not 0 (i.e., it's either 1 or -1), proceed
        if fort != 0:
            # Check if 'prev' is not -1 (meaning we've already seen a non-zero fort before)
            # and check if the current fort and the last seen fort are different
            if prev != -1 and forts[prev] != fort:
                # If so, calculate the distance between the current fort and the last seen fort
                # i - prev - 1 gives the number of zeros between the two forts
                ans = max(ans, i - prev - 1)  # Update 'ans' with the maximum distance found so far
            
            # Update 'prev' to the current index (this fort will be considered the "last seen" fort)
            prev = i
    
    # After looping through all the forts, print the result: the maximum distance between two different forts
    print(ans)

# Test the function with a sample input
forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]
capture(forts)  # The output will be the maximum distance between different forts
