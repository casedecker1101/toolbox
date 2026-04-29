# Module Pattern
+ Module is just a file or component with a single responsibility.
    - Signal:
        [This part feels separate, This logic is its own thing, this could b reused later]
    - Example:
        [players.py, game_logic.py, utils.py, database.py]

# Interface
+ Interface is the contract between parts of your system.
    - You don't need formal interfaces, just clear function boundaries
    - Example:
        { def load_players():
          def compute_winner(players):
          def save_results(winner):
        }

# Flow - Programs bloodstream
+ Order in which things happen
    - Build a pipeline
        [load -> clean -> compute -> output]
    - Game
        [input -> update -> render -> repeat]

# Data Shape - Decide what your world looks like
+ One of the most important architectural decisions.
    - Choose the shape of your data:
        [ list of dicts, list of objects, dict of lists, nested structures, classes, tuples]
    - Example:
        [players = {
            "name": "Society",
            "score": 42,
            "active": True
        }]

        [class Player:
            def __init__(self, name, score):
                self.name = name
                self.score = score
        ]

# Summary 
+ Modules => Break the system into meaningful parts
+ Interfaces => Define how parts communicate
+ Flow => Establish the program's heartbeat
+ Data Shapes => Decide the structure of your world
