def repeateddna(s):
        
        # set for sequence
        sequence = set()
        
        # set for sequence with repetition
        repeated = set()
        
        for i in range( len(s)-9 ):
            
            # make current sequence for i to i+10
            cur_seq = s[i:i+10]
            
            if cur_seq in sequence:
                # check for repetition
                repeated.add( cur_seq )
            
            # add to sequence set
            sequence.add( cur_seq )
            print(sequence)
        
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
repeateddna(s)
