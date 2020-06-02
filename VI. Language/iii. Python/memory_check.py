import psutil
import os

print("=="*20)
print("== memory usage check")

result = []

for exec_num in range(1, 11):
    # BEFORE code
    print(f"== {exec_num:2d} exec")
    # general RAM usage
    memory_usage_dict_b = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent_b = memory_usage_dict_b['percent']
    print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent_b}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB_b = current_process.memory_info()[0] / 2.**20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB_b: 9.3f} KB")

    # TEST
    test_list = [0 for i in range(0, 9999)]

    # AFTER  code
    memory_usage_dict_a = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent_a = memory_usage_dict_a['percent']
    print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent_a}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB_a = current_process.memory_info()[0] / 2.**20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB_a: 9.3f} KB")
    print('DIFFERENCE : ', current_process_memory_usage_as_KB_a - current_process_memory_usage_as_KB_b, 'KB')
    result.append(current_process_memory_usage_as_KB_a - current_process_memory_usage_as_KB_b)
    del test_list
    print("--"*30)

# Reference: https://frhyme.github.io/python/python_check_memory_usage/
