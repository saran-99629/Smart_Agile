# import psutil
# import os
# from collections import defaultdict

# def get_running_apps():
#     apps = defaultdict(int)
#     for proc in psutil.process_iter(['pid', 'name', 'exe']):
#         exe_path = proc.info.get('exe')
#         if exe_path and ("Program Files" in exe_path or "Program Files (x86)" in exe_path):
#             apps[os.path.basename(exe_path)] += 1
#     return apps

# def print_running_apps(apps):
#     total = sum(apps.values())
#     print("Running User Applications:")
#     for app, count in apps.items():
#         percentage = (count / total) * 100
#         print(f"{app}: {count} instances ({percentage:.2f}%)")

# if __name__ == "__main__":
#     running_apps = get_running_apps()
#     print_running_apps(running_apps)


# working with piechart


# import psutil
# import os
# import matplotlib.pyplot as plt
# from collections import defaultdict

# def get_running_apps():
#     apps = defaultdict(int)
#     for proc in psutil.process_iter(['pid', 'name', 'exe']):
#         exe_path = proc.info.get('exe')
#         if exe_path and ("Program Files" in exe_path or "Program Files (x86)" in exe_path):
#             apps[os.path.basename(exe_path)] += 1
#     return apps

# def plot_running_apps(apps):
#     labels = list(apps.keys())
#     sizes = list(apps.values())

#     plt.figure(figsize=(10, 8))
#     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
#     plt.axis('equal')
#     plt.title('Running User Applications')
#     plt.show()

# def print_running_apps(apps):
#     total = sum(apps.values())
#     print("Running User Applications:")
#     for app, count in apps.items():
#         percentage = (count / total) * 100
#         print(f"{app}: {count} instances ({percentage:.2f}%)")

# if __name__ == "__main__":
#     running_apps = get_running_apps()
#     plot_running_apps(running_apps)
#     print_running_apps(running_apps)


# bar graph presentation
import psutil
import os
import matplotlib.pyplot as plt
from collections import defaultdict

def get_running_apps():
    apps = defaultdict(int)
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        exe_path = proc.info.get('exe')
        if exe_path and ("Program Files" in exe_path or "Program Files (x86)" in exe_path):
            apps[os.path.basename(exe_path)] += 1
    return apps

def plot_running_apps(apps):
    labels = list(apps.keys())
    values = list(apps.values())

    plt.figure(figsize=(12, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Applications')
    plt.ylabel('Number of Instances')
    plt.title('Running User Applications')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def print_running_apps(apps):
    total = sum(apps.values())
    print("Running User Applications:")
    for app, count in apps.items():
        percentage = (count / total) * 100
        print(f"{app}: {count} instances ({percentage:.2f}%)")

if __name__ == "__main__":
    running_apps = get_running_apps()
    plot_running_apps(running_apps)
    print_running_apps(running_apps)
