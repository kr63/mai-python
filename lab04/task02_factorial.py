import concurrent.futures
import threading


class Factorial:
    def __init__(self):
        self._lock = threading.Lock()
        self.results = dict()

    def calculate(self, number):
        with self._lock:
            result = 1
            for item in range(1, number + 1):
                result *= item
            self.results[number] = result

if __name__ == "__main__":
    factorial = Factorial()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(factorial.calculate, 12)

    for value in factorial.results.values():
        print(value)
