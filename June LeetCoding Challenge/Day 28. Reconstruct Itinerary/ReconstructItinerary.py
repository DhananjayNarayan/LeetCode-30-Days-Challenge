class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # make dict
        def dfs(city):
            while len(graph[city]) > 0:
                dfs(graph[city].pop(0))
            res.insert(0, city)
        
        res = []
        graph = defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
            graph[frm].sort()
        
        dfs('JFK')
        return res
        
