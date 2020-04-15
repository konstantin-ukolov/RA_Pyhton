import re
import sys

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class PingParser(object):
    _pattern = r'^Reply from (.*): bytes=(\d+) time=(\d+)ms TTL=(\d+)$'
    _results = list()

    host = str()

    @classmethod
    def parse(cls):
        while True:
            line = sys.stdin.readline()
            sys.stdout.write(line)

            match = re.search(cls._pattern, line.strip())

            if match:
                cls.host = match.group(1)
                cls._results.append(match.group(3))

                return cls._results


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)


    def animate(i):
        xs = list()
        ys = list()

        data = PingParser.parse()

        for x, y in enumerate(data):
            xs.append(x)
            ys.append(y)

        ax.clear()
        ax.plot(xs, ys)

        plt.title(PingParser.host)
        plt.xlabel('Package')
        plt.ylabel('Time (ms)')

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
