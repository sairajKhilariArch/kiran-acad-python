# Dictionary

A **dictionary** in Python is a collection of comma-separated key-value pairs enclosed within curly braces `{}`. It is an ordered, mutable, and indexed data structure that does not allow duplicate keys. From Python 3.7 onward, dictionaries maintain insertion order.

## Syntax and Structure

Dictionaries are defined using curly braces `{}` with key-value pairs separated by colons `:` and pairs separated by commas.
For example:

```python
var = {k1: v1, k2: v2, k3: v3}
```

A practical example is:

```python
square = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(type(square))  # <class 'dict'>
```

Keys must be unique and immutable
(e.g., strings, integers, or tuples), while values can be any data type and may be duplicated.

## Key Characteristics

- **Uniqueness of Keys**: Each key must be unique. If a duplicate key is used, the last value assigned to that key will overwrite the previous one.

- **Immutability of Keys**: Keys must be of an immutable type such as strings, integers, or tuples. Mutable types like lists cannot be used as keys..

- **Mutability of Dictionary**: The dictionary itself is mutable—meaning you can add, modify, or remove key-value pairs after creation.

For instance:

```python
numbers = {1: 1, 2: 4, 3: 6, 4: 16, 5: 25, 3: 9}
print(numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Here, the key `3` appears twice, but only the last value `9` is retained.

## Dictionary Methods

Python provides several built-in methods for manipulating dictionaries:


| Method | Description |
| :-- | :-- |
| `clear()` | Removes all elements from the dictionary  |
| `copy()` | Returns a shallow copy of the dictionary |
| `fromkeys(keys, value)` | Creates a new dictionary with specified keys and value  |
| `get(key, default)` | Returns the value for the key, or default if key not found  |
| `items()` | Returns a view of key-value pairs as tuples  |
| `keys()` | Returns a view of all keys  |
| `pop(key, default)` | Removes and returns the value for the specified key  |
| `popitem()` | Removes and returns the last inserted key-value pair  |
| `setdefault(key, default)` | Returns value if key exists, else inserts key with default value  |
| `update(dict)` | Updates the dictionary with key-value pairs from another dictionary  |
| `values()` | Returns a view of all values  |

These methods allow efficient access, modification, and traversal of dictionary data. For example, `items()` enables iterating over both keys and values simultaneously.





