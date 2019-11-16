
import math
import sys

from . import save_model


def generate_circle(vertex_count):
    circle = []
    interval = 2 * math.pi / vertex_count
    for i in range(vertex_count):
        circle.append([math.cos(i * interval), math.sin(i * interval)])
    return circle


if __name__ == '__main__':
    vertex_count = int(sys.argv[1])
    file_path = sys.argv[2]
    save_model(generate_circle(vertex_count), file_path)
