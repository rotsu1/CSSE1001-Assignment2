__author__ = "Ryu Otsu"
__email__ = "s4800316@uqconnenct.edu.au"
__date__ = "05/04/2023"

from a2_support import *

class Card():
    """
    An absract class from which all instantiable types of cards inheret.
    """
    def __init__(self) -> None:
        """
        The initial values for Card.
        """
        self._damage = 0
        self._block = 0
        self._energy = 1
        self._status = {}
        self._name = "Card"
        self._description = "A card."
        self._target = True
    
    def get_damage_amount(self) -> int:
        """
        Returns the amount of damage this card does to its target.

        Return:
            int: damage amount.
        """
        return self._damage

    def get_block(self) -> int:
        """
        Returns the amount of block this card adds to its user.

        Return:
            int: block amount.
        """
        return self._block

    def get_energy_cost(self) -> int:
        """
        Returns the amount of energy this card costs to play.

        Return:
            int: energy cost.
        """
        return self._energy

    def get_status_modifiers(self) -> dict[str, int]:
        """
        Returns a dictionary describing each status modifiers applied when the
        card is played.

        Return:
            dictionary: status of the card.
        """
        return self._status

    def get_name(self) -> str:
        """
        Returns the name of the card.

        Return:
            str: name of card.
        """
        return self._name

    def get_description(self) -> str:
        """
        Returns a description of the card.

        Return:
            str: description of card.
        """
        return self._description

    def requires_target(self) -> bool:
        """
        Returns True if playing this card requires a target, and False if it
        does not.

        Return:
            bool.
        """
        return self._target

    def __str__(self) -> str:
        """
        Returns the string representation for the card.

        Return:
            str: string representation.
        """
        return f"{self._name}: {self._description}"

    def __repr__(self) -> str:
        """
        Returns the text that would be required to create a new instance of this
        class identical to self.

        Return:
            str: class name.
        """
        return self._name + "()"

class Strike(Card):
    """
    Deals 6 damage to its target.
    Costs 1 energy to play.
    """
    def __init__(self) -> None:
        """
        The initial value for Strike.
        """
        super().__init__()
        self._damage = 6
        self._name = "Strike"
        self._description = "Deal 6 damage."

class Defend(Card):
    """
    Adds 5 block to its user.
    Does not require a target.
    Costs 1 energy to play.
    """
    def __init__(self) -> None:
        """
        The initial value for Defend.
        """
        super().__init__()
        self._block = 5
        self._name = "Defend"
        self._description = "Gain 5 block."
        self._target = False

class Bash(Card):
    """
    Adds 5 block to its user and causes 7 damage to its target.
    Costs 2 energy to play.
    """
    def __init__(self) -> None:
        """
        The initial value for Bash.
        """
        super().__init__()
        self._damage = 7
        self._block = 5
        self._energy = 2
        self._name = "Bash"
        self._description = "Deal 7 damage. Gain 5 block."

class Neutralize(Card):
    """
    Deals 3 damage to its target.
    Applies 1 weak and 2 vulnerable to its target.
    Costs 0 energy to play.
    """
    def __init__(self) -> None:
        """
        The initial value for Neutralize.
        """
        super().__init__()
        self._damage = 3
        self._energy = 0
        self._status = {
            "weak": 1,
            "vulnerable": 2
            }
        self._name = "Neutralize"
        self._description = "Deal 3 damage. Apply 1 weak. Apply 2 vulnerable."

class Survivor(Card):
    """
    Adds 8 block and applies 1 strength to its user.
    Does not require a target.
    Costs 1 energy to play.
    """
    def __init__(self) -> None:
        """
        The initial value for Survivor.
        """
        super().__init__()
        self._block = 8
        self._status = {
            "strength": 1
            }
        self._name = "Survivor"
        self._description = "Gain 8 block and 1 strength."
        self._target = False

