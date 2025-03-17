def happy(n):
        c= set()
        while  n not in c:
            c.add(n)
            s = 0
            for v in str(n):
                s += int(v)**2 

            n = s
            if n ==1:
                return True

        return False