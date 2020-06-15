class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        costs = [(0, src, K + 1)]
        stops = collections.defaultdict(dict)

        for start, end, price in flights:
            stops[start][end] = price

        while costs:
            cost, node, remaining_flights = heapq.heappop(costs)
            if node == dst:
                return cost

            if remaining_flights:
                for destination in stops[node]:
                    heapq.heappush(
                        costs, 
                        (cost + stops[node][destination], destination, remaining_flights - 1)
                    )

        return -1
