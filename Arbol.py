from collections import defaultdict
from Node import Node


class Arbol:
    def __init__(self):
        self.root = None
        self.cross = []

    def add_recursive(self, node: Node, value):
        if self.root == None:
            self.root = Node(value)
        elif value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self.add_recursive(node.left, value)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self.add_recursive(node.right, value)

    def find_node(self, node: Node, valor_buscado):
        if node == None:
            return
        elif node.value == valor_buscado:
            return node
        if valor_buscado < node.value:
            return self.find_node(node.left, valor_buscado)
        else:
            return self.find_node(node.right, valor_buscado)

    def aggregate(self, value):
        self.add_recursive(self.root, value)

    def inorder(self):
        inorder = []

        def cross(node: Node):
            if node != None:
                cross(node.left)
                inorder.append(node.value)
                cross(node.right)

        cross(self.root)
        self.cross = inorder

    def preorder(self):
        preorder = []

        def cross(node: Node):
            if node != None:
                preorder.append(node.value)
                cross(node.left)
                cross(node.right)

        cross(self.root)
        self.cross = preorder

    def postorder(self):
        postorder = []

        def cross(node: Node):
            if node != None:
                cross(node.left)
                cross(node.right)
                postorder.append(node.value)

        cross(self.root)
        self.cross = postorder

    def amplitude(self):
        route = defaultdict(list)  # Crea el manejador de datos

        def dfs(node: Node, level):  # Funcion encargada de añadir los valores al manejador
            route[level].append(node.value)
            # LLamado recursivo por cada hijo
            if node.left != None:
                dfs(node.left, level + 1)
            if node.right != None:
                dfs(node.right, level + 1)

        dfs(self.root, 0)  # Primer llamado
        self.cross = [ans for k, ans in sorted(route.items())]
        return [ans for k, ans in sorted(route.items())]

