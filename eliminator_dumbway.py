class Solution(object):
    def lastRemaining(self, n):
        valuebin = []
        for x in range(1, n + 1):
            valuebin.append(x)

        def eliminator(array):
            if len(array) == 1:
                return array[0]
            array = array[1::2]
            return eliminator(array[::-1])

        answer = eliminator(valuebin)
        return answer

        # print(array)
        # print(lastRemaining())
        """
        :type n: int
        :rtype: int
        """
