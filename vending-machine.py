def vending_machine(ada_vending_machine, customer_input):

    # Display message
    print("Welcome to Ada's Vending Machine!")

    # Display contents of vending machine
    print(ada_vending_machine)

    # Validate user_input
    item_selected = False
    sufficient_funds = False

    for item in ada_vending_machine:

        #Check for valid item number
        if customer_input[0] == item.get('item_number'):

            item_selected = True

            # Check sufficient funds are deposited
            if customer_input[1] >= item.get('price'):

                sufficient_funds = True

                # Deduct cost of item from deposited amount
                remaining_funds = customer_input[1] - item.get('price')

                # Disburse change to customer
                print(f'Change disbursed: {remaining_funds}')

                item['quantity'] = item.get('quantity') - 1

    if item_selected == False:

        print("Please update input to select an item number in the vending machine")

    elif sufficient_funds == False:

        print("Please update input with amount of sufficient funds for the selected item number in the vending machine")

    else:

        print(ada_vending_machine)



ada_vending_machine = [{'name': 'Ada Chips', 'item_number': 'A1', 'price': 0.50, 'quantity': 5},
                        {'name': 'Ada Candy Bar', 'item_number': 'A2', 'price': 0.75, 'quantity': 5},
                        {'name': 'Ada Gum', 'item_number': 'A3', 'price': 0.25, 'quantity': 5},
                        {'name': 'Ada Cookies', 'item_number': 'A4', 'price': 1.50, 'quantity': 5}]

customer_input = ['A1', 1.00]

vending_machine(ada_vending_machine,customer_input)