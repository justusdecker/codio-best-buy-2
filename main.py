from store import Store
from promotions import SecondHalfPrice, BOGO, PercentDiscount
STORE = Store()
MENU = """
Welcome to BestBuy!
-----------------------------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""

def main():
    is_running = True
    
    STORE.products[0].set_promotion(SecondHalfPrice())
    STORE.products[1].set_promotion(BOGO())
    STORE.products[2].set_promotion(PercentDiscount(10))
    while is_running:
        print(MENU)
        user_input = input('Please choose a number: ')
        match user_input:
            case "1": # print a table of products in store
                print(f"{'Name':<30} {'Price':<6} {'Quantity':<15}")
                for prod in STORE.products:
                    print(prod.show())
                input('ENTER to continue!')
            case "2": # get total quantity of all products in store
                print(STORE.get_total_quantity())
                input('ENTER to continue!')
            case "3": # ordering
                print('-'*6)
                print(f"#   {'Name':<30} {'Price':<6} {'Quantity':<15}")
                for index,prod in enumerate(STORE.products):
                    print(f'#{index+1:<2} {prod.show()}')
                print('-'*6)
                print("When you want to finish order, enter empty text.")
                ordering_input = 'NOTEMPTY'
                quantity_input = 'NOTEMPTY'
                shopping_cart = []
                while ordering_input and quantity_input:
                    ordering_input = input("Which product # do you want? ")
                    
                    if not ordering_input: break
                    if not ordering_input.isdecimal(): 
                        print('Something went wrong please try again!')
                        continue
                    
                    quantity_input = input("What amount do you want? ")
                    
                    if not quantity_input: break
                    if not quantity_input.isdecimal(): 
                        print('Something went wrong please try again!')
                        continue
                    

                    if int(ordering_input) - 1 < len(STORE.products):
                        shopping_cart.append((STORE.products[int(ordering_input) - 1],int(quantity_input)))
                        print("Product added to list!")
                    else:
                        print('This Product doesn\'t exist!')
                for product in shopping_cart:
                    product[0].buy(product[1])
                    print(f'Ordered: {product[1]} of {product[0].name}')

            case "4": # exit
                is_running = False

if __name__ == '__main__':
    main()