class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    # Recursion (70ms)
    def zigzagLevelOrder(self, root):
        res = []
        self.level_order(root, 0, res)
        return res
    
    def level_order(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0,root.val)
            self.level_order(root.left, level+1, res)
            self.level_order(root.right, level+1, res)
    
    # Iteration (55ms)
    def zigzagLevelOrder(self, root):
        queue = collections.deque([root])
        res = []
        while queue:
            r = []
            for _ in range(len(queue)):
                q = queue.popleft()
                if q:
                    r.append(q.val)
                    queue.append(q.left)
                    queue.append(q.right)
            r = r[::-1] if len(res) % 2 else r
            if r:
                res.append(r)
        return res
