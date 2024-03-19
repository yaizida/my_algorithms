from collections import deque


data = deque(maxlen=10)

for item in range(15):
    data.appendleft(item)

print(data)
