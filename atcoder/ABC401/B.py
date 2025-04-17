n = int(input())
status = "logout"
answer = 0
for i in range(n):
    new_status = input()
    if new_status == "private" and status == "logout":
        answer += 1
    if new_status == "logout" or new_status == "login":
        status = new_status

print(answer)