# This is to certify that this project is my own work, based on my personal efforts in studying and applying the concepts learned. I have constructed the functions and their respective algorithms and corresponding code by myself. The program was run, tested, and debugged by my own efforts. I further certify that I have not copied in part or whole or otherwise plagiarized the work of other students and/or persons.
# <MALINAY, Ma. Bernadette C.>, DLSU ID# <12252743>
# <ZOLETA, Margareth Glenn Y.>, DLSU ID# <12256626>

#Description: <Users of the program can place up to three orders, each of which can include one meal, one side dish, and one drink. Additionally, both during and after the ordering process, they can change and cancel their orders. A detailed invoice is displayed at the very conclusion of the program.>
#Programmed by: <MALINAY, Ma. Bernadette C. & ZOLETA, Margareth Glenn Y.> <HUMSS12-C>
#Last modified: <December 12, 2023>
#Version: <Python 3.0>
#Acknowledgements: <Empowerment Technologies 1 (Computational Thinking)>

# Menu for Main Dishes
main_dishes = [{
    "Type": "Chicken",
    "Price": 90.00
}, {
    "Type": "Pork",
    "Price": 105.00
}, {
    "Type": "Fish",
    "Price": 120.00
}, {
    "Type": "Beef",
    "Price": 135.00
}]

# Menu for Side Dishes
side_dishes = [{
    "Type": "Steamed Rice",
    "Price": 20.00
}, {
    "Type": "Shredded Corn",
    "Price": 35.00
}, {
    "Type": "Mashed Potatoes",
    "Price": 50.00
}, {
    "Type": "Steam Vegetables",
    "Price": 65.00
}]

# Menu for Drinks
drinks = [{
    "Type": "Mineral Water",
    "Price": 25.00
}, {
    "Type": "Iced Tea",
    "Price": 35.00
}, {
    "Type": "Soda",
    "Price": 45.00
}, {
    "Type": "Fruit Juice",
    "Price": 55.00
}]


# Function to display the menu
def display_menu():
  print("Menu:")
  print("Main Dishes:")
  for i, dish in enumerate(main_dishes):
    print(f"{i+1}. {dish['Type']} - Price: {dish['Price']}")
  print()
  print("Side Dishes:")
  for i, dish in enumerate(side_dishes):
    print(f"{i+1}. {dish['Type']} - Price: {dish['Price']}")
  print()
  print("Drinks:")
  for i, drink in enumerate(drinks):
    print(f"{i+1}. {drink['Type']} - Price: {drink['Price']}")
  print()


# Function to take the order from the customer
def take_order():
  order = {
      "Mains": None,
      "Sides": None,
      "Drinks": None,
  }

  print("You may now choose your order :)")
  display_menu()

  # Take input for the main dish
  main_id = int(input("Enter the ID of the main dish: "))
  if main_id >= 1 and main_id <= len(main_dishes):
    order["Mains"] = main_dishes[main_id - 1]
  else:
    print("Invalid main dish ID!")
    return None

  # Take input for the side dish
  side_id = int(input("Enter the ID of the side dish: "))
  if side_id >= 1 and side_id <= len(side_dishes):
    order["Sides"] = side_dishes[side_id - 1]
  else:
    print("Invalid side dish ID!")
    return None

  # Take input for the drink
  drink_id = int(input("Enter the ID of the drink: "))
  if drink_id >= 1 and drink_id <= len(drinks):
    order["Drinks"] = drinks[drink_id - 1]
  else:
    print("Invalid drink ID!")
    return None

  return order


# Function to compute the total amount due for the order
def compute_amount_due(order):
  total_amount_due = 0.0

  for category, item in order.items():
    if item is not None:
      total_amount_due += item["Price"]

  return total_amount_due


# Function to process a single order
def process_single_order(order_number):
      print(f"Order {order_number}:")
      order = take_order()
      order_correct = input("Is this order correct (y/n)? ")

      while order_correct.lower() != 'y' and order_correct.lower() != 'n':
          print("Please enter 'y' or 'n'")
          order_correct = input()

      if order_correct.lower() == 'y':
          exclude_item_from_total([order])
          display_total_amount([order])
          generate_receipt(order_number, [order])
          if ask_continue():
              process_single_order(order_number + 1)
          else:
              print("Stopping...")
      else:
          process_single_order(order_number)


