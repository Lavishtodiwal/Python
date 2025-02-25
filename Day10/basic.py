signal = input("Enter the signal color-> ")
signal = signal.lower().strip()

if signal =="red":
    print("Stop")
elif signal =="green":
    print("Go")
elif signal =="yellow":
    print("Slow down")
else:
    print("please enter correct signal color name :) ")