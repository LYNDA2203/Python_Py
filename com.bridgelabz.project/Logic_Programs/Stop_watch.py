import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        input("Press Enter to START the stopwatch...")
        self.start_time = time.time()
        print("Stopwatch started.")

    def stop(self):
        input("Press Enter to STOP the stopwatch...")
        self.end_time = time.time()
        print("Stopwatch stopped.")

    def elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            print("Stopwatch has not been used properly.")
        else:
            elapsed = self.end_time - self.start_time
            print(f"Elapsed Time: {elapsed:.2f} seconds")

# ----------- Run the Stopwatch -------------
if __name__ == "__main__":
    sw = Stopwatch()
    sw.start()
    sw.stop()
    sw.elapsed_time()