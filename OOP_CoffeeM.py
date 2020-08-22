class CoffeeMachine:
    REMAINING = True
    BUY = False
    FILL = False
    MODIFIED_INGREDIENTS = 0
    
    machine_state = [['water', 400], ['milk', 540], ['coffee beans', 120], ['disposable cups', 9], ['money', 550]]
    recipes = [(250, 0, 16, 1, 4), (350, 75, 20, 1, 7), (200, 100, 12, 1, 6)] # espresso, latte, cappuccino    
    
    def __init__(self):
        self.print_menu_remaining()
    
    def controller(self, user_input):
        if 'exit' == user_input:
            exit()
        elif CoffeeMachine.REMAINING:
            if user_input == 'remaining': # CoffeeMachine state does not change
                self.display_state()
                self.print_menu_remaining()
            elif user_input == 'buy':    # CoffeeMachine state changes
                CoffeeMachine.REMAINING = False 
                CoffeeMachine.BUY = True
                self.print_menu_buy()
            elif user_input == 'fill':  # CoffeeMachine state changes
                CoffeeMachine.REMAINING = False 
                CoffeeMachine.FILL = True
                print()
                self.print_menu_fill()
            elif user_input == 'take':   # CoffeeMachine state does not change
                self.take_action()
                self.print_menu_remaining()
            else:
                self.print_menu_remaining()
                
        elif CoffeeMachine.BUY:
            self.buy_action(user_input)
            CoffeeMachine.BUY = False
            CoffeeMachine.REMAINING = True
            self.print_menu_remaining()
        
        elif CoffeeMachine.FILL:
            self.fill_action(user_input)
            if CoffeeMachine.MODIFIED_INGREDIENTS > 3:
                CoffeeMachine.FILL = False
                CoffeeMachine.REMAINING = True   
                CoffeeMachine.MODIFIED_INGREDIENTS = 0
                print()
                self.print_menu_remaining()
            else:
                pass
            
    # menu printing menu - telling users what options they have
    
    def print_menu_remaining(self):
        print('Write action (buy, fill, take, remaining, exit):')
        
    def print_menu_buy(self):
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        
    def print_menu_fill(self):
        
        if CoffeeMachine.MODIFIED_INGREDIENTS == 0:
            print('Write how many ml of water do you want to add:')
        elif CoffeeMachine.MODIFIED_INGREDIENTS == 1:
            print('Write how many ml of milk do you want to add:')
        elif CoffeeMachine.MODIFIED_INGREDIENTS == 2:
            print('Write how many grams of coffee beans do you want to add:')
        elif CoffeeMachine.MODIFIED_INGREDIENTS == 3:
            print('Write how many disposable cups of coffee do you want to add:')
        else:
            pass    
    
    # methods dealing with user's action
    
    def display_state(self):
        print("\nThe coffee machine has:")
        for item in CoffeeMachine.machine_state:
            if item[0] == 'money': 
                print('$' + str(item[1]), 'of', item[0])
            else:
                print(item[1], 'of', item[0])  
        print()
    
    def buy_action(self, user_input):
        if user_input not in ['1', '2', '3']:
            pass
        else:
            user_input = int(user_input)
            user_input -= 1 # lists indexes are zero-based
            # checking if there are enough ingredients for selected drink
            # Each of the following should hold
            water_status = CoffeeMachine.recipes[user_input][0] <= CoffeeMachine.machine_state[0][1]
            milk_status = CoffeeMachine.recipes[user_input][1] <= CoffeeMachine.machine_state[1][1]
            beans_status = CoffeeMachine.recipes[user_input][2] <= CoffeeMachine.machine_state[2][1]
            cups_status = CoffeeMachine.recipes[user_input][3] <= CoffeeMachine.machine_state[3][1]
            if water_status and milk_status and beans_status and cups_status:
                # confirming that selection is available
                print("I have enough resources, making you a coffee!\n")
                CoffeeMachine.machine_state[0][1] -= CoffeeMachine.recipes[user_input][0]
                CoffeeMachine.machine_state[1][1] -= CoffeeMachine.recipes[user_input][1]
                CoffeeMachine.machine_state[2][1] -= CoffeeMachine.recipes[user_input][2]
                CoffeeMachine.machine_state[3][1] -= CoffeeMachine.recipes[user_input][3]
                CoffeeMachine.machine_state[4][1] += CoffeeMachine.recipes[user_input][4]
            elif not water_status:
                print("Sorry, not enough " + CoffeeMachine.machine_state[0][0] + "!\n")
            elif not milk_status:
                print("Sorry, not enough " + CoffeeMachine.machine_state[1][0] + "!\n")
            elif not beans_status:
                print("Sorry, not enough " + CoffeeMachine.machine_state[2][0] + "!\n")
            else:
                print("Sorry, not enough " + CoffeeMachine.machine_state[2][0] + "!\n")              
    
    def fill_action(self, user_input):
        user_input = int(user_input)
        if CoffeeMachine.MODIFIED_INGREDIENTS == 0:
            CoffeeMachine.machine_state[0][1] += user_input
            self.print_menu_fill()
        elif CoffeeMachine.MODIFIED_INGREDIENTS == 1:
            CoffeeMachine.machine_state[1][1] += user_input
            self.print_menu_fill()
        elif CoffeeMachine.MODIFIED_INGREDIENTS == 2:
            CoffeeMachine.machine_state[2][1] += user_input
            self.print_menu_fill()
        elif CoffeeMachine.MODIFIED_INGREDIENTS == 3:
            CoffeeMachine.machine_state[3][1] += user_input            
        else:
            pass
        CoffeeMachine.MODIFIED_INGREDIENTS += 1            
    
    def take_action(self):
        money = CoffeeMachine.machine_state[4][1]
        print('I gave you $' + str(money))
        print('\n')
        CoffeeMachine.machine_state[4][1] = 0
        # return money      

demo_machine = CoffeeMachine()

while(True):
    demo_machine.controller(input().strip())
