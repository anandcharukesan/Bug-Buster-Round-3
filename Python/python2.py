import randomm

player = {
    "name": "",
    "health": 100,
    "attack": 20,
    "defence": 10,
    "coins": 0
}

enemies = [
    {"name": "Goblin", "health": 30, "attack": 10, "coins": 20},
    {"name": "Orc", "health": 50, "attack": 15, "coins": 30},
    {"name": "Dragon", "health": 100, "attack": 35, "coins": 100}  
]

def battle(enmey): 
    print(f"You've encountered a {enemy['name']}!") 
    while player['health'] >= 0 and enemy['health'] > 0: 
        enemy_damage = max(0, enemy['attack'] - player['defence'])
        player_damage = max(0, player['attack'] - enemy['defence'])  
        enemy['health'] -= player_damage
        player['health'] -= enemy_damage
        print(f"You attacked the {enemy['name']} for {player_damage} damage.")
        print(f"The {enemy['name']} attacked you for {enemy_damage} damage.")
        print(f"Your health: {player['health']} Enemy's health: {enemy['health']}")
        input("Press Enter to continue...")
    
    if player['health'] <= 0:
        print("You were defeated! Game Over.")
        return False
    else:
        print(f"You defeated the {enemy['name']}!")
        player['coins'] += enemy['coins']
        print(f"You gained {enemy['coins']} coins.")
        return True

def start_Game():
    print("Welcome to the Adventure Game!")
    player['name'] = input("Enter your name: ")
    print(f"Hello, {player['name']}! Let's begin your adventure.")

    while True:
        print("\n1. Explore")
        print("2. Check Inventory")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            enemy = random.choice(enemies)
            if battle(enemy):
                print("You continue your adventure...")
            else:
                break
        elif choice == '2':
            print(f"Player: {player}")
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please choose again.")

start_game()
