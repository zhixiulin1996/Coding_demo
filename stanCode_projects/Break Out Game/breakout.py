"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is a extended version of breakout game with external function listed as below:
1. Score board (set up at coder file)
2. Remaining lives board (set up at coder file, update at user file)
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts

graphics = BreakoutGraphics()


def main():
    life_count = NUM_LIVES  # to count the remaining lives
    # Initialize the live board
    update_life_board(life_count)
    # get initial velocity
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    # Add the animation loop here!
    while True:
        judge_result = graphics.judge_collision()
        if judge_result == 1:
            dy = -dy
        if not graphics.switch:  # ball will only move when switch is False
            graphics.ball.move(dx, dy)
            # ball reflection condition
            if graphics.ball.y <= 0:
                dy = -dy
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                dx = -dx
            # ball out of range
            if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                dx = graphics.get_dx()  # reset a new dx
                graphics.back_to_center()
                graphics.switch = True
                life_count -= 1
                update_life_board(life_count)
            # Game over conditions
            if life_count == 0 or graphics.break_count == graphics.brick_counts:
                graphics.back_to_center()
                break
        pause(FRAME_RATE)


def update_life_board(life_count):
    life_board_string = ""
    for i in range(life_count):
        life_board_string += "\u2665"
    graphics.live_board.text = life_board_string


if __name__ == '__main__':
    main()
