from collections import deque

snake_queue = deque()
snake_queue.append("小明")
snake_queue.append("小華")
snake_queue.append("小強")
print(f"初始隊列:{snake_queue}")
first_student = snake_queue.popleft()
print(f"{first_student}以機購買並離開隊列。")
print(f"現在的隊列{snake_queue}")
snake_queue.append("小美")
print(f"小美加入隊列")
print(f"最終隊列:{snake_queue}")
