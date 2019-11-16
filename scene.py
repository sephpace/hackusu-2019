
from pygame import draw
from numpy import array, ndarray


class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.game_objects = []

        self.unit_ratio = 100

        screen_width = screen.get_width()
        screen_height = screen.get_height()
        if screen_width >= screen_height:
            self.screen_ratio = screen_height
            self.screen_offset = (screen_width - screen_height) // 2
            self.camera = Camera((0., 0.), (screen_width / screen_height) * self.unit_ratio, self.unit_ratio)
        else:
            self.screen_ratio = screen_width
            self.screen_offset = (screen_height - screen_width) // 2
            self.camera = Camera((0., 0.), self.unit_ratio, (screen_height / screen_width) * self.unit_ratio)

    def add(self, game_object): self.game_objects.append(game_object)

    def update(self):
        # Update the camera
        self.camera.update()

        # Update and render each object
        for obj in self.game_objects:
            obj.update()

            # Only render the object if it's on the screen
            if self.__is_visible(obj):
                self.__render(obj)

    def __render(self, obj):
        # Calculate vertex offsets from camera
        screen_pos = []
        for v in obj.get_vertices():
            offset = (v - self.camera.pos)
            screen_pos.append(self.coord_to_pixel(offset))

        # Draw the polygons
        draw.polygon(self.screen, obj.color, screen_pos)

    def __is_visible(self, obj):
        for x, y in obj.get_vertices():
            left, right, top, bottom = self.camera.get_edges()
            if left <= x <= right and top <= y <= bottom:
                return True
        return False

    def pixel_to_coord(self, pixel_pos):
        if self.screen.get_width() >= self.screen.get_height():
            return ((pixel_pos - array([self.screen_offset, 0])) / self.screen_ratio - 0.5) * self.unit_ratio
        else:
            return ((pixel_pos - array([0, self.screen_offset])) / self.screen_ratio - 0.5) * self.unit_ratio

    def coord_to_pixel(self, coord):
        if self.screen.get_width() >= self.screen.get_height():
            return (coord / self.unit_ratio + 0.5) * self.screen_ratio + array([self.screen_offset, 0.])
        else:
            return (coord / self.unit_ratio + 0.5) * self.screen_ratio + array([0., self.screen_offset])


class Camera:
    PAN_SPEED = 0.5

    def __init__(self, center_pos, width, height):
        if type(center_pos) == ndarray:
            self.pos = center_pos
        else:
            self.pos = array(center_pos)
        self.width = width
        self.height = height
        self.move_up = False
        self.move_left = False
        self.move_down = False
        self.move_right = False

    def __str__(self): return f'x={self.pos[0]} y={self.pos[1]} width={self.width} height={self.height}'

    def get_edges(self):
        left = self.pos[0] - self.width / 2
        right = self.pos[0] + self.width / 2
        top = self.pos[1] - self.height / 2
        bottom = self.pos[1] + self.height / 2
        return left, right, top, bottom

    def update(self):
        if self.move_up:
            self.pos[1] -= self.PAN_SPEED
        if self.move_left:
            self.pos[0] -= self.PAN_SPEED
        if self.move_down:
            self.pos[1] += self.PAN_SPEED
        if self.move_right:
            self.pos[0] += self.PAN_SPEED
