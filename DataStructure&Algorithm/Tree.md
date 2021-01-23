# Tree
## depth
If "p" is a node of a tree, the depth of p is the number of its ancestors,excluding itself.
```python
def depth(self,p):
    if self.is_root(p):
        return 0
    return 1+self.depth(self.parent(p)) 
```
## height
The max depth in this tree.   
Two ways to calculate.
```python
# O(n**2)
def height(self,p):
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
# O(n) Pass the root node into the function below.
def height2(self,p):
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self.height2(c) for c in self.children(p))

# But users are not supposed to pass parameters when calculate the height,so.
def height(p=None):
    if not p:
        p = self.root()
    return self._height2(p)
```
# Binary Tree
+ Every node has two child nodes which are named left child and right child.
+ Left before right.

## complete binary tree(Full binary tree)
Every node except the root and leaves, has two child nodes.


# Traverse
Time complexity: O(n)

## preorder

```python
def preorder(T,p):
    # "visit" action for the current node.
    for child in T.children(p):
        preorder(T,child)
```

## postorder
```python
def postorder(T,p):
    for child in T.children(p):
        postorder(T,child)
    # "visit" action for the current node.
```
## breadth first
Commonly used in games, traverse the tree layer by layer.
```python
def breadthfirst(T):
    Q = queue()
    # Make T contain the root node.
    while not Q.empty:
        p = Q.dequeue()
        # "visit" action for the current node.
        for child in T.children(p):
            Q.enqueue(child)
```
## inorder
```python
def inorder(p):
    if p has a left child:
        inorder(p)
    # "Visit" action for the current node.
    if p has a right child:
        inorder(p)
```
