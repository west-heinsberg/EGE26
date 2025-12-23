with open(r'../../files/24_1975.txt') as file:
    data = file.readline()

# test = '***P**PP****PP****P***P' #счет символов
test = '***P**PP****P****PP**'
ans = []
#ans = 0
cnt = 1 #у нас 4 символа
for i in range(len(test) - 1):
    if test[i] + test[i+1] != 'PP':
        cnt +=1
    else:
        ans.append(cnt) #ans = max(ans,cnt)
        cnt = 1
#ans = max(ans,cnt)
ans.append(cnt) # else в последний раз не сработает
print(max(ans))  # тк просят самую длинную
    # 0 1
    # 1 2
    #2 3
    # 3 4 - чтобы не рассм. несущ. пару делаем +1, пара будет у первых трёх элементов

    # 0 1
    # 1 2
    # 2 3

###########################
# решение

with open(r'.\files\24_1975.txt') as file:
    data = file.readline()

ans = 0
cnt = 1
for i in range(len(data) - 1):
    if data[i] + data[i + 1] != 'pp':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)

print(ans)