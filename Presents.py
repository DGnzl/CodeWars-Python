def presents(a):
    ans = []
    for x in range(len(a)):
        print(x)
        ans.append(a.index(x + 1) + 1)
    return ans

# return [a.index(i)+1 for i in range(1,len(a)+1)]

# import unittest

# @test.describe("Sample tests")
# def sample_tests():
#     @test.it("Tests")
#     def it_1():
#         test.assert_equals(presents([2, 3, 4, 1]), [4, 1, 2, 3])
#         test.assert_equals(presents([1, 3, 2]), [1, 3, 2])
#         test.assert_equals(presents([1, 2]), [1, 2])