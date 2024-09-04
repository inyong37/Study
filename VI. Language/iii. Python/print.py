# ANSI escape codes for text colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

# Define task messages with emojis and colors
def print_task_status(task_name, status):
    if status == "init":
        print(f"{BLUE}🔄 {task_name} init!{RESET}")
    elif status == "in_progress":
        print(f"{CYAN}⏳ {task_name} in progress...{RESET}")
    elif status == "paused":
        print(f"{YELLOW}⏸️ {task_name} paused.{RESET}")
    elif status == "error":
        print(f"{RED}❌ {task_name} encountered an error!{RESET}")
    elif status == "success":
        print(f"{GREEN}✅ {task_name} done!{RESET}")
    elif status == "failed":
        print(f"{RED}⚠️ {task_name} failed!{RESET}")
    else:
        print(f"{task_name} status unknown.")

# Example usage
tasks = ["Task A", "Task B", "Task C"]

print_task_status(tasks[0], "init")
print_task_status(tasks[1], "in_progress")
print_task_status(tasks[2], "paused")
print_task_status(tasks[0], "error")
print_task_status(tasks[1], "success")
print_task_status(tasks[2], "failed")