class Entity():
    """
    This class provides the base entity funtionality that all entities inherit.
    """
    def __init__(self, max_hp: int) -> None:
        """
        The initial value for Entity.

        Parameters:
            max_hp(int): The maximum amount of HP the entity can have.
        """
        self._max_hp = max_hp
        self._hp = max_hp
        self._block = 0
        self._strength = 0
        self._weak = 0
        self._vulnerable = 0

    def get_hp(self) -> int:
        """
        Returns the current HP for this entity.

        Return:
            int: current HP.
        """
        return self._hp

    def get_max_hp(self) -> int:
        """
        Returns the maximum possible HP for this entity.
        
        Return:
            int: maximum HP.
        """
        return self._max_hp

    def get_block(self) -> int:
        """
        Returns the amount of block for this entity.

        Return:
            int: block amount.
        """
        return self._block

    def get_strength(self) -> int:
        """
        Returns the amount of strength for this entity.

        Return:
            int: strength amount.
        """
        return self._strength

    def get_weak(self) -> int:
        """
        Returns the number of turns for which this entity is weak.

        Return:
            int: weak amount.
        """
        return self._weak

    def get_vulnerable(self) -> int:
        """
        Returns the number of turns for which this entity is vulnerable.

        Return:
            int: vulnerable amount.
        """
        return self._vulnerable

    def get_name(self) -> str:
        """
        Returns the name of the entity.

        Return:
            str: name of entity.
        """
        return self.__class__.__name__

    def reduce_hp(self, amount: int) -> None:
        """
        Attacks the entity with a damage of amount.
        This involves reducing block until it reaches 0.

        Parameters:
            amount(int): the amount of hp that is going to be reduced.
        """
        if self._block > 0:
            self._block -= amount
            if self._block < 0:
                self._hp += self._block
                self._block = 0
        else:
            self._hp -= amount

        if self._hp < 0:
                    self._hp = 0

    def is_defeated(self) -> bool:
        """
        Returns True if the entity is defeated, and False otherwise.
        It is considered defeat if it has 0 HP.
        """
        if self._hp == 0:
            return True
        else:
            return False

    def add_block(self, amount: int) -> None:
        """
        Adds the given amount to the amount of block this entity has.

        Parameters:
            amount(int): the amount of block that is going to be added to the
                         entity.
        """
        self._block += amount

    def add_strength(self, amount: int) -> None:
        """
        Adds the given amount to the amount of strength this entity has.

        Parameters:
            amount(int): the amount of strength that is going to be added to the
                         entity.
        """
        self._strength += amount

    def add_weak(self, amount: int) -> None:
        """
        Adds the given amount to the amount of weak this entity has.

        Parameters:
            amount(int): the amount of weak that is going to be added to the
                         entity.
        """
        self._weak += amount

    def add_vulnerable(self, amount: int) -> None:
        """
        Adds the given amount to the amount of vulnerable this entity has.

        Parameters:
            amount(int): the amount of vulnerable that is going to be added to
                         the entity.
        """
        self._vulnerable += amount

    def new_turn(self) -> None:
        """
        Applies any status changes that occur when a new turn begins.
        This involves:
            block back to 0
            redcuing weak and vulnerable each by 1 if they are greater than 0.
        """
        self._block = 0
        if self._weak > 0:
            self._weak -= 1
        if self._vulnerable > 0:
            self._vulnerable -= 1
        
    def __str__(self) -> str:
        """
        Returns the entity name with entity name and hp/max_hp.

        Return:
            str: name of the entity with hp/max_hp.
        """
        return f"{self.__class__.__name__}: {self._hp}/{self._max_hp} " + "HP"

    def __repr__(self) -> str:
        """
        Returns the entity name with max_hp.

        Return:
            str: name of entity with max_hp.
        """
        return f"{self.__class__.__name__}({self._max_hp})"

