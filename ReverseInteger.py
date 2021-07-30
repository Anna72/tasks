class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)
        
        if ( x >= 0):
            s = s[::-1]
        else:
            s = '-' + s[:0:-1]
        
        maxx = pow(2,31) - 1
        minx = -maxx -1  
        
        maxs = str(maxx)
        mins = str(minx)
        
        #print(s)
        #print(maxs)
        #print(mins)
        
        if ( x >= 0):
            if(len(s) > len(maxs)):
                return(0)
            else:
                if(len(s) == len(maxs) and s > maxs):
                    return(0)
        else: 
            if(len(s) > len(mins)):
                return(0)
            else:
                if(len(s) == len(mins) and s > mins):
                    return(0)
            
        return(int(s))    
