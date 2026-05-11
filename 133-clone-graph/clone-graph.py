from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        clones = {}

        # clone first node
        clones[node] = Node(node.val)

        queue = deque([node])

        while queue:

            current = queue.popleft()

            for neighbor in current.neighbors:

                # create clone if not visited
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # connect cloned neighbors
                clones[current].neighbors.append(clones[neighbor])

        return clones[node]