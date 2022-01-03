import random
import matplotlib.pyplot as plt


def random_walk(win_probability: int, lose_probability: int):
    max_position: int = 30
    min_position: int = 0
    time_point, position = 0, 20
    positions = [position]
    time_points = [time_point]
    movements = ["POSITIVE", "NEGATIVE"]
    reach_30: bool = False

    while min_position < position < max_position:
        time_point += 1
        movement = random.choices(movements, weights=[win_probability, lose_probability], k=1)[0]
        if movement == "POSITIVE":
            position += 1
        if movement == "NEGATIVE":
            position -= 1
        if position == max_position:
            reach_30 = True

        positions.append(position)
        time_points.append(time_point)

    return time_points, positions, reach_30


def random_walk_2d(observations: int):
    x, y = 0, 0
    positions = [y]
    time_points = [x]
    movements = ["UP", "DOWN", "RIGHT", "LEFT"]

    for observations in range(1, observations + 1):
        movement = random.choices(movements, weights=[25, 25, 25, 25], k=1)[0]
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


def run_random_walk(observations: int):
    count_before_reach_30: int = 0
    for observation in range(1, observations + 1):
        time_data, position_data, reach_30 = random_walk(49, 51)
        if not reach_30:
            count_before_reach_30 += 1
    print('tries before reach 30: ' + str(count_before_reach_30))


def run():
    time_data, position_data = random_walk_2d(1000)
    plt.plot(time_data, position_data, 'r-')
    plt.title("2D Random Walk in Python")
    plt.show()
    time_data, position_data, reach_30 = random_walk(50, 50)
    plt.plot(time_data, position_data, 'r-')
    plt.title("Random Walk in Python")
    plt.show()
    run_random_walk(100)


if __name__ == "__main__":
    run()
