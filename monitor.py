# import psutil
# import matplotlib.pyplot as plt
# from collections import defaultdict

# def get_running_apps():
#     apps = defaultdict(int)
#     for proc in psutil.process_iter(['pid', 'name']):
#         apps[proc.info['name']] += 1
#     return apps

# def plot_running_apps(apps):
#     labels = apps.keys()
#     sizes = apps.values()

#     plt.figure(figsize=(10, 8))
#     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
#     plt.axis('equal')
#     plt.title('Running Applications')
#     plt.show()

# if __name__ == "__main__":
#     running_apps = get_running_apps()
#     plot_running_apps(running_apps)
# import psutil
# import matplotlib.pyplot as plt
# from collections import defaultdict

# def get_running_apps():
#     apps = defaultdict(int)
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             username = proc.username()
#         except psutil.AccessDenied:
#             username = 'AccessDenied'

#         if username != 'SYSTEM':  # Exclude system processes
#             apps[proc.info['name']] += 1
#     return apps

# def plot_running_apps(apps):
#     labels = apps.keys()
#     sizes = apps.values()

#     plt.figure(figsize=(10, 8))
#     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
#     plt.axis('equal')
#     plt.title('Running User Applications')
#     plt.show()

# if __name__ == "__main__":
#     running_apps = get_running_apps()
#     plot_running_apps(running_apps)
import psutil
from collections import defaultdict

def get_running_apps():
    apps = defaultdict(int)
    total = 0
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            username = proc.username()
        except psutil.AccessDenied:
            username = 'AccessDenied'

        if username != 'SYSTEM':  # Exclude system processes
            apps[proc.info['name']] += 1
            total += 1
    return apps, total

def print_running_apps(apps, total):
    print("Running User Applications:")
    for app, count in apps.items():
        percentage = (count / total) * 100
        print(f"{app}: {count} instances ({percentage:.2f}%)")

if __name__ == "__main__":
    running_apps, total = get_running_apps()
    print_running_apps(running_apps, total)
