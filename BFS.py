def BFS(self,start,goal):
        visited_checker =  set([])
        explored = []
        queue = []
        child_parent = {}
        queue.append(start)
        visited_checker.add(start.data)
        while queue:
            q = queue.pop(0) 
            for i in self.adjacentNodes[q]:
                if i.data not in visited_checker:
                    queue.append(i)
                    visited_checker.add(i.data)
                    explored.append(i.data)
                    child_parent[i.data] = q
                    if i == goal :
                        print(explored)
                        print("The shortest path followed by BFS from ",start.data,"to ",goal.data,"---->",self.short_path(child_parent,start,goal))
                        return len(self.short_path(child_parent,start,goal))
                         