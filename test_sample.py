n = 0
while n < 100:
    n = n + 1
    if n % 2 == 0:
        print('这是偶数:', n)
    else:
        print('这是奇数:', n)


    def test_number():
        assert n == 100
