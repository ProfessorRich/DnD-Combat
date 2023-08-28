from random import randint
import os

times_ran = 0

class creature:    
    def __init__(self, name, max_hp, ac, attacks, speed, str, dex, con, int, wis, cha, resistances, vulnerabilities, immunities, size, type, alignment, notes):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.ac = ac
        self.attacks = attacks
        self.speed = speed
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.resistances = resistances
        self.vulnerabilities = vulnerabilities
        self.immunities = immunities
        self.size = size
        self.type = type
        self.alignment = alignment
        self.notes = notes
        self.target=None
        self.wins=0
        
    def get_name(self):
        return self.name
        
    def set_target(self, creature):
        self.target=creature
        
    def clear_target(self):
        self.target=None
        
    def get_target(self):
        return self.target
    
    def get_attacks(self):
        return self.attacks
    
    def get_hp(self):
        return self.hp
    
    def reset_hp(self):
        self.hp = self.max_hp
    
    def get_max_hp(self):
        return self.max_hp
    
    def get_wins(self):
        return self.wins
    
    def plus_one_win(self):
        self.wins = self.wins + 1
        
class dice_roll_required:
    def __init__(self, number_of_dice, dice_sides, bonus):
        self.number_of_dice = number_of_dice
        self.dice_sides = dice_sides
        self.bonus = bonus
        
combat_mode = True
print_status = False

def combat_over(creatures_and_turn_order_sorted):
    global combat_mode
    combat_mode=False
    
    for creature_and_turn_order in creatures_and_turn_order_sorted:
        creature=creature_and_turn_order['creature']
        if is_alive(creature):
            creature.plus_one_win()
        
def run_turn(creatures_and_turn_order_sorted):
        os.system('cls')
        print_round_status(creatures_and_turn_order_sorted)
        take_all_turns(creatures_and_turn_order_sorted)

def run_combat(creatures_and_turn_order_sorted):
    while combat_mode:
        run_turn(creatures_and_turn_order_sorted)  
        if print_status:
            print("\nPress any key..." + "\n")
            input()
        
def roll_initiative_and_sort_all_creatures(creatures):
    creatures_and_turn_order_unsorted = roll_initiative_for_all_creatures(creatures)
    creatures_and_turn_order_sorted = sort_initiative_and_creatures(creatures_and_turn_order_unsorted)
    return creatures_and_turn_order_sorted
        
def roll_initiative_for_all_creatures(creatures):
    creatures_and_turn_order_unsorted=[]
    for creature in creatures:
        initiative = roll_initiative(creature)
        creatures_and_turn_order_unsorted.append({'initiative': initiative, 'creature': creature})        
        
    return creatures_and_turn_order_unsorted
        
def sort_initiative_and_creatures(creatures_and_turn_order_unsorted):     
    creatures_and_turn_order_sorted = sorted(creatures_and_turn_order_unsorted, key=lambda x: x['initiative'], reverse=True)
    return creatures_and_turn_order_sorted

def is_alive(creature):
    if creature.get_hp() <= 0:
        return False
    else:
        return True

def take_all_turns(creatures_and_turn_order_sorted):
    
    for creature_and_initiative in creatures_and_turn_order_sorted:
        creature = creature_and_initiative['creature']
        if is_alive(creature):
            take_turn(creature)
            
        
def take_turn(creature):
    if print_status:
        print("It is " + creature.get_name() + "'s turn...\n")
    take_all_attacks(creature)
    
def dice_roll_actioned(dice_roll_required):
    total_dice_result = 0
    
    for n in range(dice_roll_required.number_of_dice):
        total_dice_result += randint(1, dice_roll_required.dice_sides)
    
    total_result=total_dice_result + dice_roll_required.bonus
    return total_result

def get_ability_score_modifier(ability_score):
    modifier = (ability_score - 10) // 2
    return modifier

def take_all_attacks(attacker):
    defender = attacker.get_target()
    
    for attack in attacker.get_attacks():
        if is_alive(defender):
            if print_status:
                print(attacker.get_name())
            if roll_to_hit(attack, defender) == True:
                damage = roll_damage(attack['damage'])
                take_damage(damage, defender)
                if not(is_alive(defender)):
                    if print_status:
                        print(defender.get_name() + " has died horribly!")
                        
            else:
                if print_status:
                    print(" misses!")
            
