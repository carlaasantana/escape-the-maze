# Escape the Maze

This is a game project developed using **Pygame** to teach programming concepts such as collision detection, movement, and game logic. The project is part of a game mentorship server.

---

## Description
The player must escape a maze filled with obstacles and enemies. Using keyboard controls, the player must reach the blue area (the exit) without losing all lives.

---

## Concepts Covered
- Creating windows with Pygame
- Sprites and Groups
- Collision detection (`colliderect`)
- Keyboard-controlled movement
- Enemy behavior and interaction
- Heads-Up Display (HUD) for player life
- Victory and defeat conditions

---

## How to Play

1. Run the file `main.py`
2. Use the arrow keys to move the player
3. Avoid red enemies
4. Reach the blue exit area while maintaining at least one life
5. Collision with enemies reduces life by 1
6. The game ends when:
   - You reach the exit (victory)
   - Your life reaches zero (game over)

---

## Controls
| Key         | Action          |
|-------------|-----------------|
| ← ↑ ↓ →    | Move player     |
| ESC         | Quit game       |

---

## Code Structure
- `Jogador` (Player) → controllable sprite
- `Inimigo` (Enemy) → moving sprites that cause damage
- `Parede` (Wall) → collision blocks player movement
- `Saida` (Exit) → blue area representing game completion

---

## Requirements
- Python 3.10+
- Pygame (`pip install pygame`)

---

## Suggested Enhancements for Students
- Add a countdown timer
- Implement multiple levels with unique maps
- Include temporary power-ups
- Add background music and sound effects
- Create animations for win and lose conditions

---

## Created by
**Carla Aparecida Santana**  
Game Mentorship | Computer Science
