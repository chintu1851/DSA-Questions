def colorblock(blocks, k):
    min_white_count = float('inf')

    for i in range(len(blocks) - k + 1):
        window = blocks[i:i + k]
        white_count = window.count('W')  # Directly count the number of 'W's in the window
        
        print(f"Window: {window} -> W count: {white_count}")
        min_white_count = min(min_white_count, white_count)
    
    return min_white_count

blocks = "WBWBBBW"
k = 2

print(colorblock(blocks, k))
