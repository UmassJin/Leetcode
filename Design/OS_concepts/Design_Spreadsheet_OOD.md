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

##### Polymorphism 
* Polymorphism: single interface, multiple types
      * ad-hoc polymorphism (function overloading, C++ template (partial) specialization)
         * 对于不同的类型有不同的behavior
         * difference types -> maybe different behavior, static resolution
         * e.g. int max(int, int), string max(string, string); hash<int>, hash<string>
      * parameterized polymorphism, generic programming (C++ templates, Java generics)
         * 不同的类型有相同的behavior 
         * different types -> same behavior, static resolution
         * e.g. ArrayList<V>, Object.hashcode().
      * Subtyping polymorphism, polymorphism
         * 不同的类型不同的behavior 
         * different types -> maybe different behavior, dynamic resolution--> python
         * Avoid using “instanceof” in Java (dynamic_cast<> in C++) (code smell, violate LSP)
            * “instanceof” means two subtypes have different interfaces -> deal with them separately.
            * python 里面是：isinstance()
         * *Subtyping vs. inheritance.

##### Level 2 (with expression)
* How to support the expressions ?
* What expressions are supported? +, -, *, / between numbers. SUM, MEAN
* 题目大意：


##### Level 2 - Algorithm
* Another cell type: ExpressionCell.
* Constructor takes a string as input: “($0$0 - $0$1) / $0$2”
* Parser takes a string and output an expression (array or tree)
      * 输入是一个string，输出是一个expression tree or array 
      
* Evaluator takes an expression and returns a value (or error).
      * This is itself a good OO design question. https://www.youtube.com/watch?v=4F72VULWFvc

* What if one cell is updated (by Sheet.put())?
      * Lazy calculation: do nothing on put(), evaluate expression on every get().
         * If there is no put() after last get(), we can directly use the old value. As long as there is a put() (no matter on
which cell), we need to re-evaluate.
         * If get() is more frequent than put(), many repetitive computations.
         * Cell $0$0 may be again an ExpressionCell. Since we don’t have the up-to-date cell value of it either, we need
to do ripple calculation.
      
      * Eager calculation: propagate value updates on put(), simply read values on get().
         * If put() is more frequent than get(), many transparent computations.
         * In actual spreadsheet software, almost every update is visible -> eager calculation is necessary.
      * Like news feed, but more tricky: I want to get all my friends’ friends’ friends’ … update.
      * 这里我们选择用 Eager calculation
* The dependency graph should be acyclic.

#### Eager Calculation - Determine update order
* In addition to the expression (from where we can get a list of dependent positions), we also need to store the current value and a list of (directly) affecting positions for every cell.
* 改了现在cell的数值，不仅要存储dependent数值，还要存储可能影响到的其它cell的数值，例如，输入的“($0$0 - $0$1) / $0$2”，我们需要记录dependent ((0,0), (0,1), (0,2))，还要记录这个写入的cell的x, y是什么，哪些是depend这个cell的数值，都要改变
* If we use the BFS, which will have the issue, 
      * we need to call “reevaluate neighbor (directly affecting) cells” for every children, even for visited nodes.
      * e.g. 1->2, 1->3, 3->2, we need to update 1, 2, 3, 2
* To avoid the need to update updated node, update in topological sorted order.
      * How to do topological sort? O(N)
         * Iteratively find node with zero in-degree (not suitable, since we are not given a adjacency list of all reachable nodes)
         * DFS, reverse the “finish” order.
         * 这里我们要找的是从这个节点出发，所能到的所有的节点，而不用去找图中所有的节点

#### Eager calculation - Cycle Detection  
* After the topological sort, we get a list of all reachable positions from the current position. We should check if this list intersects it’s dependent position list (in the expression, if it is an ExpressionCell). If yes, cycle is found, we should reject this update.
* Specifically, if it depends on itself, we should also reject the update.

