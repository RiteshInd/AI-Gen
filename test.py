# import time
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def get_balance(self):
#         return self.__balance
    
#     def deposit(self, amount):
#         self.__balance += amount
        
#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds") 
            
# account=BankAccount(1000)

# print("Initial Balance:", account.get_balance())
# account.deposit(500)
# print("Balance after deposit:", account.get_balance())
# account.withdraw(200)
# print("Balance after withdrawal:", account.get_balance())
# account.withdraw(1500)
# time.sleep(1)
# print("Final Balance:", account.get_balance())
# print(account._BankAccount__balance)


# class Player:
#     def __init__(self, name, sports):
#         self.name = name
#         self.sports = sports
    
#     def _run(self):
#         print(f"{self.name} is running in {self.sports}")
#         return "Running"
    
# class Coach:
#     def __init__(self, name, player):
#         self.name = name
#         self.player = player
        
#     def command_player(self):
#         return self.player._run()
    
# player = Player("John", "Football")

# coach = Coach("Mike", player)

# print(coach.command_player())  # This will raise an AttributeError since __run is private



import logging
from logging.handlers import RotatingFileHandler

# Step 1: Create a custom logger
logger = logging.getLogger("MyAppLogger")
logger.setLevel(logging.DEBUG)  # Log everything from DEBUG and above

# Step 2: Create handlers

# Console handler (prints to terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Show INFO+ messages on console

# Rotating file handler (max 1MB per file, keep 3 backups)
file_handler = RotatingFileHandler(
    "app.log", maxBytes=1_000_000, backupCount=3
)
file_handler.setLevel(logging.DEBUG)  # Log everything to file

# Step 3: Create formatters and add to handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Step 4: Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# === Classes using custom logger ===

class Player:
    def __init__(self, name, sports):
        self.name = name
        self.sports = sports
        logger.info(f"Player created: {self.name}, Sport: {self.sports}")

    def __run(self):
        logger.debug(f"{self.name} is executing __run method.")
        print(f"{self.name} is running in {self.sports}")
        return "Running"

    def start_training(self):
        logger.debug(f"{self.name} called start_training.")
        return self.__run()


class Coach:
    def __init__(self, name, player):
        self.name = name

        if not isinstance(player, Player):
            logger.warning(
                f"Invalid player assigned to Coach '{self.name}'. Expected Player instance, got {type(player).__name__}."
            )
            self.player = None
        else:
            self.player = player
            logger.info(f"Coach '{self.name}' assigned to Player '{self.player.name}'.")

    def command_player(self):
        logger.debug(f"{self.name} called command_player.")
        if self.player is None:
            logger.error(f"Coach '{self.name}' attempted to command an invalid (None) player.")
            return "No valid player to command."

        logger.info(f"Coach '{self.name}' is commanding '{self.player.name}'.")
        return self.player.start_training()


# === Testing ===

# Invalid player
coach1 = Coach("Mike", "NotAPlayerObject")
print(coach1.command_player())

# Valid player
player = Player("John", "Football")
coach2 = Coach("Alex", player)
print(coach2.command_player())
