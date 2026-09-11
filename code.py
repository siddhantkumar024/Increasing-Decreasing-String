# p or pattern make it soln will be easy p=ascii_lowercase + ascii_lowercase[::-1]
#  p= 'abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba '


class Solution:
    def sortString(self, s: str) -> str:
        d={}
        for nu in s:
            if nu not in d:
                d[nu]=1
            else:
                d[nu]+=1
        p=ascii_lowercase + ascii_lowercase[::-1]
        print(p,d)
        r=[]
        while len(r)<len(s):
            for ch in p:
                print(ch)
                if ch in d and d[ch]>0:
                    r.append(ch)
                    d[ch]-=1
        return ''.join(r)
        
