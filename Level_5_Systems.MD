# How programs scale
# Separation of Concerns - Backbone of scalable software
+ Idea: Each part of your program should do one job and do it well
    - Example:
        [One module loads data, another processes it, the final outputs results]
    
# Event loop/Game loop
+ Games, Simulations, Servers, Automation Scripts
    - Shape:
        {while running:
            handle_input()
            update_state()
            render_output()
        }
    
# Dependency Injection
# Allows for swapping parts without breaking the system.
+ Don't Hardcode, Pass them in. 
    - Creates flexible and testable code
    - Example: 
        - Instead of:
        {db = Database()
         service = UserService(db)
        }
        - Do:
        {def run(service):
            service.execute()
        }

# Configuration Layer
# Do not have magic numbers or hardcoded paths scattered everywhere
+ Centralize them:
    - Example:
        [CONFIG = { 
            "db_path": "data/users.db",
            "max_players": 10,
            "log_level": "debug"
        }]

# Data Flow Architecture
# Designing how information moves through the system.
# Choosing the correct flow is half the battle
+ Choose between:
    - Pipeline flow
        [input -> transform -> compute -> output]
    - Event-Driven flow
        [event happens -> handlers respond]
    - Request/Response flow
        [client asks -> server answers]
    - Stateful flow
        [system changes over tme -> state updates]

# Layered Architecture
# Each layer talks only to the one below it
# Maintains a clean and stable system
+ Layer 1 - Data
    - Files, databases, API
+ Layer 2 - Logic
    - Rules, calculations, decisions
+ Layer 3 - Interface
    - CLI, GUI, API endpoints

# Error Boundary
# Contain errors, rather than letting them explode
+ Example:
    - { try:
            risky_operation()
        except Exception as e:
            log(e)
            recover()
    }

# Summary
+ Separation of Concerns => Prevents tangled code
+ Event Loop    =>  Real-time systems
+ Dependency injection  => Flexible, testable design
+ Configuration Layer   => centralized settings
+ Data Flow Architecture    => Defines how info moves
+ layered Architecture      => Scalable structure
+ Error boundaries          => Stability resilience