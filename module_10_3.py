import threading
from threading import Thread, Lock
import random
from time import sleep
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
    def deposit(self):

        for i in range(100):
            x = random.randint(50,500)
            self.balance = self.balance + x
            time.sleep(0.001)
            print(f'Пополнение: {x}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()



    def take(self):
        for i in range(100):
            x = random.randint(50,500)
            print(f'Запрос на {x}.')
            if self.balance > x:
                self.balance = self.balance - x
                time.sleep(0.001)
                print(f'Снятие: {x}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

