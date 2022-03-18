import threading
import time

import thread_client


class ThreadState:

    def write_to_file(self, key, value, total_threads):
        all_threads = []
        for i in range(total_threads):
            # once 10 processes are running, the following `acquire` call
            # will block the main process since `sema` has been reduced
            # to 0. This loop will continue only after one or more
            # previously created processes complete.
            t = threading.Thread(target=thread_client.Client().set_value, args=(key, value))
            all_threads.append(t)
            t.start()

            for t in all_threads:
                t.join()

    def read_from_file(self, key, total_threads):

        all_threads = []
        for i in range(total_threads):
            # once 10 processes are running, the following `acquire` call
            # will block the main process since `sema` has been reduced
            # to 0. This loop will continue only after one or more
            # previously created processes complete.
            t = threading.Thread(target=thread_client.Client().get_value, args=(key, 12))
            all_threads.append(t)
            t.start()

        for t in all_threads:
            t.join()

    def del_from_file(self, key, total_threads):
        all_threads = []
        for i in range(total_threads):
            # once 10 processes are running, the following `acquire` call
            # will block the main process since `sema` has been reduced
            # to 0. This loop will continue only after one or more
            # previously created processes complete.
            t = threading.Thread(target=thread_client.Client().del_value, args=(key,))
            all_threads.append(t)
            t.start()

        for t in all_threads:
            t.join()
