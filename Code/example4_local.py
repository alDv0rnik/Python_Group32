import threading


def func():
    print("Something")


task = threading.Thread(target=func)
task.start()

print(threading.active_count())
current = threading.current_thread()

print(current.getName())
print(current.is_alive())

try:
    current.start()
except RuntimeError as e:
    print(e)

current.setName("NotmainThread")
print(current.getName())

current.name = "SuperThread"
print(current.name)
task.join()