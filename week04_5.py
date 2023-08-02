import sys
t = int(input())
def fight(atk_j, hp_j, encounter):
    for atk_m, hp_m in encounter:
        while True:
            hp_m -= atk_j
            if hp_m <= 0:
                break
            hp_j -= atk_m
            if hp_j <= 0:
                return False
            
    return True

for _ in range(t):
    n, m, mon = map(int,input().split())
    data = input()
    atk_j, hp_j = map(int,input().split())
    monsters= [(0,0)] * n
    
    for _ in range(mon):
        pos_m, atk_m, hp_m = map(int,input().split())
        monsters[pos_m-1] = (atk_m, hp_m)
    sys.stdin.readline().rstrip()
    junsik = data.index("@")
    exits = [i for i in range(n) if data[i] == "O"]

    flag = "NO"
    for exit in exits:
        l, r = min(junsik, exit), max(junsik, exit)
        wall = data[l:r+1].count("#")
        encounter = [(atk_m, hp_m) for atk_m, hp_m in monsters[l:r] if atk_m != 0]
        if junsik > exit:
            encounter = reversed(encounter)

        if wall <= m and fight(atk_j, hp_j, encounter): 
            flag = "YES"

    print(flag)
