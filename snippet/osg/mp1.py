import os , time


def handle():
    pid = os.fork()
    if pid:
        os.waitpid(-1,0)
        print("child is %d"%pid,",i'm %d"%os.getpid())
    else:
        print("i'm child %d"%os.getppid())

if __name__ == "__main__":
    handle()