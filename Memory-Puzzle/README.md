# Memory Puzzle

![Python](https://img.shields.io/badge/Python-3.8%2B-1f6feb?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-tkinter-ff9900?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-2ea043?style=for-the-badge)

A GUI-based memory matching card game built with tkinter. Match pairs of emoji cards within the time limit to win!

**Highlights**

- 4x4 grid of cards (8 pairs)
- 60-second timer
- Interactive flip animation
- Visual feedback for matched pairs (green)
- Play Again button to restart
- Clean, modern UI with emoji icons

**Tech**

- Python 3.8+
- `tkinter` - GUI framework

**Run**

```bash
python memory_puzzle.py
```

**How to Play**

1. Click on a card to flip it and reveal an emoji
2. Click on a second card to try to find a match
3. If the emojis match, both cards stay revealed (green)
4. If they don't match, they flip back over
5. Match all 8 pairs before time runs out to win!

**Game Rules**

- You have 60 seconds to match all pairs
- Only two cards can be flipped at a time
- Once a pair is matched, it stays face-up

**Project Structure**

- `memory_puzzle.py` - Main game script
