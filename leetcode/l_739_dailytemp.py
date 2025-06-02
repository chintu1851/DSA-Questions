def dailytemp(temperatures):
        stack = []
        answer = [0] * len(temperatures) 
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer
    
temperatures = [73,74,75,71,69,72,76,73]
print(dailytemp(temperatures))