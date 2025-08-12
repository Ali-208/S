import time

print("Stopwatch")
print("Boshlash uchun Enter bosing. To‘xtatish uchun Ctrl + C bosing.")
input()

start_time = time.time()  

try:
    while True:
        elapsed_time = time.time() - start_time
        print(f"Vaqt: {elapsed_time:.2f} soniya", end="\r")
        time.sleep(0.01)  # ekranni tez yangilash
except KeyboardInterrupt:
    print("\nStopwatch to‘xtadi.")
