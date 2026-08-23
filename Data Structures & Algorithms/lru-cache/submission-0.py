class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head/tail sentinels simplify edge cases (empty list, single node, etc.)
        self.left = Node(0, 0)   # least recently used side
        self.right = Node(0, 0)  # most recently used side
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        """Unlink a node from the list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        """Insert a node right before 'right' (i.e., the most-recently-used end)."""
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)  # move to most-recently-used position
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])  # remove old node, we'll re-insert fresh

        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            # Evict the least recently used node (right after 'left' sentinel)
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]