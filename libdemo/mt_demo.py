import threading


class ChildThread(threading.Thread):
    def run(self):
        for i in range(1, 26):
            print("Child 1 : ", i)


def print_nums():
    for i in range(1, 11):
        print("Child 2 : ", i)


mt = threading.main_thread()
ct = threading.current_thread()
cht = ChildThread()
cht.start()
t = threading.Thread(target=print_nums)
t.start()

print(f"\nMain --> {ct} {threading.active_count()}")
