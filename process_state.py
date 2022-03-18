import threading
import time
from multiprocessing import Process, Semaphore

import process_client


class ProcessState:

    # def write_to_file(self, key, value):
    #     t1 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t2 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t3 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t4 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t5 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t6 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t7 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t8 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t9 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t10 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t11 = Process(target=process_client.Client().set_value, args=(key, value))
    #     t12 = Process(target=process_client.Client().set_value, args=(key, value))
    #
    #     t1.start()
    #     t2.start()
    #     t3.start()
    #     t4.start()
    #     t5.start()
    #     t6.start()
    #     t7.start()
    #     t8.start()
    #     t9.start()
    #     t10.start()
    #     t11.start()
    #     t12.start()
    #
    #     t1.join()
    #     t2.join()
    #     t3.join()
    #     t4.join()
    #     t5.join()
    #     t6.join()
    #     t7.join()
    #     t8.join()
    #     t9.join()
    #     t10.join()
    #     t11.join()
    #     t12.join()
    #
    # def read_from_file(self, key):
    #     t1 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t2 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t3 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t4 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t5 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t6 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t7 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t8 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t9 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t10 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t11 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     t12 = Process(target=process_client.Client("process").get_value, args=(key, 1))
    #     # t1 = Process(target=process_client.Client().get_value, args=(key, 12))
    #     # t2 = Process(target=process_client.Client().get_value, args=(key, 11))
    #     # t3 = Process(target=process_client.Client().get_value, args=(key, 10))
    #     # t4 = Process(target=process_client.Client().get_value, args=(key, 9))
    #     # t5 = Process(target=process_client.Client().get_value, args=(key, 8))
    #     # t6 = Process(target=process_client.Client().get_value, args=(key, 7))
    #     # t7 = Process(target=process_client.Client().get_value, args=(key, 6))
    #     # t8 = Process(target=process_client.Client().get_value, args=(key, 5))
    #     # t9 = Process(target=process_client.Client().get_value, args=(key, 4))
    #     # t10 = Process(target=process_client.Client().get_value, args=(key, 3))
    #     # t11 = Process(target=process_client.Client().get_value, args=(key, 2))
    #     # t12 = Process(target=process_client.Client().get_value, args=(key, 1))
    #
    #     t1.start()
    #     t2.start()
    #     t3.start()
    #     t4.start()
    #     t5.start()
    #     t6.start()
    #     t7.start()
    #     t8.start()
    #     t9.start()
    #     t10.start()
    #     t11.start()
    #     t12.start()
    #
    #     t1.join()
    #     t2.join()
    #     t3.join()
    #     t4.join()
    #     t5.join()
    #     t6.join()
    #     t7.join()
    #     t8.join()
    #     t9.join()
    #     t10.join()
    #     t11.join()
    #     t12.join()
    #
    # def del_from_file(self, key):
    #     t1 = Process(target=process_client.Client().del_value, args=(key,))
    #     t1.start()
    #     t1.join()

    def run_read(self, key, total_processes):
        concurrency = 10
        total_task_num = total_processes
        sema = Semaphore(concurrency)
        all_processes = []
        for i in range(total_task_num):
            # once 10 processes are running, the following `acquire` call
            # will block the main process since `sema` has been reduced
            # to 0. This loop will continue only after one or more
            # previously created processes complete.
            p = Process(target=process_client.Client().get_value, args=(key, sema, i, 1))
            all_processes.append(p)
            p.start()

    def run_write(self, key, value, total_processes):
        concurrency = 1
        total_task_num = total_processes
        sema = Semaphore(concurrency)
        all_processes = []
        for i in range(total_task_num):
            # once 10 processes are running, the following `acquire` call
            # will block the main process since `sema` has been reduced
            # to 0. This loop will continue only after one or more
            # previously created processes complete.
            p = Process(target=process_client.Client().set_value, args=(key, value, sema, i))
            all_processes.append(p)
            p.start()

        # inside main process, wait for all processes to finish
        for p in all_processes:
            p.join()

    def run_delete(self, key, total_processes):
        concurrency = 1
        total_task_num = total_processes
        sema = Semaphore(concurrency)
        all_processes = []
        for i in range(total_task_num):
            # once 10 processes are running, the following `acquire` call
            # will block the main process since `sema` has been reduced
            # to 0. This loop will continue only after one or more
            # previously created processes complete.
            p = Process(target=process_client.Client().del_value, args=(key, sema, i))
            all_processes.append(p)
            p.start()

        # inside main process, wait for all processes to finish
        for p in all_processes:
            p.join()
