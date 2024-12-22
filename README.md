# snakeproj

README

SNAKE GAME IN PYTHON

This repo contains a very simple version of the classic Snake game recreated in Python.

Input controls
- W - up
- A - left
- S - down
- D right

Game rules
- Eating food increases score and snake length
- Bumping into borders or one's own snake == game over


Requirements to run
- Python 3.x (Turtle library requires no external install as it's built in within python)


``` mermaid
graph TD
    A[Start Game] --> B{Game Running?}
    B -->|Yes| C[Player Movement Input]
    C --> D[Update Snake Position Accordingly]
    D --> E{Collision Detected?}
    E -->|Collision with Wall/Self| F[Game Over]
    E -->|Ate food| G[Increase Length & Score]
    G --> H[Update Game]
    H --> I[Keep Running]
    I --> B
    E -->|No| H
    B -->|No| F
``` 
