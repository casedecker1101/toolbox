# Archetypes
+ Search 
    - Shape:
        [You're looking for something in a collection]
    - Signals:
        [Find the, Which One, Does This Exist, Return the first]
    - Patterns:
        [Linear search, filter, max/min, key functions]
    - Example:
        {Find the highest score -> max() with key}

+ Scan & Track
    - Shape:
        [Walk through data and track something as you go.]
    - Signals:
        [Keep track of, Find the longest, Count while scanning]
    - Patterns:
        [Best-so-far, accumulator, sliding window, two pointers]
    - Example:
        {Find the longest streak -> best-so-far}

+ Grouping
    - Shape:
        [Organize items by category]
    - Signals:
        [Group by, Bucket these, Organize by type]
    - Patterns: 
        [Dict-as-database, setdefault, Counter, defaultdict]
    - Example:
        {Group players by team -> dict of lists}

+ Transformation
    - Shape:
        [Turn one structure into another.]
    - Signals:
        [Convert this into, Transform each item, Map this to that]
    - Patterns:
        [map, list comprehension, zip, pipeline]
    - Example:
        {Turn list objects into list of names -> list comprehension}

+ Filtering
    - Shape:
        [Keep only the items that match a condition.]
    - Signals:
        [Only include, Remove anything that, return valid items]
    - Patterns:
        [predicate function, filter, list comprehension]
    - Example:
        {Get all active users -> [u for u in users if u.active]}

+ Counting & Frequency
    - Shape:
        [You need to know how often something appears.]
    - Signals:
        [How many times, Find duplicates, Count occurrences]
    - Patterns:
        [Counter, dict counting, set for uniqueness]
    - Example:
        {Find duplicates -> set + dict}

+ State Machine
    - Shape:
        [Your logic depends on what "state" you're in.]
    - Signals:
        [If this happens, then switch to, Depending on the previous step, workflow with stages]
    - Patterns:
        [state variable, if/elif chain, event loop]
    - Example:
        {Parsing text -> state machine lite}

+ Divide and Conquer
    - Shape:
        [Break the problem into smaller pieces.]
    - Signals:
        [Split this into parts, solve each piece, combine results]
    - Patterns:
        [recursion, partitioning, merge logic]
    - Example:
        {Sorting -> divide & conquer}

+ Caching/Memoization
    - Shape:
        [You're repeating expensive work.]
    - Signals:
        [This caulculation happens a lot, Optimize repeated calls, Avoid recomputing]
    - Patterns:
        [memo dict, LRU cache, dynamic programming]
    - Example:
        {Fibonacci -> memoization}
    
+ Validation
    - Shape:
        [Check if data meets rules.]
    - Signals:
        [Ensure this is valid, Reject if, Check constraints]
    - Patterns:
        [guard clauses, predicate functions, early returns]
    - Example:
        {Validate input -> guard clause}

+ Summary 
    - Search => Find something
    - Scan & Track => Track best, longest, highest
    - Grouping => Organize by category
    - Transformation => Convert structures
    - Filtering => Keep only what matches
    - Counting => Frequency, duplicates
    - State Machine => Multi-step logic
    - Divide & Conquer => Break into parts
    - Memoization => Avoid repeated work
    - Validation => ensure correctness