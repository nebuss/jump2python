a = [1, 2, 3, 4]
result= []
for num in a:
    result.append(num*3)
print(result)


a = [1, 2, 3, 4]
result = [num*3 for num in a if num % 2 ==0]
print(result)


result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)

result = 0
i = 1
while i < 1000:
    if i % 3 == 0:
        result += i
    i +=1
print(result)

# 별 표시하기
i = 0
while True:
    i+=1
    if i > 5: break
    print('*' * i)

# for문 사용해서 1부터 100까지 숫자를 출력해 보자
for i in range(101):
    print(i)


A = [70, 60, 55, 75, 95, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / 10
print(average)

# 리스트 컴프리헨션



