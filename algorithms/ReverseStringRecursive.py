def reverse(str_arr):
    if len(str_arr) == 0:
        return ""

    return str_arr[-1] + reverse(str_arr[0:-1])


print(reverse("test"))
print(reverse("string"))
print(reverse("abcd"))
print(reverse("reverse"))

