def loop_regular_start():
    sample_dict = {"lemon":2.99, "tomatoes": 5.50, "potatoes": 10.99, "apples":7.24}

    total_price = 0
    fruit_bought=[]
    for fruit, price in sample_dict.items():
        total_price += price
        fruit_bought.append(fruit)
    print(f"Total price of fruits: {total_price}" )
    print(f"fruit bought: {sample_dict.keys()}")




loop_regular_start()