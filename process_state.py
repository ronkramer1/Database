import threading
import time
from multiprocessing import Process, Semaphore

import process_client


class ProcessState:

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
