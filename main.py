
import math


class Canvas(list[str, ...]):
    def __init__(self, width, height):
        super().__init__([" " * width for row in range(
            height)])

    def print(self):
        def create_row_headers(length: int):
            return "".join([str(i % 10) for i in range(length)])

        header = " " + create_row_headers(len(self[0]))
        print(header)
        for idx, row in enumerate(self):
            print(idx % 10, row, idx % 10, sep="")
        print(header)

    def draw_polygon(self, *points: tuple[int, int], closed: bool = True, line_char: str = "*"):
        def draw_line_segment(start: tuple[int, int], end: tuple[int, int], line_char: str = "*"):

            def replace_at_index(s: str, r: str, idx: int) -> str:

                return s[:idx] + r + s[idx + len(r):]

            x1, y1 = start
            x2, y2 = end

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            sx = 1 if x1 < x2 else -1
            sy = 1 if y1 < y2 else -1
            error = dx - dy

            while x1 != x2 or y1 != y2:
                self[y1] = replace_at_index(self[y1], line_char, x1)

                double_error = error * 2
                if double_error > -dy:
                    error -= dy
                    x1 += sx

                if double_error < dx:
                    error += dx
                    y1 += sy

            self[y2] = replace_at_index(self[y2], line_char, x2)

        start_points = points[:-1]
        end_points = points[1:]
        if closed:
            start_points += (points[-1],)
            end_points += (points[0],)

        for start_point, end_point in zip(start_points, end_points):
            draw_line_segment(start_point, end_point, line_char)

    def draw_line(self, start: tuple[int, int], end: tuple[int, int], line_char: str = "*"):
        self.draw_polygon(start, end, closed=False, line_char=line_char)

    def draw_rectangle(self, upper_left: tuple[int, int], lower_right: tuple[int, int],
                       line_char: str = "*"):
        x1, y1 = upper_left
        x2, y2 = lower_right

        self.draw_polygon(upper_left, (x2, y1), lower_right, (x1, y2), line_char=line_char)

    def draw_n_gon(self, center: tuple[int, int], radius: int, number_of_points: int, rotation: int = 0,
                   line_char: str = "*"):
        angles = range(rotation, 360 + rotation, 360 // number_of_points)

        points = []
        for angle in angles:
            angle_in_radians = math.radians(angle)
            x = center[0] + radius * math.cos(angle_in_radians)
            y = center[1] + radius * math.sin(angle_in_radians)
            points.append((round(x), round(y)))

        self.draw_polygon(*points, line_char=line_char)


# Usage
self = Canvas(100, 40)
self.draw_line((10, 4), (92, 19), "+")
self.draw_polygon((7, 12), (24, 29), (42, 15), (37, 32), (15, 35))
self.draw_rectangle((45, 2), (80, 27), line_char='#')
self.draw_n_gon((72, 25), 12, 20, 80, "-")

self.print()

###################################

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"({self.x}/{self.y})"

    def __repr__(self):
        return self.__str__()

class Shape:
    def __init__(self, *points):
        self.points = list(points)

    def __str__(self):
        return f"Shape {self.points}"

    def __repr__(self):
        return self.__str__()

# Usage
p1 = Point(2.3, 43.14)
p2 = Point(5.53, 2.5)
p3 = Point(12.2, 28.7)

s1 = Shape(p1, p2, p3)
s2 = Shape(p2)
s3 = Shape()


print(p1)
print([p1, p2, p3])
print(s1)
print(s2)
print(s3)
