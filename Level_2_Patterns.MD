# Toolkit Philosophy

+ 1. You don't reinvent patterns - collect them
+ 2. You don't memorize - recognize
    - See the shape of the problem
+ 3. You don't feel guilt - feel acceleration
    - Existing patters build mastery
+ 4. You don't build from scratch - assemble


---------- Code ----------


# Search and find maximum items/users/objects and creates a list within JSON files
max_joint_count = max(len(prize.get("laureates", [])) for prize in read_json["prizes"])

# Guard Clause Pattern - sharp pattern, short functions
# Clean, readable and free of nesting hell
if condition:
    do_work()

# Inverse
if not condition:
    return
do_work()

# Accumulator Pattern
# Building Restults over time
# Backbone of: Filtering, mapping, grouping, aggregating
result = []
for item in items:
    if condition(item):
        result.append(transform(item))

# Dictionary as a Mini-Database
# Fast lookup, grouping, counting mapping keys to values
groups = {}
for item in items:
    key = item.category
    groups.setdefault(key, []).append(item)

# State Machine Lite
# Parsing, workflows, multi-step logic, game loops, UI Interactions
state = "idle"
for event in events:
    if state == "idle" and event == "start":
        state = "running"
    elif state == "running" and event == "stop":
        state = "idle"

# Key Function Pattern
# sorting or select based on custom logic
# backbone: finding winner, ranking, ordering, prioritizing
winner = max(players, key=lambda p: p.score)
sorted_items = sorted(items, key=lambda x: x.date)

# Predicate Function Pattern
# clean and modular logic
def is_valid(x):
    return x > 0 and x % 2 == 0
valid_items = [x for x in items if is_valid(x)]

# Pipeline pattern
# Break a problem into steps
# Data processing, API, machine learning, ETL Pipelines, game loops

data = load()
cleaned = clean(data)
filtered = filter(cleaned)
result = compute(filtered)
save(result)

# Template Function Pattern
# Function handles structure, pass custom logic
def process(items, transform):
    return [transform(x) for x in items]
result = process(nums, lambda x: x * 2)

+ Guard Clause - Cleaner logic, fewer bugs
+ Accumulator - Build results step-by-step
+ Dict-as-DB - Fast lookup, grouping, counting
+ State Machine Lite - Multi-step workflows
+ Key Function - Custom sorting & selecting
+ Predicate Function - Clean filtering logic
+ Pipeline - Modular, readable architecture
+ Template Function - Reusable, flexible tools