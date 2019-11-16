
from pygame import draw


class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.camera = Camera(0, 0, screen.get_width(), screen.get_height())
        self.game_objects = []

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
        for x, y in obj.get_vertices():
            offset = (x - self.camera.x, y - self.camera.y)
            screen_pos.append((self.screen.get_width() // 2 + offset[0], self.screen.get_height() // 2 + offset[1]))

        # Draw the polygons
        draw.polygon(self.screen, obj.color, screen_pos)

    def __is_visible(self, obj):
        for x, y in obj.get_vertices():
            left, right, top, bottom = self.camera.get_edges()
            if left <= x <= right and top <= y <= bottom:
                return True
            return False


class Camera:
    PAN_SPEED = 5

    def __init__(self, center_x, center_y, width, height):
        self.x = center_x
        self.y = center_y
        self.width = width
        self.height = height
        self.move_up = False
        self.move_left = False
        self.move_down = False
        self.move_right = False

    def get_edges(self):
        left = self.x - self.width // 2
        right = self.x + self.width // 2
        top = self.y - self.width // 2
        bottom = self.y + self.width // 2
        return left, right, top, bottom

    def update(self):
        if self.move_up:
            self.y -= self.PAN_SPEED
        if self.move_left:
            self.x -= self.PAN_SPEED
        if self.move_down:
            self.y += self.PAN_SPEED
        if self.move_right:
            self.x += self.PAN_SPEED
