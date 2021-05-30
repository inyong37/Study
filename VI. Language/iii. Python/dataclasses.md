# dataclasses - Data Classes | [Docs (3.7.10)] | [lib/dataclasses.py](https://github.com/python/cpython/blob/3.7/Lib/dataclasses.py)
This module provides a decorator and functions for automatically adding generated speical methods such as __init__() and __repr__() to user-defined classes. It was originally described in PEP 557.

The member variables to use in these generated methods are defined using PEP 526 type annotations.

For example this code:
```Python
from dataclasses import dataclass

@dataclass
class InventoryItem:
  '''Class for keeping track of an item in inventory.'''
  name: str
  unit_price: float
  quantity_on_hand: int = 0
  
  def total_cost(self) -> float:
    return self.unit_price * self.quantity_on_hand
```
Will add, among other things, a __init__() that looks like:
```Python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int=0):
  self.name = name
  self.unit_price = unit_price
  self.quantity_on_hand = quantity_on_hand
```
Note that this method is anutomatically added to the class: it is not directly specified in the InventoryItem definition shown above.
