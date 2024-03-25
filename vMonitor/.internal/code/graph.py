import random
from typing import List
import math
import time
import os


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

    def stop_graph(self):
        self.graph_contents = "/n".join(self.graph_lines)

        return self.graph_contents


def spawn_insect(line, w):
    line_with_insect1 = "🪳️"
    line_with_insect2 = "🪲️"
    line_with_insect3 = "🕷️"
    line_with_insect4 = "🪰️"
    insect = random.randint(0, 4)
    if insect == 1:
        insect_column = random.randint(0, w)
        print(f"{line * insect_column}{line_with_insect1}")
    elif insect == 2:
        insect_column = random.randint(0, w)
        print(f"{line * insect_column}{line_with_insect2}")
    elif insect == 3:
        insect_column = random.randint(0, w)
        print(f"{line * insect_column}{line_with_insect3}")
    elif insect == 4:
        insect_column = random.randint(0, w)
        print(f"{line * insect_column}{line_with_insect4}")
    else:
        print(line)



if __name__ == '__main__':
    base_speed = 21
    angle = 0
    a = 0
    number_of_insects = 10
    
    w, _ = os.get_terminal_size()
    
    line_with_insect1 = "🪳️"
    line_with_insect2 = "🪲️"
    line_with_insect3 = "🕷️"
    line_with_insect = "❗️⚠️"
    line = " "
    while True:
        try:
            if random.randint(0, number_of_insects) == number_of_insects:
                spawn_insect(line, w)
            else:
                print(line)
            time.sleep(0.1)
        except KeyboardInterrupt:
            spawn_insect(line, w)
                

    for i in range(0, 1000):
        number = random.randint(0, 9)
        angle += math.pi / 180
        # style = colors[random.randint(0, len(colors) - 1)]
        sinus = int(base_speed + math.sin(angle) * 20)
        a += 1
        # print(sinus)
        graph_lines = Graph.graph_creator(self=Graph("graph1"), number=sinus, symbols=f"")
        print(graph_lines[-1])
        time.sleep(0.1)
    # print(graph_lines)
    
# 🪳️
