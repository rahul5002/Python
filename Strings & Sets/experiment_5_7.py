#Create 2 sets s1 and s2 of n fruits each by taking input from user and find: 
#a) Fruits which are in both sets s1 and s2 
#b) Fruits only in s1 but not in s2 
#c) Count of all fruits from s1 and s2 
def main():  
    n = int(input("Enter the number of fruits in each set: "))  

    s1 = set()  
    print(f"Enter {n} fruits for set s1:")  
    for _ in range(n):  
        fruit = input("Enter fruit: ").strip() 
        s1.add(fruit)  

    s2 = set()  
    print(f"Enter {n} fruits for set s2:")  
    for _ in range(n):  
        fruit = input("Enter fruit: ").strip()  
        s2.add(fruit)  

    common_fruits = s1.intersection(s2)  
    print("Fruits which are in both sets:", common_fruits)  

    unique_to_s1 = s1.difference(s2)  
    print("Fruits only in s1:", unique_to_s1)  

    all_unique_fruits = s1.union(s2)  
    print("Count of all unique fruits from s1 and s2:", len(all_unique_fruits))  

if __name__ == "__main__":  
    main()