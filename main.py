# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import process_state
import thread_state


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    thread = thread_state.ThreadState()
    process = process_state.ProcessState()
    # thread.write_to_file("hi", "ron")
    # thread.write_to_file("hello", "mario")
    thread.read_from_file("hi")
    # thread.del_from_file("hello")
    # process.write_to_file("hi", "ron")
    # process.write_to_file("hello", "mario")
    # process.read_from_file(1)
    # process.del_from_file("hello")

