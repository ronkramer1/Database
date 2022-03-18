# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from multiprocessing import Semaphore, Process

import process_client
import process_state
import thread_state


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    threads = thread_state.ThreadState()
    procs = process_state.ProcessState()

    # # process writing
    # procs.run_write("hi", "shalom", 3)
    #
    # # process reading
    # procs.run_read("hi", 12)
    #
    # # process deleting
    # procs.run_delete("hi", 10)
    #
    # # thread writing
    # threads.write_to_file("hi", "Ron", 1)
    # threads.write_to_file("hello", "Mario", 10)
    #
    # # thread reading
    # threads.read_from_file("hi", 1)
    # threads.read_from_file("hi", 12)
    # #
    # # thread deleting
    # threads.del_from_file("hello", 3)


