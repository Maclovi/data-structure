class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def __eq__(self, other):
        return {self._v1, self._v2} == {other.v1, other.v2}

    def __repr__(self):
        return f"Link(v1={self._v1}, v2={self._v2}, d={self._dist})"


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if link not in self._links:
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            self._links.append(link)
            link.v1.links.append(link)
            link.v2.links.append(link)

    @classmethod
    def find_min_node(cls, costs):
        result = None
        min_num = float("inf")
        for k, v in costs.items():
            if v[-1] and v[0] < min_num:
                min_num = v[0]
                result = k

        return result

    @classmethod
    def get_links_and_vertex(cls, stop_v, costs):
        lst_vertex = [stop_v]
        lst_links = []

        top = costs[stop_v]
        while top[1]:
            link = top[2]
            vertex = top[1]

            lst_links.append(link)
            lst_vertex = [vertex] + lst_vertex
            top = costs[vertex]

        return lst_vertex, lst_links

    def find_path(self, start_v, stop_v):    # algorithm dijkstra
        costs = {k: [float("inf"), None, None, True] for k in self._vertex}
        costs[start_v][0] = 0

        node = start_v
        while node:
            cost = costs[node][0]
            neighbors = node.links
            for link in neighbors:
                new_cost = cost + link.dist
                vertex = link.v2 if link.v2 != node else link.v1

                if new_cost < costs[vertex][0]:
                    costs[vertex][0] = new_cost
                    costs[vertex][1] = node
                    costs[vertex][2] = link

            costs[node][-1] = False
            node = self.find_min_node(costs)

        result = self.get_links_and_vertex(stop_v, costs)
        return result


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    pass