#### Eager calculation - Update
* What need to be updated? (cell had better be mutable. )
      * The current cell’s expression, value (affecting list remains unchanged. )
      * If the old cell is an ExpressionCell, this position should be removed from the old expression’s dependent cells’ affecting lists.
         *  *To effectively find the one to be removed, we can use HashMap for the affecting list.
      * If the new cell is an ExpressionCell, this position should be added to the new expression’s dependent cells’ affecting lists.   
      * All reachable cells’ value. (expression and affecting list remain unchanged. )
* Note: adding to/removing from affecting lists may involve creating and removing a “default value” cell.
      * Like reference counting. But when a cell is referenced by no one, we should make sure that value is “default” before removing it.
      * 例如在exel里面加一个expression cell, 这个expression cell是加上第一行的前10个数值，这里就返回一个default数值



```python
#! /user/bin/python

# mMap structure: 
# {x1 : {y1 : Cell1}, x2: {y2: Cell2}}

class Sheet(object):
    def __init__(self):
        self.mMap = dict()

    def get_cell(self, x, y):
        if self.mMap.has_key(x):
            return self.mMap.get(x).get(y)
        else:
            return Cell() # if can not find, return the default cell

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

class Cell(object):
    def __init__(self, sheet, x, y, value):
        self.mSheet = sheet
        self.mPosx = x
        self.mPosy = y
        self.value = value
        self.moutEdges = [] # affecting list 

    def getDoubleValue(self ): # if input is not integer, will return error
        try:

        except:
class ExpressionCell(object):
    def __init__(self, sheet, x, y, expression_str):
        self.mSheet = sheet
        self.mPosx = x
        self.mPosy = y
        self.mExpression = Parser.parse(s, expression_str)
        # mInEdges 表示dependent是什么，如果例子中是(0,1)
        # mOutEdges 表示这个cell影响谁
        self.mInEdges = OutEdgeExtractor.extract(mExpression)

        self.updateCurrentValue()
        self.reachableCell  = Graph.topologicalSort()

        # 首先得到原来存在该位置的cell
        self.oldCell = self.mSheet.get_cell(x, y)
        # 其次将新的cell插入到位置(x, y)中
        self.newCell = self.mSheet.put_cell(x, y, mExpression)

        # 对于每一个旧的cell中，我们把旧的节点从原来的dependency的affect list中删除
        for dependentCell in self.oldCell.mInEdges:
            dependentCell.mOutEdges.remove(self.oldCell)

        # 对于每一个新的cell中，我们把新的节点加到每一个dependency的affect list中
        for dependentCell in self.mInEdges:
            dependentCell.mOutEdges.add(self.newCell)

        # 然后我们update这个节点影响到的其它节点的数值
        # 例如old cell(1,2) has dependency ((1,1) (0,1)),同时又是cell(3,2)的dependency
        # 新的cell(1,2)有新的dependency((2,2))
        # 我们就先update (1,1),(0,1)的affecting list, mOutEdges, 去掉(1,2) 
        # 再更新的dependency (2,2),加到它的affecting list里面
        # 再根据从topology中得到的这个cell会影响到谁，例如这里是影响cell(3,2),依次update
        for affectingCells in self.reachableCell:
            affectingCells.updateCurrentValue()

        self.mOutEdges = self.oldCell.mOutEdges

    def updateCurrentValue(self):
        self.mCurrectValue = self.mExpression.value()


class ExpressionNode():
    def __init__(self, sheet):
        self.mSheet = sheet

    def multiplynode(self, op1, op2):
        mop1 = op1
        mop2 = op2
        return mop1.val * mop2.val

    def expressionnode(self, x, y):
        return self.get_cell(x, y)

if __name__ == '__main__':
    s = Sheet()
    c1 = Cell(s, 0, 1, 5)
    c2 = ExpressionCell(s, 0, 2, "$0$1 * 2")
    d = s.get_cell(0,2)
    print "d: ", d.value

```
