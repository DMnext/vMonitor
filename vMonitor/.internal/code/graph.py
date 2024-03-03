import random
from typing import List
import math
import time


class Graph:
    
    def __init__(self, graph_name):
            self.graphs: List[Graph] = []
            self.graphs.append(graph_name)
            self.graph_id = random.randint(0, 1000)
            self.graph = f"GRAPH[{graph_name}]<{self.graph_id}>**"
            self.graph_lines: List[Graph] = []
            self.graph_lines.append(self.graph)
            # print(self.graphs)

    def graph_creator(self, number:int, symbols: str = "+", last_symbol:str | None = None):
        if last_symbol is None:
            _symbols = symbols * number
            self.graph_lines.append(f"|{_symbols}")
        else:
            _symbols = symbols * (number - 1)
            self.graph_lines.append(f"|{_symbols}{last_symbol}")
        # print(self.graph_lines)
        return self.graph_lines

    def _start_graph(self, graph_name:str):
        self.graphs.append(graph_name)

    def stop_graph(graph_lines):
        self.graph_contents = "/n".join(graph_lines)

        return self.graph_contents


if __name__ == '__main__':
    base_speed = 21
    angle = 0
    a = 0

    for i in range(0, 1000):
        number = random.randint(0, 9)
        angle += math.pi / 180
        # style = colors[random.randint(0, len(colors) - 1)]
        sinus = int(base_speed + math.sin(angle) * 20)
        a += 1
        # print(sinus)
        graph_lines = Graph.graph_creator(self=Graph("graph1"), number=sinus, symbols=f"{number}")
        print(graph_lines[-1])
        time.sleep(0.1)
    # print(graph_lines)
