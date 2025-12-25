# CShot  
Competitive Two-Player Arcade Game

## Overview
CShot is a two-player competitive arcade game developed in Python, designed to demonstrate
object-oriented system design, real-time game logic, and persistent data management.

## Objective
The goals of this project are to:
- design a responsive real-time game loop for competitive play,
- implement a clean and extensible entity-based architecture,
- persist player performance and rankings across sessions.

## Approach
The system is built using:
- an object-oriented entity hierarchy to model players, projectiles, and game elements,
- real-time input handling, collision detection, and scoring logic,
- a relational database backend integrated through an ORM for reliable persistence.

Special attention is given to robustness in high-frequency updates and separation of
game logic from data management.

## Key Concepts
object-oriented design • real-time systems • game loop architecture •
collision handling • database persistence • leaderboard systems

## Project Structure
- `main.py`: game loop and application entry point  
- `entities.py`: core game entities and behaviors  
- `DbContext.py`: database session and persistence logic  
- additional modules for resources and utilities  

## How to Run
1. Install required dependencies  
2. Configure database connection if needed  
3. Run the game:
   ```bash
   python main.py
