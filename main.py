import random
import matplotlib
import matplotlib.pyplot as plt

matplotlib.interactive(True)


def random_walk():
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
        movement = random.choice(movements)
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


def run():
    time_data, position_data = random_walk()
    plt.plot(time_data, position_data, 'r-')
    plt.title("1D Random Walk in Python")
    plt.show()


if __name__ == "__main__":
    run()
