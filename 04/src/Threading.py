import time

from threading import Thread, current_thread


def func(name: str):
    while True:
        print(f'{current_thread().name}: pid: {name}')
        time.sleep(1)


if __name__ == '__main__':
    tasks = list()

    for index in range(4):
        task = Thread(target=func, args=(f'Task_{index}',))
        task.start()
        tasks.append(task)

    for task in tasks:
        task.join()
