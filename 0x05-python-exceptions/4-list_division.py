#!/usr/bin/python3


def list_division(my_lis_1, my_list_2, list_length):
    newList = []
    ans = 0
    for a in range(0, list_length):
        try:
            ans = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("Wrong type")
            ans = 0
            continue
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
            continue
        except IndexError:
            ans = 0
            print("out of range")
            continue
        finally:
            newList.append(ans)
            return (newList)