class Player(Entity):
    """
    The type of entity that the user controls.
    """
    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        """
        The initial value for Player.

        Parameters:
            max_hp(int): max HP of the Player.
            cards(list[Card]): list of the players cards. 
        """
        super().__init__(max_hp)
        self._energy = 3
        self._deck = cards
        self._hand = []
        self._discard = []

    def get_energy(self) -> int:
        """
        Returns the amount of energy the user has remaining.

        Return:
            int: amount of energy.
        """
        return self._energy

    def get_hand(self) -> list[Card]:
        """
        Returns the players current hand.

        Return:
            list[Card]: players current hand.
        """
        return self._hand

    def get_deck(self) -> list[Card]:
        """
        Returns the players current deck.

        Return:
            list[Card]: players current hand.
        """
        return self._deck

    def get_discarded(self) -> list[Card]:
        """
        Returns the players current discard pile.

        Return:
            list[Card]: players current discard pile.
        """
        return self._discard

    def start_new_encounter(self) -> None:
        """
        This method adds all cards from the player’s discard pile to the end of
        their deck, and sets the discard pile to be an empty list.

        Pre-condition:
            player's hand should be empty when it is called.
        """
        self._deck.extend(self._discard)
        self._discard.clear()

    def end_turn(self) -> None:
        """
        This method adds all remaining cards from the player’s hand to the end
        of their discard pile, and sets their hand back to an empty list.
        """
        self._discard.extend(self._hand)
        self._hand = []

    def new_turn(self) -> None:
        """
        This method sets the player up for a new turn.
        This involves everything that a regular entity requires for a new turn,
        but also requires that the player be dealt a new hand of 5 cards, and
        energy be reset to 3.
        """
        super().new_turn()
        draw_cards(self._deck, self._hand, self._discard)
        self._energy = 3       

    def play_card(self, card_name: str) -> Card | None:
        """
        Attempts to play a card from the player’s hand.
        If the name exists in the player's hand, and the player has enough
        energy, the card will move from the player's hand to the discard pile.
        The energy will be deducted and the card is returned.

        Parameters:
            card_name(str): the card that is going to be used.

        Return:
            Card(class): instance of the card.

            None: if the name does not exist in the player's hand.
        """
        for hand in self._hand:
            if (type(hand).__name__ == card_name and
                hand.get_energy_cost() <= self._energy):
                # Checks if the card is in the player's hand and
                # have enough energy
                self._hand.remove(hand)
                self._discard.append(hand)
                self._energy -= hand.get_energy_cost()
                return hand

        return None

    def __repr__(self) -> None:
        """
        Returns the player name, max HP and deck.
        """
        return f"{self.__class__.__name__}({self._max_hp}, {self._deck})"

class IronClad(Player):
    """
    Type of player the user can choose from.
    IronClad starts with 80 HP.
    Contains 5 Strike, 4 Defend, and 1 Bash in the deck.
    """
    def __init__(self) -> None:
        """
        The initial value for IronClad.
        """
        super().__init__(max_hp = 80, cards = [Strike(), Strike(), Strike(),
                        Strike(),Strike(), Defend(), Defend(), Defend(),
                        Defend(), Bash()])

    def __repr__(self) -> None:
        """
        Returns the text that would be required to create a new instance of this
        class identical to self.
        """
        return f"{self.__class__.__name__}()"

class Silent(Player):
    """
    Type of player the user can choose from.
    Silent starts with 70 HP.
    Contains 5 Strike, 5 Defend, 1 Neutralize, and 1 Survivor in the deck.
    """
    def __init__(self) -> None:
        """
        The initial value for Silent.
        """
        super().__init__(max_hp = 70, cards = [Strike(), Strike(), Strike(),
                        Strike(),Strike(),Defend(), Defend(), Defend(),
                        Defend(), Defend(), Neutralize(), Survivor()])

    def __repr__(self) -> None:
        """
        Returns the text that would be required to create a new instance of this
        class identical to self.
        """
        return f"{self.__class__.__name__}()"

class Monster(Entity):
    """
    Type of entity that the user battles during the encounters.
    Each monster will have a unique ID.
    """
    unique_id = 0   
    def __init__(self, max_hp: int) -> None:
        """
        The initial value for Monster.
        """
        super().__init__(max_hp)
        self._id = Monster.unique_id
        Monster.unique_id += 1
        self._monsters_action = {} # dict of the monsters ability {ability: int}
    
    def get_id(self) -> int:
        """
        Returns the monsters ID.
        """
        return self._id

    def action(self) -> dict[str, int]:
        """
        Returns the action of the monster.
        """
        raise NotImplementedError

    def __repr__(self) -> None:
        """
        Returns the text that would be required to create a new instance of this
        class identical to self.
        """
        return f"{self.__class__.__name__}({self._max_hp})"


class Louse(Monster):
    """
    Type of monster that the user battles during the encounters.
    """
    def __init__(self, max_hp: int) -> None:
        """
        The initial value for Louse.

        Parameter:
            max_hp(int): the maximum HP of Louse.
        """
        super().__init__(max_hp)
        self._monsters_action = {
            "damage": random_louse_amount()
            }
        
    def action(self) -> dict[str, int]:
        """
        Returns a dictionary of {'damage': amount}.
        Amount is an random integer betweeen 5 and 7.

        Return:
            dict[str, int]: damage amount.
        """
        return self._monsters_action

