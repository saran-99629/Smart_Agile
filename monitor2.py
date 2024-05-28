import psutil
from collections import defaultdict

def get_running_apps():
    apps = defaultdict(lambda: {'count': 0, 'cpu_time': 0, 'cpu_percent': 0})
    total = 0
    for proc in psutil.process_iter(['pid', 'name', 'cpu_times', 'cpu_percent']):
        try:
            username = proc.username()
        except psutil.AccessDenied:
            username = 'AccessDenied'

        if username != 'SYSTEM':  # Exclude system processes
            proc_info = apps[proc.info['name']]
            proc_info['count'] += 1
            proc_info['cpu_time'] += proc.info['cpu_times'].user + proc.info['cpu_times'].system
            proc_info['cpu_percent'] += proc.info['cpu_percent']
            total += 1
    return apps, total

def print_running_apps(apps, total):
    print("Running User Applications:")
    for app, info in apps.items():
        percentage = (info['count'] / total) * 100
        print(f"{app}: {info['count']} instances ({percentage:.2f}%)")
        print(f"  Total CPU Time: {info['cpu_time']:.2f} seconds")
        print(f"  CPU Utilization: {info['cpu_percent']:.2f}%")

if __name__ == "__main__":
    running_apps, total = get_running_apps()
    print_running_apps(running_apps, total)
