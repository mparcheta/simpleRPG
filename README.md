## Project description

A simple RPG/dungeon crawler where the player assumes a role of a brave hero traversing the
underground dungeon in his quest for glory (and riches, of course).

## Project overview

1. The player fights through 10 encounters with random monsters in a dungeon
2. The player stats are:
    - Damage (DMG) (2-4)
    - Health points (HP) (15)
    - Mana (10)
    - Gold (0)
3. In each fight player takes turns deciding their action:
    - Attack for their DMG
    - Block the next enemy attack, avoiding their damage, but be unable to block next turn
    - Use healing to regenerate 5 HP (costs 6 mana, mana replenishes 1 point per turn)
4. Each turn the player knows what is the enemy's intent (chosen randomly) - either:
    - Attack
    - Block, reducing the player's damage by 1-3
5. The player's action is always processed before the enemy
6. There will be a couple of different monsters with different stats:
    - Goblin (10/2) (HP/DMG)
    - Skeleton (15/3)
    - Wolf (7/5)
    - Orc (20/4)
7. The monsters will drop a random amount of gold after defeating them (10-100)

## Implementation

The project is supposed to be written using OOP. Some of the game core logic is already
handled, but there is still a lot more to be implemented, like handling user input,
showing character stats and implementing actual monsters. After we deal with the basic scenario
we will probably want to add new features (:
