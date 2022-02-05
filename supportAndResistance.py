
high = int(input("Enter High: "))
low = int(input("Enter Low: " ))
close = int(input("Enter close: "))

pivotPoint = int(((high) + (low) + (close)) / 3)
r1 = (2 * pivotPoint) - low
s1 = (2 * pivotPoint) - high

r2 = pivotPoint + (high - low)
s2 = pivotPoint - (high - low)

r3 = high + 2 * (pivotPoint - low)
s3 = low - 2 * (high-pivotPoint)


print("Resistance R1: ", r1)
print("Support S1: ", s1)
print()
print("Resistance R2: ",r2)
print("Support S2: ", s2)
print()
print("Resistance R3: ",r3)
print("Support S3: ", s3)