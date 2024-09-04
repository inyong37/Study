def print_task_status(task_name, status):
    """
    Logs the status of a task with appropriate color and emoji.

    :param task_name: The name of the task to be logged.
    :param status: The status of the task.
                   Valid options are 'init', 'in_progress', 'paused', 'error', 'success', 'failed'.
    """
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"

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
