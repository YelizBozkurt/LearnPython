page = 5
total = 0
day, month ,year=1,1,2024

def calculate_next_day(day,month,year):
    day+=1
    if month in[1,3,5,7,8,10,12] and day >31:
        day=1
        month+=1
    elif month in [4,6,9,11] and day >30:
        day=1
        month+=1
    elif month==2:


for i in range(365):
    total+=5

print("Total number of pages: ", total)
print("Average number of books: ", total/150)

