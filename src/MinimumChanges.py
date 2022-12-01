class MinimumChanges:

    def minOperations(self, s: str) -> int:
        # 首先判断奇偶
        # length = len(s)
        startWithOne = 0
        for index in range(len(s)):
            # s[index]
            # 奇数 = 0 需要 ++
            # 偶数 = 1 需要 ++
            if index % 2 == 1:
                if s[index] == '0':
                    startWithOne = startWithOne + 1
            else:
                if s[index] == '1':
                    startWithOne = startWithOne + 1
        startWithZero = len(s) - startWithOne
        return startWithOne if startWithZero > startWithOne else startWithZero


m = MinimumChanges()
s = '1010111110101'
print(m.minOperations(s))
