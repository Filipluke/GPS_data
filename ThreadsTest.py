
def infinite_loop(stop_signal):
    while True:
        print("x")
        if stop_signal == 1:
            break

stop_signal = 0  # ustawienie początkowej wartości stop_signal na 0

def stop_loop():
    global stop_signal
    stop_signal = 1  # ustawienie wartości stop_signal na 1

# uruchomienie funkcji infinite_loop w osobnym wątku
import threading
thread = threading.Thread(target=infinite_loop, args=(stop_signal,))
thread.start()

# zaczekaj 5 sekund, a następnie wywołaj funkcję stop_loop, aby zakończyć pętlę infinite_loop
import time
time.sleep(5)
stop_loop()

# oczekiwanie na zakończenie wątku
thread.join()