class Cultist(Monster):
    """
    Type of monster that the user battles during the encounters.
    """
    def __init__(self, max_hp: int) -> None:
        """
        The initial value of Cultist.

        Parameters:
            max_hp(int): the maximum HP of Cultist.
        """
        super().__init__(max_hp)
        self._monsters_action = {
            "damage": 0,
            "weak": 0
            }
        self._num_calls = 0 # The number of times action() is called
    def action(self) -> dict[str, int]:
        """
        Returns a dictionary of {'damage'; damage_amount, 'weak': weak_amount'}
        Cultists damage starts from 0 and increases by 6 + (number of times
        action method is called).
        Weak alternates between 0 and 1 each time action method is called.

        Return:
            dict[str, int]: damage amount and weak amount.
        """
        if self._num_calls == 0:
            self._num_calls = 1
            return self._monsters_action

        else: 
            self._monsters_action["damage"] = 6 + self._num_calls
            self._num_calls += 1
            
            if self._num_calls % 2 == 0: # When even number of times the method
                                         # is called
                self._monsters_action["weak"] = 1
                return self._monsters_action
            
            elif self._num_calls % 2 == 1: # When odd number of times the method
                                           # is called
                self._monsters_action["weak"] = 0
                return self._monsters_action

class JawWorm(Monster):
    """
    Type of monster that the user battles during the encounters.
    """
    def __init__(self, max_hp: int) -> None:
        """
        The initial value for JawWorm.

        Parameter:
            max_hp(int): the maximum HP of JawWorm
        """
        super().__init__(max_hp)
        self._monsters_action = {
            "damage": 0,
            }
    def action(self) -> dict[str, int]:
        """
        Each time the action is called:
            1/2 of damage the jaw worm has taken so far (rounding up)
            is added to the jaw worm’s own block amount.
            1/2 of damage the jaw worm has taken so far (rounding down)
            is used for damage to the target.

        Return:
            dict[str, int]: damage amount
        """
        if self._hp == self._max_hp:
            return self._monsters_action
        else: # If JawWorm has took at least 1 damage
            if (self._max_hp - self._hp) % 2 == 1: # When the damage taken is an
                                                   # odd number
                self._block += int((self._max_hp - self._hp) / 2 + 0.5)
                # Round up the block
            elif (self._max_hp - self._hp) % 2 == 0: # When the damage taken is
                                                     # an even number
                self._block += int((self._max_hp - self._hp) / 2)
                
            self._monsters_action["damage"] = int((self._max_hp - self._hp) / 2)
            # Round down the damage
            return self._monsters_action

