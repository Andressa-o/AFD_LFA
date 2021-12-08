
condition = input().split(" ")
simbalf = input().split(" ")
qtrans = int(input())

afd = {}

for state in condition:
    afd[state] = {}

for i in range(0, qtrans):
    i, c, f = input().split(" ")
    if c not in afd[i]:
      afd[i][c] = f

inicial_state = input()
final_state = input().split(" ")
words = input().split(" ")

for word in words:
    actual_state = inicial_state
    error_state = 0
    for char in word:
        try:
            actual_state = afd[actual_state][char]
        except KeyError:
            error_state = 1
            break
    if(error_state == 1 or actual_state not in final_state):
        print('N')
    else:
        print('S')