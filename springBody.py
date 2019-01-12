import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def main():
    body = Body(1.0, 0.0)
    steps = 100
    data = calculateSpring(body, dt=0.1, steps=steps)
    time = [0.1 * i for i in range(steps)]
    positions = [data[i]["x"] for i in range(steps)]
    plt.plot(time, positions)
    plt.show()


class Body():

    def __init__(self, x, v):
        self._x = x
        self.v = v
        self.a = -x
        self.t = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.resetA()

    def resetA(self):
        self.a = -self._x

    def printDict(self):
        dictFormat = \
        {
            "x": self.x,
            "v": self.v,
            "a": self.a,
            "t": self.t,
        }
        return dictFormat


def calculateSpring(body, dt, steps):
    data = body
    dataset = []
    dataset.append(data.printDict())
    data.v += data.a * (dt / 2)
    data.x += dt * data.v
    data.t += 1
    dataset.append(data.printDict())
    for step in range(steps - 1):
        data.v += data.a * dt
        data.x += data.v * dt
        data.t += 1
        dataset.append(data.printDict())
    return dataset


if __name__ == "__main__":
    main()
