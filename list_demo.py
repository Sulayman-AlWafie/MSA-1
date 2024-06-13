def main():
    #list de3mo
    #create a list of string names
    names = ["John", "Mary", "Alice","bob"]
    list_of_integers = [10, 16,24,42,14,9]
    random_typr_list = ["cyde", 15, 22.3, "Frank"]

    print(names)
    print(list_of_integers)

    #add values to a list
    names.append("jonnie")
    list_of_integers.append(5)
    list_of_integers.append(63)

    print(names)
    print(list_of_integers)
    
   #get the number of item in a list
    number_of_items = len(list_of_integers)
    print ("//n")
    print(f" number of items in integer list:{number_of_items}")

    #get values from our list
    #get the first value from the list_of_integers
    print(f"\nfirst item in integer list:{list_of_integers[0]}")

      #get the fourth value from the list_of_integers
    print(f"\nfourth item in integer list:{list_of_integers[3]}")

    #print all itmes in the list_of_integers
    print("\nInteger list itmes")
    for item in list_of_integers:
        print(item)
    print("\n")

    for index in range(len(list_of_integers)):
       print(f"Index{item+1}: {list_of_integers[index]}")


main()
