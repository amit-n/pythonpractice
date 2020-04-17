da = (input("Share your birthday in YYYYMMDD Format"))
def myday(data):
    x=0
    if len(data) ==1:
        return int(data)
    for i in data:
        x+=int(i)
    return myday(str(x))

print(myday(da))
