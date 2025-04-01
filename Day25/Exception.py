try:
    a = int(input("entee a number -> "))
    print(a**2)

except Exception as e:
    print(e)

finally:
    print("thanks for visit")