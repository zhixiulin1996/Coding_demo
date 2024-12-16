"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

In BreakoutGraphics class, I create a world containing paddle, ball and bricks(You can define CONSTANT below)
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 8  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2,
                        y=window_height - paddle_offset - paddle_height)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width / 2 - ball_radius, y=window_height / 2 - ball_radius)
        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.switch = True  # default switch is on
        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.paddle_move)
        # Draw bricks, I divide brick_rows by 5 to make sure there are always 5 color bricks (brick_rows must >=5)

        self.matrix = [[0 for x in range(brick_cols)] for y in range(brick_rows)]  ########################

        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=j * (brick_width + brick_spacing),
                              y=brick_offset + i * (brick_height + brick_spacing))
                brick.filled = True
                if i <= brick_rows // 5 - 1:
                    brick.fill_color = 'red'
                elif i <= 2 * brick_rows // 5 - 1:
                    brick.fill_color = 'orange'
                elif i <= 3 * brick_rows // 5 - 1:
                    brick.fill_color = 'yellow'
                elif i <= 4 * brick_rows // 5 - 1:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
                self.window.add(brick)
        # some variable that will be used in other methods
        self.ball_radius = ball_radius
        self.paddle_offset = paddle_offset
        self.brick_counts = brick_cols * brick_rows
        self.break_count = 0  # to calculate break count
        # Add a score board
        self.score_board = GLabel("Score: " + str(self.break_count))
        self.score_board.font = "SansSerif-20"
        self.window.add(self.score_board, x=0, y=window_height - self.score_board.height)
        # Add a life remaining board
        self.live_board = GLabel("")
        self.live_board.font = "SansSerif-30"
        self.live_board.color = 'red'
        self.window.add(self.live_board, x=0, y=self.live_board.height + 10)

    def get_dx(self):
        # To let the user get the current dx
        return self.__dx

    def get_dy(self):
        # To let the user get the current dy
        return self.__dy

    def paddle_move(self, event):
        # to make sure that paddle will always in window
        if event.x < self.paddle.width / 2:
            self.paddle.x = 0
        elif event.x > (self.window.width - self.paddle.width / 2):
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    def ball_move(self, event):
        # Initialize velocity for the ball after 2nd round
        if self.switch:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
        self.switch = False  # once change to False, the dx will not be changed even user clicks

    def judge_collision(self):
        # I use double for loop to judge the 4 point of the ball
        for i in range(2):
            for j in range(2):
                judge_obj = self.window.get_object_at(self.ball.x + i * 2 * self.ball_radius,
                                                      self.ball.y + j * 2 * self.ball_radius)
                if judge_obj not in [None, self.score_board, self.live_board]:
                    # if the ball faces bricks
                    if judge_obj is not self.paddle:
                        self.window.remove(judge_obj)
                        self.break_count += 1
                        self.score_board.text = "Score: " + str(self.break_count)
                    # if the ball faces paddle, move vertically by ball and paddle y-cordi. difference
                    if judge_obj is self.paddle:
                        self.ball.move(0, -(self.ball.y + 2 * self.ball_radius - self.paddle.y))
                    return 1  # if return 1, it means need to reflect the ball at the user side
        return 0  # if return 0, the ball doesn't touch anything

    def back_to_center(self):
        # to make ball back to the center place
        self.ball.x = self.window.width / 2 - self.ball_radius
        self.ball.y = self.window.height / 2 - self.ball_radius
