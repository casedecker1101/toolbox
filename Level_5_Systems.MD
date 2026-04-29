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

# Data Flow Architecture
# Designing how information moves through the system.
+ Choose between:
    - Pipeline flow
        [input -> transform -> compute -> output]
    - Event-Driven flow
        [event happens -> handlers respond]
    - Request/Response flow
        [client asks -> server answers]
    - Stateful flow
        [system changes over tme -> state updates]

# Layered Archi
    