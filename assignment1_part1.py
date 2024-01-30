def list_divide(numbers, divide=2):
    pass
class ListDivideException:
    def test_list_divide():
        if list_divide([1,2,3,4,5]) != 2:
            return print("2")
        elif list_divide([2,4,6,8,10]) != 5:
            return print("5")
        elif list_divide([30, 54, 63,98, 100], divide=10) != 2:
            return print("2")
        elif list_divide([]) != 0:
            return print("0")
        elif list_divide([1,2,3,4,5], 1) != 5:
            return print("5")