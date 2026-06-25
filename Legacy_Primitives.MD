# safe_get
**Purpose:** Protects your pipeline from missing keys, weird structures, and inconsistent JSON.
```python
def safe_get(data, path, default=None):
    """
    Safely navigate nested JSON using a list of keys.
    Example:
        safe_get(user, ["address", "city"])
    """
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
```
**Example:**
```python
user = {"address": {"city": "LA"}}
safe_get(user, ["address", "city"])  # "LA"
safe_get(user, ["address", "zip"], default=None)  # None
```

# flatten_json
**Purpose:** Turns tree‑shaped JSON into flat rows you can normalize, map, or export.
```python
def flatten_json(data, parent_key="", sep="."):
    """
    Flatten nested JSON (dicts only) into a single-level dict.
    Example:
        {"a": {"b": 1}} -> {"a.b": 1}
    """
    items = {}
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, sep=sep))
        else:
            items[new_key] = value

    return items
```
**Example:**
**Input:**
```python
{"user": {"name": "Alice", "address": {"city": "LA"}}}
```

**Output:**
```python
{"user.name": "Alice", "user.address.city": "LA"}
```

# normalize_list_of_dicts
**Purpose:** Makes every record have the same fields — essential for CSV, SQL, and clean JSON output. 
```python
def normalize_list_of_dicts(records, fill=None):
    """
    Normalize a list of dicts so all dicts share the same keys.
    Ensures consistent schema for JSON→JSON, JSON→CSV, JSON→SQL.
    """
    # Collect all keys across all records
    all_keys = set()
    for rec in records:
        all_keys.update(rec.keys())

    # Normalize each record
    normalized = []
    for rec in records:
        row = {key: rec.get(key, fill) for key in all_keys}
        normalized.append(row)

    return normalized
```

**Example:**
**Input:**
```python
[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "city": "LA"}
]
```

**Output:**
```python
[
    {"name": "Alice", "age": 30, "city": None},
    {"name": "Bob", "age": None, "city": "LA"}
]
```

# extract_records
**Purpose:** Finds the “real” list of objects inside any nested JSON — the step before flattening or normalizing.
```python
def extract_records(data):
    """
    Extract the first list of dicts found anywhere inside a JSON structure.
    Works for wrapped, nested, or weird vendor JSON.
    """
    # Case 1: The JSON itself *is* the list
    if isinstance(data, list) and all(isinstance(x, dict) for x in data):
        return data

    # Case 2: The JSON is a dict containing lists or nested dicts
    if isinstance(data, dict):
        for value in data.values():
            # If value is the list of dicts → return it
            if isinstance(value, list) and all(isinstance(x, dict) for x in value):
                return value
            # If value is nested → recurse
            if isinstance(value, dict):
                result = extract_records(value)
                if result is not None:
                    return result

    # No records found
    return None
```

**Example:**
```python
{
  "meta": {},
  "payload": {
    "results": [
      {"id": 1},
      {"id": 2}
    ]
  }
}
```

# list-aware_flatten_json
**Purpose:** Flatten nested JSON including lists, lists of dicts, and mixed structure
```python
def flatten_json_list_aware(data, parent_key="", sep="."):
    """
    Flatten nested JSON including lists.
    Produces keys like:
        a.b[0].c
        items[2]
        user.address.city
    """
    items = {}

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.update(flatten_json_list_aware(value, new_key, sep=sep))

    elif isinstance(data, list):
        for index, value in enumerate(data):
            new_key = f"{parent_key}[{index}]"
            items.update(flatten_json_list_aware(value, new_key, sep=sep))

    else:
        items[parent_key] = data

    return items
```

**Example:**
**Input:**
```python
{
  "user": {
    "name": "Alice",
    "phones": [
      {"type": "mobile", "number": "123"},
      {"type": "home", "number": "456"}
    ]
  }
}
```

**Output:**
```python
{
  "user.name": "Alice",
  "user.phones[0].type": "mobile",
  "user.phones[0].number": "123",
  "user.phones[1].type": "home",
  "user.phones[1].number": "456"
}
```