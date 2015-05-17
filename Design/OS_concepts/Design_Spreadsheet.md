#### Design Spreadsheet
##### Requirements:
* Store a value in a given cell (identified by it’s coordination (x, y)).
* Retrieve the value from a given cell.
* Remove a given cell.
* *Support expressions/functions in cells.

##### Ask for clarifications:
* What kinds of values can be stored in cells?
    * numbers (double), strings, etc
* Hint: your design should be extendable.
* 注意的问题：每一个数字，可能存储在任意一个二维的位置

##### Level 1
* Classes: Sheet, Cell
    * A sheet has many cells.
* How a sheet organize cells?
    * Requirements:
      * two-dimensional
      * size can grow indefinitely
      * very likely to be sparse
    * For one-dimensional data: Cell[]
      * support dynamic growing: ArrayList<Cell>
      * support sparse storage: HashMap<int, Cell>
    * For two-dimensional data: Cell[][]
      * support dynamic growing: ArrayList<ArrayList<Cell>>
      * support sparse storage: HashMap<int, HashMap<int, Cell>>

```python
#! /user/bin/python

# mMap structure: 
# {x1 : {y1 : Cell1}, x2: {y2: Cell2}}

class Sheet:
    def __init__(self):
        self.mMap = dict()

    def get_cell(self, x, y):
        if self.mMap.has_key(x):
            return self.mMap.get(x).get(y)
        else:
            return None

    def put_cell(self, x, y, cell):
        if self.mMap.has_key(x):
            imap = self.mMap.get(x)
            imap[y] = cell
        else:
            self.mMap[x] = {y:cell}
        return self.mMap[x][y]
    
    def remove_cell(self, x, y):
        if self.mMap.has_key(x):
            imap = mMap.get(x)
            del imap[y]
        else:
            return None

class Cell:
    def __init__(self, value):
        self.value = value

if __name__ == '__main__':
    s = Sheet()
    c1 = Cell(3.14)
    c2 = Cell('Hello World!')
    print s.put_cell(1, 1, c1).value
    print s.put_cell(2, 3, c2).value
    c = s.get_cell(1,1)
    print "c: ", c.value
```

##### Design Choice 1
* Immutable vs. mutable.
      * Cell is designed to be immutable (final value, no setters).
         * When we want to change the value of a cell from 2.2 to 2.3, we need to create a new cell and put it into the sheet.
         * Partly because: even if we provide NumberCell.setValue(double), how to change from 2.2 to “s.3”?
* Immutable classes:
      * Easier to reason the object state (won’t get into inconsistent state), inherent thread safety, etc.
      * Suitable for simple “value” types: Integer, String, Double, Color, etc.
*  Mutable classes:
      * Cheaper to mutate (No need to create a new object and copy unchanged fields).
      * Suitable for large/complex types: Car (speed, fuel), Game character (speed, life), Sheet
* More on immutable vs. mutable
* http://www.ibm.com/developerworks/java/library/j-jtp02183/index.html
* 在写一个class的时候，一般会注释thread-safy and author 

##### Design Choice:
* Object Oriented Programming: Encapsulation(封装), Abstruction(抽象), Inheritance(继承), Polymorphism(多态)
* 

