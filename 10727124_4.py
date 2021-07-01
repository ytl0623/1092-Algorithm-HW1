import sys
import math
import random

class Node:

  def __init__( self, val, parent=None ):
    self.vals = [val]
    self.parent = parent
    self.children = []

  def Insert( self, val ):
    self.vals.append(val)
    self.vals.sort()


class two34tree:

  def __init__( self, val ):
    self.root = Node( val )


  def Display(self):
    print( "2-3-4 Tree (Preorder):" )
    self.Preorder(self.root)
    print('\n')
    print( "2-3-4 Tree (Postorder):" )
    self.Postorder(self.root)
    print('\n')

  def Preorder(self, node):
    
    print(node.vals, end = '')

    if 0 < len(node.children):
      self.Preorder(node.children[0])
    if 1 < len(node.children):
      self.Preorder(node.children[1])
    if 2 < len(node.children):
      self.Preorder(node.children[2])
    if 3 < len(node.children):
      self.Preorder(node.children[3])

  def Postorder(self, node):
    

    if 0 < len(node.children):
      self.Postorder(node.children[0])
    if 1 < len(node.children):
      self.Postorder(node.children[1])
    if 2 < len(node.children):
      self.Postorder(node.children[2])
    if 3 < len(node.children):
      self.Postorder(node.children[3])

    print(node.vals, end = '')


  def Insert( self, val ):
    walk = self.root
    while len(walk.children) > 0:
      if len(walk.vals) == 1:
        if val < walk.vals[0] and val !=walk.vals[0]:
          walk = walk.children[0]
        elif val > walk.vals[0] and val !=walk.vals[0]:
          walk = walk.children[1]
        else:
          return 0

      elif len(walk.vals) == 2:
        if val < walk.vals[0] and val !=walk.vals[0]:
          walk = walk.children[0]
        elif val > walk.vals[1] and val !=walk.vals[0]:
          walk = walk.children[2]
        elif val < walk.vals[1] and val !=walk.vals[0]:
          walk = walk.children[1]
        else:
          return 0
		
      elif len(walk.vals) == 3:

        if val < walk.vals[0] and val !=walk.vals[0]:
          k = 1
        elif val < walk.vals[1] and val !=walk.vals[0]:
          k = 2
        elif val < walk.vals[2] and val !=walk.vals[0]:
          k = 3
        elif val > walk.vals[2] and val !=walk.vals[0]:
          k = 4
        else:
          return 0
        walk = self.Spilt( walk, k )

    if len(walk.vals) == 3:
      print(walk.vals)
      print(val)
      if val < walk.vals[0] and val !=walk.vals[0]:
        k = 1
      elif val < walk.vals[1] and val !=walk.vals[0]:
        k = 2
      elif val < walk.vals[2] and val !=walk.vals[0]:
        k = 3
      elif val > walk.vals[2] and val !=walk.vals[0]:
        k = 4
      else:
        if val == 6:
          print('123')
        return 0
		
      walk = self.Spilt( walk, k )
      walk.Insert(val)
    else:
      for x in walk.vals:
        if x == val:
          return 0
      walk.Insert(val)

  def Spilt( self, node, k ):
    if node.parent == None:
      if len(node.children) == 0:
        node.children.append( Node(node.vals[0], node) )
        node.children.append( Node(node.vals[2], node) )
        node.vals.pop(0)
        node.vals.pop(1)
        node1 = node.children[0]
        node2 = node.children[1]
      elif len(node.children) == 4:
        self.root = Node(node.vals[1])
        node1 = Node(node.vals[0], self.root)
        node2 = Node(node.vals[2], self.root)
        node.children[0].parent = node1
        node.children[1].parent = node1
        node.children[2].parent = node2
        node.children[3].parent = node2
        node1.children.append( node.children[0] )
        node1.children.append( node.children[1] )
        node2.children.append( node.children[2] )
        node2.children.append( node.children[3] )
        self.root.children.append( node1 )
        self.root.children.append( node2 )
    else:
      node1 = Node(node.vals[0], node.parent)
      node2 = Node(node.vals[2], node.parent)
      if len(node.children) == 0:
        if len(node.parent.vals) == 1:
          node.parent.Insert(node.vals[1])
          if node == node.parent.children[0]:
            node.parent.children.pop(0)
            node.parent.children.insert(0, node1)
            node.parent.children.insert(1, node2)
          elif node == node.parent.children[1]:
            node.parent.children.pop(1)
            node.parent.children.append(node1)
            node.parent.children.append(node2)
        elif len(node.parent.vals) == 2:
          node.parent.Insert(node.vals[1])
          if node == node.parent.children[0]:
            node.parent.children.pop(0)
            node.parent.children.insert(0, node1)
            node.parent.children.insert(1, node2)
          elif node == node.parent.children[1]:
            node.parent.children.pop(1)
            node.parent.children.insert(1, node1)
            node.parent.children.insert(2, node2)
          else:
            node.parent.children.pop(2)
            node.parent.children.append(node1)
            node.parent.children.append(node2)

      elif len(node.children) == 4:
        node.children[0].parent = node1
        node.children[1].parent = node1
        node.children[2].parent = node2
        node.children[3].parent = node2
        node1.children.append( node.children[0] )
        node1.children.append( node.children[1] )
        node2.children.append( node.children[2] )
        node2.children.append( node.children[3] )
        if len(node.parent.vals) == 1:
          node.parent.Insert(node.vals[1])
          if node == node.parent.children[0]:
            node.parent.children.pop(0)
            node.parent.children.insert(0, node1)
            node.parent.children.insert(1, node2)
          elif node == node.parent.children[1]:
            node.parent.children.pop(1)
            node.parent.children.append(node1)
            node.parent.children.append(node2)
        elif len(node.parent.vals) == 2:
          if node == node.parent.children[0]:
            node.parent.children.pop(0)
            node.parent.children.insert(0, node1)
            node.parent.children.insert(1, node2)
          elif node == node.parent.children[1]:
            node.parent.children.pop(1)
            node.parent.children.insert(1, node1)
            node.parent.children.insert(2, node2)
          else:
            node.parent.children.pop(2)
            node.parent.children.append(node1)
            node.parent.children.append(node2)

    if k == 1:
      return node1
    elif k == 2:
      return node1
    elif k == 3:
      return node2
    else:
      return node2

while 1 :
  value = input( "Please Enter Number : " )
  value = value.split()
  tree = two34tree(int(value[0]))

  i = 1
  while i < len(value):
    tree.Insert(int(value[i]))
    i = i + 1

  tree.Display()
  del tree