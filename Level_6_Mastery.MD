# Abstraction Mental Model
+ Abstraction is the art of hiding complexity behind a simple interface
    - Stop Thinking: "How does this work internally?"
    - Start Thinking: "What does this do and what do I need from it?"
    - Example: 
        [How sort() works is irrelevant, only that it sorts.]

# Layer of Indirection
# The system now depends on this block, not the database.
+ Secret weapon of senior engineers.
    - If it's too tangled, messy, rigid - add a layer.
    - Example: 
        [Instead of calling a database everywhere directly]
            (You create)
            {class UserRepository:
                def get_user(self, id):
                    ...
            }

# Inversion of Control
+ Instead of code controlling everything, the system calls you
    - How frameworks, game engines and UI systems work.
    - Example:
        [You don't call the event loop, event loop calls your functions.]

# Composition Over Inheritance
+ Instead of building deep class hierarchies
    - Build small pieces that snap together
    - Example:
        - [Instead of: Animal -> Mammal -> Dog -> GuardDog]
        - [Do:  class GuardBehavior:
                    ...
                class Dog:
                    def __init__(self, behavior):
                        self.behavior = behavior
          ]

# Data-Oriented Thinking
+ Beginners think in terms of code.
    - Experts think in terms of data.
+ The question becomes:
    - "What shape should the data be so the code becomes simple?"
    - Shape determine code complexity and completion time.

# Constraints First
+ Prior to writing:
    - Ask: 
        [ What are the: limits, rules, can't happen, must always happen?]
    - Prevents entire categories of bugs before they exist.

# Simplify Until It's Boring
# Hallmark of Mastery - Making the complex feel inevitable
+ If a solution feels clever, elegant, impressive...it's probably wrong.
+ Best solutions feel:
    - Obvious, boring, simple, stable

# Fail Fast, Recover Gracefully
+ Don't try to prevent every error.
+ Try to detect them early and handle them cleanly.
+ Builds systems that don't collapse under pressure.

# Summary
+ Abstraction   =>  Hide complexity, focus on intent
+ Indirection   =>  Flexibility and modularity
+ Inversion of Control  =>  Framework-level thinking
+ Composition   =>  Lego-style system design
+ Data-Oriented Thinking    =>  Simpler code through better data
+ Constraints First =>  Bug prevention
+ Cimplify Until Boring =>  Stability and clarity
+ Fail Fast     =>  Resilience