import threading, queue
import time

def washer(dishs, dish_queue):
    for dish in dishs:
        print("Washing", dish)
        time.sleep(5)
        dish_queue.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print("Drying", dish)
        time.sleep(10)
        dish_queue.task_done()

if __name__ == "__main__":
    dish_queue = queue.Queue()
    
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.daemon = True
        dryer_thread.start()
        
    for n in range(2):
        dishes = ['salad', 'bread', 'entree', 'dessert']
        washer(dishes, dish_queue)
        
    dish_queue.join()
    print("모든 작업이 완료되어 프로그램을 종료합니다.")