# countdown.py
import time

seconds = int(input("How many seconds to count down? "))

print("⏳ Countdown starting...")
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)  # Wait 1 second

print("🎉 Time's up!")
