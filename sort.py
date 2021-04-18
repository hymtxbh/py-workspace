class Sort(object):
    @classmethod
    def q_sort(cls, array, left, right):
        if left > right:
            return
        stack = [left, right]
        while stack:
            left = stack.pop(0)
            right = stack.pop(0)
            if left > right:
                continue
            _x = left - 1
            tmp = array[right]
            for j in range(left, right):
                if array[j] <= tmp:
                    _x += 1
                    array[_x], array[j] = array[j], array[_x]
            array[_x + 1], array[right] = array[right], array[_x + 1]
            stack.extend([left, _x, _x +2, right])


if __name__ == '__main__':
    s = [1, 2, 34, 5, 78, 4, 8, 8, 1, 0, 5, 2, 4]
    Sort.q_sort(s, 0, len(s) - 1)
    print(s)
