from collections import defaultdict


# 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。

# 实现 FreqStack 类:

# FreqStack() 构造一个空的堆栈。
# void push(int val) 将一个整数 val 压入栈顶。
# int pop() 删除并返回堆栈中出现频率最高的元素。
# 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。


class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.freq_group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # 需要实现记录每一个 value 的频率
        # 需要计算最大频率是哪一个值
        # 对频率进行分组
        self.cnt[val] += 1
        self.freq_group[self.cnt[val]].append(val)
        # self.freq_GROUP
        self.max_freq = max(self.max_freq, self.cnt[val])

    def pop(self) -> int:
        # 得到result, 并pop
        #result = self.freq_group.get(self.max_freq)[-1]
        result = self.freq_group.get(self.max_freq).pop()
        # cnt 即数值的频率需要减小
        self.cnt[result] -= 1
        # 判断是否为empty , 如果是的话，就max - 1
        if len(self.freq_group.get(self.max_freq)) == 0:
            self.max_freq -= 1
        return result

# ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
# [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]
test = FreqStack()
test.push(4)
test.push(0)
test.push(9)
test.push(3)
test.push(4)
test.push(2)
print(test.pop())
test.push(6)
print(test.pop())
test.push(1)
print(test.pop())
test.push(1)
print(test.pop())
test.push(4)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())






