# Cricket Tournament Simulation

This is a Python program that simulates a cricket tournament with advanced features. The program allows you to simulate cricket matches between teams, considering player stats, field conditions, and various match events.

## Project Structure

The project structure is organized as follows:

```cricket_tournament/
├── main.py
├── models/
│ ├── player.py
│ ├── team.py
│ ├── field.py
│ ├── umpire.py
│ ├── commentator.py
│ └── match.py
├── utils/
│ └── helpers.py
└── README.md
```


- `main.py`: The entry point of the program where the match simulation is initiated.
- `models/`: Contains the different classes representing the various components of the cricket simulation.
- `utils/`: Contains helper functions for setting up the game and playing the match.
- `README.md`: This file.

## Features

- Simulates cricket matches with two innings per match.
- Includes player statistics such as batting, bowling, fielding, running, and experience.
- Allows selection of team captains and batting order.
- Considers field conditions, including size, fan ratio, pitch conditions, and home advantage.
- Tracks scores, wickets, and overs in real-time during the match.
- Provides commentary for each ball and over.

## Usage

To run the cricket tournament simulation, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository or download the code files.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the simulation:

   ```bash
   python main.py

5. The program will simulate the cricket match and display the ball-by-ball commentary, scores, wickets, and match results.

# Customization
Feel free to customize the program by modifying the player statistics, field conditions, and other parameters according to your preferences. The code is designed to be extensible, allowing you to add additional features or enhance existing functionality as needed.

# Credits
This cricket tournament simulation program was created by [Anusha Navada]. It utilizes the principles of object-oriented programming and randomization techniques to mimic real-world cricket matches.