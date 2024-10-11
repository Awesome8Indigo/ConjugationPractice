import shoresh
shleach = shoresh.shoresh(["ש","ל","ח"], "to send")
f = shleach.search()
print(f)

z = shoresh.shoresh(["ז,""ד","ג"], "to send")
z.addShoresh()
print(z.search())