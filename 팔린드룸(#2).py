# "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 팔린드롬(palindrome)이라고 부릅니다.
# 문자열 word가 팔린드롬인지 확인하는 함수 is_palindrome를 쓰세요. is_palindrome은 word가 팔린드롬이면 True를,
# 팔린드롬이 아니면 False를 리턴합니다.
# palindrome : 회문문
# https://dojang.io/mod/page/view.php?id=2331

def is_palindrome(word):
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        print(word[left], word[right])

        if word[left] != word[right]:
            return False    # return 틍성상 값이 True면 종료되므로 일부러 False를 주어 회문을 만드는 것이 좋다.


    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
