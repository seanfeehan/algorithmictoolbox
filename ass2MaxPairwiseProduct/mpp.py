# Uses python3

class mpp:
    def maxPairwiseProduct(self, len, arr):
        result = 0

        for i in range(0, len):
            for j in range(i + 1, len):
                if arr[i] * arr[j] > result:
                    result = arr[i] * arr[j]
        return result


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)

    print(mpp().maxPairwiseProduct(n, a))


if __name__ == '__main__':
    main()
