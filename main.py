import random
import matplotlib.pyplot as plt


def random_walk(win_probability, lose_probability):
    max_position: int = 30
    min_position: int = 0
    time_point, position = 0, 20
    positions = [position]
    time_points = [time_point]
    movements = ["POSITIVE", "NEGATIVE"]
    zero_before_reach_30: int = 0
    reach_30: bool = False

    while min_position < position < max_position:
        time_point += 1
        movement = random.choices(movements, weights = [win_probability, lose_probability], k = 1)[0]
        if movement == "POSITIVE":
            position += 1
        if movement == "NEGATIVE":
            position -= 1
        if position == max_position:
            reach_30 = True
        if position == min_position and not reach_30:
            zero_before_reach_30 += 1

        positions.append(position)
        time_points.append(time_point)

    return time_points, positions


def random_walk_2d(observations: int):
    x, y = 0, 0
    positions = [y]
    time_points = [x]
    movements = ["UP", "DOWN", "RIGHT", "LEFT"]

    for observations in range(1, observations + 1):
        movement = random.choices(movements, weights = [25, 25, 25, 25], k = 1)[0]
        if movement == "UP":
            y += 1
        if movement == "DOWN":
            y -= 1
        if movement == "RIGHT":
            x += 1
        if movement == "LEFT":
            x -= 1

        positions.append(y)
        time_points.append(x)

    return time_points, positions


def run():
    time_data, position_data = random_walk_2d(1000)
    plt.plot(time_data, position_data, 'r-')
    plt.title("1D Random Walk in Python")
    plt.show()


if __name__ == "__main__":
    run()
