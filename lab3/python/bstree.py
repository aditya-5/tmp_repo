import config

class bstree:
    def __init__(self, value = None):
        self.verbose = config.verbose
        self.value = value
        self.left = None
        self.right = None
        
    def size(self):
        if(self.left != None):
            left_size = self.left.size()
        else:
            left_size = 0

        if(self.right != None):
            right_size =  self.right.size()
        else:
            right_size = 0

        return 1 + left_size + right_size
    
    def height(self):
        if(self.left != None):
            left_size = self.left.height()
        else:
            left_size = 0

        if(self.right != None):
            right_size = self.right.height()
        else:
            right_size = 0

        return 1 + max(left_size, right_size) 

    def tree(self):
        if hasattr(self, 'value') and hasattr(self, 'left') and hasattr(self, 'right'):
            return self.value != None and self.left != None and self.right != None

        
    def insert(self, value):
        # If current node has no value
        if not self.value:
            self.value = value
            return
        # If duplicate element
        if self.value == value:
            return
        # If needs to be inserted in left subtree
        if value < self.value:
            if self.left is None:
               self.left = bstree(value)
            else:
               self.left.insert(value)
        # If needs to be inserted in right subtree
        elif value > self.value:
           if self.right is None:
              self.right = bstree(value)
           else:
              self.right.insert(value)         
        
    def find(self, value):
        if value ==  self.value:
            return True
        if value < self.value:
            if self.left != None:
                return self.left.find(value)
            return False
        elif value > self.value :
            if self.right != None:
                return self.right.find(value)
            return False
        
    # You can update this if you want
    def print_set_recursive(self, depth):
        if (self.tree()):
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.value)
            self.left.print_set_recursive(depth + 1)
            self.right.print_set_recursive(depth + 1)
            
    # You can update this if you want
    def print_set(self):
        print("Tree:\n")
        self.print_set_recursive(0)
        
    def print_stats(self):
        print("Size of the tree : " + str (self.size()))
        print("Height of the tree : " + str (self.height()))
            
            