class Encounter():
    """
    Represents each encounter in the game.
    """
    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """
        The initial value for Encouter.

        Parameter:
            player(Player): the player name.
            monsters(list[tuple[str, int]): monsters that will be encounted.
        """
        self._player = player
        self._list_of_monsters = [] # list of monster instances
        for each_monster in monsters: # Making a list of monster instances
            name, max_hp = each_monster
            monster = globals()[name](max_hp)
            self._list_of_monsters.append(monster)
        self._player.start_new_encounter()
        self.start_new_turn()
        self._turn = True # It is the player's turn when it is true.

    def start_new_turn(self) -> None:
        """
        Sets it to be the player's turn.
        """
        self._player.new_turn()
        self._turn = True
    
    def end_player_turn(self) -> None:
        """
        Sets it to be the player's turn.
        """
        self._player.end_turn()
        for monster in self._list_of_monsters:
            monster.new_turn()
        self._turn = False

    def get_player(self) -> Player:
        """
        Returns the player in this encounter.

        Return:
            Player: player.
        """
        return self._player

    def get_monsters(self) -> list[Monster]:
        """
        Returns the list of monsters.

        Return:
            list[Monster]: list of monsters.
            
        """
        return self._list_of_monsters

    def is_active(self) -> bool:
        """
        Returns True if there are monsters remaining in this encounter.

        Return:
            bool.
        """
        if self._list_of_monsters == []:
            return False
        else:
            return True

    def player_apply_card(self, card_name: str, target_id: int
                          | None = None)-> bool:
        """
        Attempts to apply the card with the given name, and target ID where
        relevant.

        Parameter:
            card_name(str): card name.
            target_id(int): ID of the monster.

        Return:
            bool.
        """
        cards = {
            "Strike": Strike(),
            "Defend": Defend(),
            "Bash": Bash(),
            "Neutralize": Neutralize(),
            "Survivor": Survivor()
            }
        
        if self._turn == False:
            return False

        if card_name in cards:
            card = cards[card_name]
        else:
            return False

        if self._turn == True:
            
            if card.requires_target() == True and target_id == None:
                return False
            
            if target_id != None: # Checks if the given ID is existing in the
                                  # encounter
                list_of_ids = [] # list of monsters unique ID
                for monster in self._list_of_monsters:
                    list_of_ids.append(monster.get_id())
                    
                if target_id not in list_of_ids:
                    return False
                
            play = self._player.play_card(card_name)
            
            if play == None: # Check if card application failed
                return False
            
            self._player.add_block(card.get_block())
            
            if "strength" in card.get_status_modifiers():
                self._player.add_strength(
                    card.get_status_modifiers()["strength"]
                    )

            for monster in self._list_of_monsters:
                
                if monster.get_id() == target_id:
                    
                    if "vulnerable" in card.get_status_modifiers():
                        monster.add_vulnerable(
                            card.get_status_modifiers()["vulnerable"]
                            )
                        
                    if "weak" in card.get_status_modifiers():
                        monster.add_weak(
                            card.get_status_modifiers()["weak"]
                            )
                        
                    damage = (
                        card.get_damage_amount() + self._player.get_strength()
                        )
                    
                    if monster.get_vulnerable() > 0:
                        damage *= 1.5
                        
                    if self._player.get_weak() > 0:
                        damage = damage * 0.75
                        
                    monster.reduce_hp(int(damage))
                    
                    if monster.get_hp() == 0:
                        self._list_of_monsters.remove(monster)
                
            return True
                    


    def enemy_turn(self) -> None:
        """
        Allows all remaining monsters in the encounter to take an action.
        """
        if self._turn == False:
            
            for monster in self._list_of_monsters: # each monster will make
                                                   # their action
                action = monster.action()
                damage = action["damage"]
                
                if "weak" in action:
                    self._player.add_weak(action["weak"])
                    
                if "vulnerable" in action:
                    self._player.add_vulnerable(action["vulnerable"])
                    
                if "strength" in action:
                    monster.add_strength(action["strength"])
                    
                damage += monster._strength
                
                if self._player.get_vulnerable() > 0:
                    damage *= 1.5
                    
                if monster.get_weak() > 0:
                    damage *= 0.75
                    
                self._player.reduce_hp(int(damage))
                
        return self.start_new_turn()
        

def main():
    players = {
        "ironclad": IronClad(),
        "silent": Silent()
        }
    
    player_type = input("Enter a player type: ")
    while player_type not in players:
        print("Please enter a valid player")
        player_type = input("Enter a player type: ")
    
    for player in players: # Check if the input is an existing player
                           # If it does, prompt for a game file 
        if player_type == player:
            player_type = players[player]
            game_file = input("Enter a game file: ")
            
    for encounter_monsters in read_game_file(game_file): # Loops over each
                                                         # encounter
        if player_type.get_hp() == 0:
            break
        
        print("New encounter!\n")
        encounter = Encounter(player_type, encounter_monsters)
        display_encounter(encounter)
        
        while encounter.is_active() == True:
            if player_type.get_hp() == 0:
                print(GAME_LOSE_MESSAGE)
                break
            
            command = input("Enter a move: ")
            
            if command == "end turn":
                encounter.end_player_turn()
                encounter.enemy_turn()
                
                if player_type.get_hp() > 0:
                    display_encounter(encounter)
                    
            elif command == "inspect deck":
                print(f"\n{player_type.get_deck()}\n")
                
            elif command == "inspect discard":
                print(f"\n{player_type.get_discarded()}\n")
                
            elif command.split()[0] == "describe":
                card_name = command.split()[-1]
                print(f"\n{globals()[card_name]().get_description()}\n")
                
            elif command.split()[0] == "play":
                if command.split()[-1].isnumeric(): # Checks if the user has
                                                    # inputted an int at the end
                    apply_card = encounter.player_apply_card(
                        command.split()[1], int(command.split()[-1])
                        )
                else:
                    apply_card = encounter.player_apply_card(
                        command.split()[1]
                        )
                    
                if apply_card == False: 
                    print(CARD_FAILURE_MESSAGE)
                else:
                    display_encounter(encounter)

            if encounter.is_active() == False:
                print(ENCOUNTER_WIN_MESSAGE)

    if player_type.get_hp() > 0:
        print(GAME_WIN_MESSAGE)

if __name__ == '__main__':
    main()
