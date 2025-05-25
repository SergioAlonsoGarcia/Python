import time

while True:
    ahora = time.strftime("%H:%M:%S")  
    print(f"\rHora actual: {ahora}", end="")  
    time.sleep(1)  
