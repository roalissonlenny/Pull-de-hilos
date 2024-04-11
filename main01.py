import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadname)s: %(message)s')


print("----------------------------")
print("Dos hilos")

globalArrayNum = []
def contador2 ( inicio, fin ):
    logging.info(f'funcion con rango: {inicio} - {fin}')
    for i in range (inicio, fin+1, 1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0

t0=time.time()
listaHilos = []
t = threading.Thread(target=contador2, args=(1,50))
listaHilos.append(t)
t.start()
t = threading.Thread(target=contador2, args=(51,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join()
tf=time.time()-t0


globalArrayNum.sort()
print(f'tiempo de ejecucion: {tf}')
print(globalArrayNum)


print("----------------------------")
print("Pool de hilos")

def printHW():
    logging.info(f'funcion con rango: {inicio} - {fin}')
    print("Hola mundo:)")
                                                                                                                                                                                                                                   
globalArrayNum = []
with ThreadPoolExecutor( max_workers=2 ) as executor:
    executor.submit(contador2, 1,50)
    executor.submit(contador2, 51,100)

print(globalArrayNum)
