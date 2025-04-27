def loop_regular_start():
    total_sum=0
    for current_number in range(10, 91):
        if current_number % 2 == 0:
            print(current_number)
            total_sum += current_number
    print(f"Final sum is {total_sum}")





loop_regular_start()