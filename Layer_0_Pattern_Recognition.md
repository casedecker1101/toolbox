# Linear Search
+ Small or unsorted List
     
    ```python
    for item in items:
        if item == target:
        return True
    ```

+ Filter 
    - All Matches
    
    ```python
    matches = [x for x in items if condition (x)]
    ```

+ max/min 
    - Looking for winner/loser
    ```python
    winner = max(items, key = lambda x: x.score)
    loser = min(items, key = lambda x: x.score)
    ```

+ Has this appeared before - Use a Set
    - Fastest way to detect duplicates
    
    ```python
        seen = set()
          for x in items:
            if x in seen:
                return True
            seen.add(x)
    ```

+ Count with dict
    
    ```python
    from collections import Counter 
    counts = Counter(items)
    ```

+ Transformation
    - Turn this into that
+ Map 
    - Apply a function to every element
        
        ```python
        squares = [x * x for x in nums]
        ```
+ Zip
    - Combine lists
        
        ```python
        pairs = list(zip(names, scores))
        ```

+ Looping Patterns
    - Walk through data cleanly
+ Enumerate
    - When index + value needed
        
        ```python
        for i, value in enumerate(items):
        ```

+ Early exit
    - Early Stop
        
        ```python
        for x in items:
            if condition(x):
                break
        ```

+ Problem solving patterns
    - How do I structure logic
+ Best-so-far, winners, max/min, comparisons
        
       best = None
          for x in items:
              if best is None or x > best:
                best = x
    

+ Two pointers
    - Sorted lists, ranges, windows
    
    ```python
        left, right = 0, len(nums) - 1
    ```

+ Sliding window
    - Subarrays, substrings, ranges
    
    ```python
        window_sum = 0
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]
    ```