def ask_continue():
      user_input = input("Do you want to place another order? (yes/no): ")

      if user_input.lower() == "yes":
          return True
      else:
          return False

def generate_receipt(order_number, orders):
      print(f"\nReceipt for Order {order_number}:")
      subtotal = 0
      for i, order in enumerate(orders, start=1):
          print(f"Order {i}:")
          order_price = 0
          for category, item in order.items():
              if item is not None:
                  item_price = item['Price']
                  print(f" {item['Type']}: P{item_price:.2f}")
                  order_price += item_price
          subtotal += order_price
          print(f"Subtotal: P{order_price:.2f}")
          print()

      print("Total Amount Due:", subtotal)
      print("Each person must pay:", subtotal / len(orders))


def main():
      print("Welcome to Marga & Ria's Restaurant!")
      print("Please select an option:")
      print("1. Order")
      print("2. Exit")

      option = int(input())
      total_amount_due = 0

      if option == 1:
          group_order = input("Group ordering (y/n)? ")

          while group_order.lower() != 'y' and group_order.lower() != 'n':
              print("Please enter 'y' or 'n'")
              group_order = input()

          if group_order.lower() == 'y':
              process_group_orders()
          else:
              process_single_order(1)
      elif option == 2:
          print("Terminating the program.")
      else:
          print("Invalid option. Terminating the program.")

# Function to cancel an order
def cancel_order(orders, group_total):
  order_to_cancel = int(input("Enter the order number to cancel: "))

  if order_to_cancel <= len(orders):
    cancelled_order_amount = group_total / len(orders)
    total -= cancelled_order_amount

    print(f"Order {order_to_cancel} cancelled.")
    print("Cancelled order amount: P " + str(cancelled_order_amount))
    print("Total amount due after cancellation: P " + str(total))
  else:
    print("Invalid order number. Please try again.")


# Function to display the total amount due
def display_total_amount(orders):
  subtotal = 0
  for i, order in enumerate(orders, start=1):
    print(f"Order {i}:")
    order_price = 0
    for category, item in order.items():
      if item is not None:
        item_price = item['Price']
        print(f" {item['Type']}: P{item_price:.2f}")
        order_price += item_price
    subtotal += order_price
    print(f"Subtotal: P{order_price:.2f}")
    print()

  print("Total Amount Due:", subtotal)
  print("Each person must pay:", subtotal / len(orders))


# Function to exclude an item from the total
def exclude_item_from_total(orders):
  print("Exclude an item from the total (y/n)?")
  exclude_item = input()

  if exclude_item.lower() == 'y':
    order_number = int(input("From which order? "))

    if order_number <= len(orders):
      print("Which item will be excluded?")
      print("1. Main")
      print("2. Sides")
      print("3. Drinks")
      choice = int(input("Enter your choice: "))

      if choice == 1:
        # Exclude a main dish
        if 'Mains' in orders[order_number - 1]:
          excluded_item = orders[order_number - 1]['Mains']
          excluded_item['Price'] = 0
          print(
              f"{excluded_item['Type']} main dish will be excluded from the total."
          )
        else:
          print("No main dish found for this order.")
      elif choice == 2:
        # Exclude a side dish
        if 'Sides' in orders[order_number - 1]:
          excluded_item = orders[order_number - 1]['Sides']
          excluded_item['Price'] = 0
          print(
              f"{excluded_item['Type']} side dish will be excluded from the total."
          )
        else:
          print("No side dish found for this order.")
      elif choice == 3:
        # Exclude a drink
        if 'Drinks' in orders[order_number - 1]:
          excluded_item = orders[order_number - 1]['Drinks']
          excluded_item['Price'] = 0
          print(
              f"{excluded_item['Type']} drink will be excluded from the total."
          )
        else:
          print("No drink found for this order.")
      else:
        print("Invalid choice.")
    else:
      print("Invalid order number. Please try again.")


