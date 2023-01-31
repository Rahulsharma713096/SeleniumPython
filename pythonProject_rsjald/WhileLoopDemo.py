
it = 4
while it > 1:
    print(it)
    it = it-1
print("END of While")


print("***********************************")

ab=10
while ab > 1:
    if ab == 9:
        ab = ab-1
        print("Skipped")
        continue
    if ab == 5:
        print("5 is Skipped")
        ab = ab-1
        continue
    if ab == 3:
        break
    print(ab)
    ab = ab-1





