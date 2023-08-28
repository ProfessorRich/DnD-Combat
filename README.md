# DnD 5th Edition Combat Simulator

This project is a Python script to automatically calculate Dungeons and Dragons (DnD) 5th edition combat. It simulates combat between creatures by automatically rolling dice, calculating damage, and determining the winner. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x

### Installing

Clone the repository to your local machine:

```
git clone  https://github.com/ProfessorRich/DnD-Combat.git
```

Change directory into the project folder.

Run the `combat.py` script:

```
python combat.py
```

## Usage

The `combat.py` script contains the `creature` class and the `dice_roll_required` class. 

### creature class

The `creature` class represents a creature participating in the combat. You need to create an instance of the `creature` class for each creature participating in the combat. The `creature` class takes the following parameters:

- `name`: Name of the creature.
- `max_hp`: Maximum hit points of the creature. When initialised the creature's hp is set to its max_hp.
- `ac`: Armor class of the creature.
- `attacks`: List of attacks of the creature. Each attack is a dictionary with the keys: 'attack', 'attack_modifier', 'damage', 'range'. 'damage' is an instance of the `dice_roll_required` class.
- `speed`: Speed of the creature.
- `str`, `dex`, `con`, `int`, `wis`, `cha`: Ability scores of the creature.
- `resistances`, `vulnerabilities`, `immunities`: Lists of resistances, vulnerabilities, and immunities of the creature.
- `size`: Size of the creature.
- `type`: Type of the creature.
- `alignment`: Alignment of the creature.
- `notes`: Additional notes about the creature.

### dice_roll_required class

The `dice_roll_required` class represents a dice roll. It can simulate any number of dice rolls with one dice of any number of sides and adds a bonus to the total. It takes the following parameters:

- `number_of_dice`: Number of dice to roll.
- `dice_sides`: Number of sides of the dice.
- `bonus`: Bonus to add to the dice roll.

### Example

Below is an example of how to use the `creature` and `dice_roll_required` classes:

```python
from combat import creature, dice_roll_required

test_1 = creature('Arnold the Anvil', 89, 21, [{'attack': 'Longsword', 'attack_modifier': 8, 'damage': dice_roll_required(1, 8, 8), 'range': 0}, {'attack': 'Longsword', 'attack_modifier': 8, 'damage': dice_roll_required(1, 8, 8), 'range': 0}], 30, 18, 14, 16, 12, 13, 13, [], [], [], 'M', 'Humanoid', 'LG', '')
test_2 = creature('Bolt', 100, 18, [{'attack': 'Morphed Limb', 'attack_modifier': 10, 'damage': dice_roll_required(2, 8, 2), 'range': 5},{'attack': 'Morphed Limb', 'attack_modifier': 10, 'damage': dice_roll_required(2, 8, 2), 'range': 5},{'attack': 'Morphed Limb', 'attack_modifier': 10, 'damage': dice_roll_required(2, 8, 2), 'range': 5}], 30, 18, 14, 18, 6, 12, 6, [], [], [], 'L', 'Demon', 'CE', '')
```

### Running the Combat

After creating the creatures, you can run the combat by calling the `run_combat_x_times` function:

```python
test_creatures_in_combat = [test_1, test_2]
run_combat_x_times(100, test_creatures_in_combat)
```

This will run the combat 100 times and print the number of times each creature won.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
