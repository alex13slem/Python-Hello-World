"""
	Цель урока: создать игру в жанре “гонки” с цикличным движением и добавлением текстуры фона.
	+ вспомнить команды прошлого урока;
	+ создать заготовку проекта;
	+ добавить фон;
	+ добавить машину;
	+ настроить управление машинкой;
	+ настроить повороты при движении машины;
	+ добавить препятствие;
	+ зациклить движение препятствия;
	+ добавить случайность в движение препятствия;
	+ настроить столкновение спрайтов;
	+ отрисовать надпись о конце игры;
	+ сделать выводы по уроку;
	+ получить домашнее задание.
"""
import random
import arcade

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Гонки"

CAR_ANGLE = 20
CAR_SPEED = 5
WALL_SPEED = 5


class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x

        # ДЗ 3
        if self.left < 56:
            self.left = 56
        if self.right > SCREEN_WIDTH - 56:
            self.right = SCREEN_WIDTH - 56

    # ДЗ 3


class Wall(arcade.Sprite):
    def update(self):
        self.center_y -= self.change_y
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT + random.randint(0, SCREEN_HEIGHT)
            self.center_x = random.randint(168, SCREEN_WIDTH - 168)

            # ДЗ 1
            window.score += 1
            # ДЗ 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("bg.png")
        self.car = Car("yellow_car.png", 0.8)
        self.wall = Wall("wall.png", 0.8)
        self.game = True

        # ДЗ 1
        self.score = 0
        # ДЗ 1

        # ДЗ 2
        self.win = False

    # ДЗ 2

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.car.change_x = 0
            self.car.angle = 0

    def on_key_press(self, key, modifiers):
        if self.game and not self.win:  # ДЗ 2
            if key == arcade.key.LEFT:
                self.car.change_x = -CAR_SPEED
                self.car.angle = CAR_ANGLE

            if key == arcade.key.RIGHT:
                self.car.change_x = CAR_SPEED
                self.car.angle = -CAR_ANGLE

    def setup(self):
        self.car.center_x = SCREEN_WIDTH / 2
        self.car.center_y = 100
        self.wall.center_y = SCREEN_HEIGHT
        self.wall.center_x = random.randint(168, SCREEN_WIDTH - 168)
        self.wall.change_y = WALL_SPEED

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(
            center_x=SCREEN_WIDTH / 2,
            center_y=SCREEN_HEIGHT / 2,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            texture=self.bg,
        )
        self.car.draw()
        self.wall.draw()
        if not self.game:
            arcade.draw_text(
                "Авария!",
                start_x=SCREEN_WIDTH / 2 - 150,
                start_y=SCREEN_HEIGHT / 2,
                color=arcade.color.CYAN,
                font_size=60,
            )

        # ДЗ 1
        arcade.draw_text(
            f"Счет:{self.score}",
            start_x=SCREEN_WIDTH - 180,
            start_y=SCREEN_HEIGHT - 40,
            color=arcade.color.RED,
            font_size=33,
        )
        # ДЗ 1

        # ДЗ 2
        if self.score >= 10:
            arcade.draw_text(
                "Победа!",
                start_x=SCREEN_WIDTH / 2 - 180,
                start_y=SCREEN_HEIGHT / 2,
                olor=arcade.color.CYAN,
                font_size=60,
            )
            self.win = True
        # ДЗ 2

    def update(self, delta_time):
        if self.game and not self.win:  # ДЗ 2
            self.car.update()
            self.wall.update()
        if arcade.check_for_collision(self.car, self.wall):
            self.game = False


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
