def main():
    

    #creat a wile loop that prints integers between 0-10
    output_value = 0
    stop_value = 10
    #run the loop while output value is less than or equal to stop value
    while output_value <= stop_value:
        print(output_value)
        # increment output value
        output_value += 1
        #output_value = output_value + 1
    print("\n\n")
    while True:
        print(output_value)
        output_value += 1

        #if output_value is greater than stop value. Break the loop

        if output_value > stop_value:
            break
main()
