class Solution(object):
    def addBinary(self, a, b):
        def todec(a):
            sum = 0
            for i in reversed(range(len(a))):
                if a[i] == '1':
                    sum += pow(2, len(a) - i - 1)
            return sum
        
        #print sumdec
        def tobin(x):
            rem = ''
            while(x >=2):
                rem = str(x % 2) + rem
                x = x // 2
            rem = str(x) + rem
            return rem
        sumdec = todec(a) + todec(b)
        outputs = tobin(sumdec)
gh
        return outputs
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        