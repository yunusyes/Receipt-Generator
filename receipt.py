class Shopping_cart: 

    def receipt(self):
        self.shopping_cart = []
        self.amount = 0
        self.item = ""
        
        while self.item != "q":
            self.item = input("Enter a food to buy (q to quit): ")
            if self.item == "q":
                print("----- YOUR CART -----")
                for i in self.shopping_cart:
                    print(i)
                print(f"Your total is: ${self.amount}")
                break  
            else:
                self.shopping_cart.append(self.item) 
                self.price = int(input(f"Enter the price of a {self.item}: $"))
                self.amount += self.price
                 
def main():
    sc = Shopping_cart()
    sc.receipt()
    
if __name__ == "__main__":
    main()