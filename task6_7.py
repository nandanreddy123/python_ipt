days_input = int(input('enter number of days'))
years = 0
if days_input > 364:
    while days_input >= 0 and days_input >= 365:
        years += 1
        days_input -= 365
print(years,'the years completed in days input')