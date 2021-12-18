import math
class Node:
  def __init__(self, val, parent):
    self.val = val
    self.parent = parent

    self.left_child = None
    self.right_child = None
  
  def get_rightmost(self):
    if self.right_child is None:
      return self
    else:
      return self.right_child.get_rightmost()

  def get_leftmost(self):
    if self.left_child is None:
      return self
    else:
      return self.left_child.get_leftmost()

  def get_parent_right(self):
    if self.left_child is None:
      return self.parent.get_parent_right()
    else:
      return self.left_child.get_rightmost()

  def get_parent_left(self):
    if self.right_child is None:
      return self.parent.get_parent_left()
    else:
      return self.right_child.get_leftmost()

  def split(self):
    if self.val is not None and self.val >= 10:
      left = int(self.val // 2)
      right = int(math.ceil(self.val / 2))
      self.val = None
      self.left_child = Node(left, self)
      self.right_child = Node(right, self)
      return True
    else:
      if self.left_child and self.left_child.split():
        return True
      elif self.right_child and self.right_child.split():
        return True
      else:
        return False

  def explode(self, depth):
    if self.val is not None:
      return
    
    if depth == 5:
      print(self)
      leftmost = self.parent.get_parent_left()
      rightmost = self.parent.get_parent_right()
      print(rightmost)
      print(leftmost)
      quit()

      if leftmost != self.left_child:
        leftmost.val += self.left_child.val
        self.left_child = None

      if rightmost!= self.right_child:
        rightmost.val += self.right_child.val
        self.right_child = None

      self.val = 0
    else:
      self.left_child.explode(depth + 1)
      self.right_child.explode(depth + 1)

  def __str__(self) -> str:
    if self.val:
      return str(self.val)
    else:
      return "[" + str(self.left_child) + "," + str(self.right_child) + "]"

  
class Tree:
  def __init__(self, array):
    self.root = Node(None, None)
    self.__fill_tree__(self.root, array)

  def explode(self):
    self.root.explode(1)
  
  def split(self):
    return self.root.split()

  def __fill_tree__(self, node, array):
    if isinstance(array[0], int):
      node.left_child = Node(array[0], node)
    else:
      node.left_child = Node(None, node)
      self.__fill_tree__(node.left_child, array[0])

    if isinstance(array[1], int):
      node.right_child = Node(array[1], node)
    else:
      node.right_child = Node(None, node)
      self.__fill_tree__(node.right_child, array[1])

  def __str__(self) -> str:
    return str(self.root)

if __name__ == "__main__":
  '''
  file = open('input.txt')
    assignment = []
    for line in file:
      l = json.loads(line)
      assignment.append(l)
  
  file.close()
  '''

  line = [[[[4,3],4],4],[7,[[8,4],9]]]
  line = [line, [1, 1]]
  tree = Tree(line)
  print(tree)
  tree.explode()
  print(tree)


