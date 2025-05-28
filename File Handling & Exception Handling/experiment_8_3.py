#Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ): 
#a. Display details of all cities 
#b. Display city names with population more than 10Lakhs 
#c. Display sum of areas of all cities 
def analyze_cities(file_name):
    with open(file_name, 'r') as file:
        cities = []
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                cities.append((parts[0], float(parts[1]), float(parts[2])))    
    print("\nAll City Details:")
    for city, population, area in cities:
        print(f"{city}: {population} Lakhs, {area} sq KM")
    large_cities = [city for city, pop, _ in cities if pop > 10]
    print("\nLarge Cities (>10 Lakhs):")
    print(", ".join(large_cities))
    total_area = sum(area for _, _, area in cities)
    print(f"\nTotal Area: {total_area} sq KM")
analyze_cities('city.txt')
