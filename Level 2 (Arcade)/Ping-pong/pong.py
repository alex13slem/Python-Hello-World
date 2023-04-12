"""
    Цель: доделать игру Пинг-понг, настроить управление и взаимодействие спрайтов.
    
    + проверить домашнее задание;
    + вспомнить команды прошлого урока; 
    + настроить управление ракеткой с клавиатуры;
    + определить, что произойдет, когда отпустишь клавишу;
    + прописать, как мяч будет отбиваться; 
    + ввести подсчет очков; 
    + добавить проигрыш в игре; 
    + ввести переменную состояния игры;
    + добавить победу в игру;
    + сделать выводы по уроку; 
    + получить домашнее задание.

"""
import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Пинг-Понг"

SPEED_X = 5
SPEED_Y = 4


# ДЗ
def game_over(self, message: str):
    arcade.draw_text(
        text=message,
        start_x=0,
        start_y=SCREEN_HEIGHT / 2,
        color=(255, 33, 33),
        font_size=50,
        width=SCREEN_WIDTH,
        align="center",
    )
    self.game = False


# ДЗ


class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("ball.png", 0.1)
        self.bar = Bar("bar.png", 0.1)
        self.setup()
        self.score = 0
        self.attempts = 3
        self.game = True

    def on_key_press(self, key, modifiers):
        if self.game:
            if key == arcade.key.LEFT:
                self.bar.change_x = -SPEED_X
            if key == arcade.key.RIGHT:
                self.bar.change_x = SPEED_X

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

    def setup(self):
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

        # ДЗ
        direction = random.randint(1, 2)
        if (direction) < 2:
            self.ball.change_x = -SPEED_X
        else:
            self.ball.change_x = SPEED_X
        # ДЗ

        self.ball.change_y = SPEED_Y
        self.bar.center_x = SCREEN_WIDTH / 2

    def on_draw(self):
        self.background_color = (255, 255, 255)
        self.clear()
        self.ball.draw()
        self.bar.draw()
        arcade.draw_text(
            text=f"Счет: {self.score}",
            start_x=20,
            start_y=SCREEN_HEIGHT - 30,
            color=(0, 0, 0),
            font_size=20,
        )
        arcade.draw_text(
            text=f"Попытки: {self.attempts}",
            start_x=SCREEN_WIDTH - 200,
            start_y=SCREEN_HEIGHT - 30,
            color=(0, 0, 0),
            font_size=20,
        )

        if self.score == 20:
            # ДЗ
            # game_over(self, "Победа!")
            # ДЗ

            arcade.draw_text(
                text="Победа!",
                start_x=0,
                start_y=SCREEN_HEIGHT / 2,
                color=(255, 33, 33),
                font_size=50,
                width=SCREEN_WIDTH,
                align="center",
            )
            self.game = False

        if self.attempts == 0:
            # ДЗ
            # game_over(self, "Проиграл(")
            # ДЗ
            arcade.draw_text(
                text="Проиграл(",
                start_x=0,
                start_y=SCREEN_HEIGHT / 2,
                color=(255, 33, 33),
                font_size=50,
                width=SCREEN_WIDTH,
                align="center",
            )
            self.game = False

    def update(self, delta_time):
        self.ball.update()
        self.bar.update()
        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.bottom = self.bar.top
            self.ball.change_y = -self.ball.change_y
            self.score += 1

            # ДЗ
            if self.ball.change_x > 0:
                self.ball.change_x += 1
            if self.ball.change_x < 0:
                self.ball.change_x -= 1
            # ДЗ

        if self.ball.bottom < 0:
            self.attempts -= 1
            self.setup()
        if not self.game:
            self.ball.stop()
            self.bar.stop()


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
