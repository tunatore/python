try:
    1 / 0
except ZeroDivisionError:
    print("Division error")
except:
    print("All other exceptions")
else:
    print("No exception")
finally:
    print("Finally")
