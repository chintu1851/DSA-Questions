def town_judge(n, trust):
    trust_score = [0] * (n + 1)
    print(trust_score)
    for pair in trust:
        a = pair[0]
        b = pair[1]
        
        trust_score[a] -= 1
        trust_score[b] += 1
    print(trust_score)    
    for i in range(1, n + 1):
        if trust_score[i] == n - 1:
            print(i)
            return
    print(-1)

n = 3
trust = [[1,3],[2,3]]
town_judge(n,trust)