def roll_initiative(creature):
    initiative_modifier = get_ability_score_modifier(creature.dex)
    initiative = dice_roll_actioned(dice_roll_required(1, 20, initiative_modifier))
    
    if print_status:
        print(creature.get_name() + " has rolled an initiative of " + str(initiative))
    
    return initiative

def roll_to_hit(attack_of_attacker, defender):
    hit_roll = dice_roll_actioned(dice_roll_required(1, 20, attack_of_attacker['attack_modifier']))
    if hit_roll >= defender.ac:
        if print_status:
            print(" hits with his " + attack_of_attacker['attack'])
        return True
    else:
        return False
    
def roll_damage(dice):
    dice_result=dice_roll_actioned(dice)
    if print_status:
        print(" for " + str(dice_result) + " points of damage!\n")
    return dice_result

def take_damage(damage, defender):
    defender.hp -= damage
    
def is_hp_greater_than_zero(creature):
    if creature.hp > 0:
        True
    else:
        False
        
def set_all_targets_to_next_creature(creatures):
    
    target_creature=None
    
    for creature in creatures:
        creature.set_target(target_creature)
        target_creature=creature
        
    creatures[0].set_target(target_creature)
    
def check_all_targets(creatures):
    for creature in creatures:
        print(creature.get_name() + " " + creature.get_target().get_name() + "")
        
def print_round_status(creatures_and_turn_order_sorted):
    for creature_and_turn_order in creatures_and_turn_order_sorted:
        creature = creature_and_turn_order['creature']
        print(creature.get_name() + " has " + str(creature.get_hp()) + "hp out of " + str(creature.get_max_hp()) + "hp.")
        if not(is_alive(creature)):
            print(creature.get_name() + " is dead.")
            combat_over(creatures_and_turn_order_sorted)

            
def reset_creatures(creatures):
    for creature in creatures:
        creature.reset_hp()
        
def run_combat_x_times(x, creatures):
    global times_ran
    global combat_mode
    set_all_targets_to_next_creature(creatures)
    while x > 0:
        x = x - 1
        initiative_and_creatures = roll_initiative_and_sort_all_creatures(creatures)
        run_combat(initiative_and_creatures)
        reset_creatures(creatures)
        times_ran = times_ran + 1
        combat_mode = True
        
    print("Combat was ran " + str(times_ran) + " times.")
    
    for creature in creatures:
        print(creature.get_name() + " won " + str(creature.get_wins()) + " times.")        
    
    
test_1 = creature('Arnold the Anvil', 89, 21, [{'attack': 'Longsword', 'attack_modifier': 8, 'damage': dice_roll_required(1, 8, 8), 'range': 0}, {'attack': 'Longsword', 'attack_modifier': 8, 'damage': dice_roll_required(1, 8, 8), 'range': 0}], 30, 18, 14, 16, 12, 13, 13, [], [], [], 'M', 'Humanoid', 'LG', '')
test_2 = creature('Bolt', 100, 18, [{'attack': 'Morphed Limb', 'attack_modifier': 10, 'damage': dice_roll_required(2, 8, 2), 'range': 5},{'attack': 'Morphed Limb', 'attack_modifier': 10, 'damage': dice_roll_required(2, 8, 2), 'range': 5},{'attack': 'Morphed Limb', 'attack_modifier': 10, 'damage': dice_roll_required(2, 8, 2), 'range': 5}], 30, 18, 14, 18, 6, 12, 6, [], [], [], 'L', 'Demon', 'CE', '')
test_3 = creature('ODreadnaught', 90, 15, [{'attack': 'Slam', 'attack_modifier': 8, 'damage': dice_roll_required(3, 6, 6), 'range': 5}], 30, 18, 14, 18, 6, 12, 6, [], [], [], 'L', 'Demon', 'CE', '')
test_4 = creature('Energy Cube', 130, 10, [{'attack': 'Psuedopod', 'attack_modifier': 5, 'damage': dice_roll_required(6, 6, 3), 'range': 5}], 30, 18, 14, 18, 6, 12, 6, [], [], [], 'L', 'Demon', 'CE', '')
test_creatures_in_combat = [test_1, test_2]
run_combat_x_times(100, test_creatures_in_combat)

