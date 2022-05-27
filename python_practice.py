print("hello world!")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
    temperature = int(input("what is the temperature outside?"))

    if temperature > 80:
        print("turn on the AC.")
else:
    print("open the windows.")

counties = ["Arapahoe", "Denver", "Jefferson"]

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")

else:
    print("El Paso is not the list of counties.")

for county, voters in counties_dict.items():
    print(county, voters)


