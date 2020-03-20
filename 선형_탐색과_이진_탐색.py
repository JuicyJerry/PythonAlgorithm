# 탐색: 저장된 정보들 중에서 원하는 값을 찾는 것
# 선형 탐색 알고리즘(liner search algorithm): 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘
# 이진 탐색 알고리즘(binary search algorithm): 반 씩 제외시키면서 찾는 알고리즘
def linear_search(element, some_list):
    count = 0
    while count <= len(some_list):
        if element == some_list[count]:
            print(element, some_list[count])
            count += 1
        elif element != some_list[count]:
            print("noun")

            break



print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