def process_group_orders():
  group_size = int(input("How many people are in your group: "))
  orders = []

  i = 0
  while i < group_size:
    order = process_single_order(i + 1)
    orders.append(order)

    if i < group_size - 1:
      proceed_next = input("Proceed with the next order (y/n)? ")

      while proceed_next.lower() != 'y' and proceed_next.lower() != 'n':
        print("Please enter 'y' or 'n'")
        proceed_next = input()

      if proceed_next.lower() != 'y':
        break

    i += 1

  exclude_item_from_total(orders)
  display_total_amount(orders)


def add_item_to_order(order):
  item_type = input("Enter the item type: ")
  item_price = float(input("Enter the item price: "))

  order.append({'Type': item_type, 'Price': item_price})
  print(f"{item_type} added to the order.")


def process_single_order(order_number):
  print(f"Order {order_number}:")
  order = take_order()
  order_correct = input("Is this order correct (y/n)? ")

  while order_correct.lower() != 'y' and order_correct.lower() != 'n':
    print("Please enter 'y' or 'n'")
    order_correct = input()

  if order_correct.lower() == 'y':
    return order
  else:
    return process_single_order(order_number)


def ask_continue():
  user_input = input("Do you want to place another order? (yes/no): ")

  if user_input.lower() == "yes":
    return True
  else:
    return False

def main():
    print("Welcome to Marga & Ria's Restaurant!")
    print("Please select an option:")
    print("1. Order")
    print("2. Exit")

    option = int(input())
    total_amount_due = 0
    orders = []  # List to store orders

    if option == 1:
        group_order = input("Group ordering (y/n)? ")

        while group_order.lower() != 'y' and group_order.lower() != 'n':
            print("Please enter 'y' or 'n'")
            group_order = input()

        if group_order.lower() == 'y':
            group_size = int(input("How many people are in your group: "))
            group_orders = []

            for i in range(1, group_size + 1):
                order = process_single_order(i)
                group_orders.append(order)

                if i < group_size:
                    proceed_next = input("Proceed with the next order (y/n)? ")

                    while proceed_next.lower() != 'y' and proceed_next.lower() != 'n':
                        print("Please enter 'y' or 'n'")
                        proceed_next = input()

                    if proceed_next.lower() != 'y':
                        break

            exclude_item_from_total(group_orders)
            total_amount_due = sum(compute_amount_due(order) for order in group_orders)
            display_total_amount(group_orders)

            #Function to generate receipt for group order
            print("\nReceipt for Group Order:")
            for i, order in enumerate(group_orders, start=1):
                print(f"Order {i}:")
                order_price = 0
                for category, item in order.items():
                    if item is not None:
                        item_price = item['Price']
                        print(f" {item['Type']}: P{item_price:.2f}")
                        order_price += item_price
                print(f"Subtotal: P{order_price:.2f}")
                print()

            print("Total Amount Due:", total_amount_due)
            print("Each person must pay:", total_amount_due / len(group_orders))

        else:
            order = process_single_order(1)
          # ... (previous code)

        def process_group_orders():
              group_size = int(input("How many people are in your group: "))
              orders = [None] * group_size  # Initialize a list with 'None' placeholders

              for i in range(group_size):
                  order = process_single_order(i + 1)
                  orders[i] = order

                  if i < group_size - 1:
                      proceed_next = input("Proceed with the next order (y/n)? ")

                      while proceed_next.lower() != 'y' and proceed_next.lower() != 'n':
                          print("Please enter 'y' or 'n'")
                          proceed_next = input()

                      if proceed_next.lower() != 'y':
                          break

              exclude_item_from_total(orders)
              display_total_amount(orders)



       #Function to generate receipt for single order
              print("\nReceipt for Single Order:")
              for i, order in enumerate(orders, start=1):
                print(f"Order {i}:")
                order_price = 0
                for category, item in order.items():
                    if item is not None:
                        item_price = item['Price']
                        print(f" {item['Type']}: P{item_price:.2f}")
                        order_price += item_price
                print(f"Subtotal: P{order_price:.2f}")
                print()

                print("Total Amount Due:", total_amount_due)
                print("Each person must pay:", total_amount_due / len(orders))

    elif option == 2:
        print("Terminating the program.")
    else:
        print("Invalid option. Terminating the program.")

    if ask_continue():
        main()
    else:
        print("Stopping...")

main()
