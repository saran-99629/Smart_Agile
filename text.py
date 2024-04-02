# import wmi

# def monitor_background_apps(memory_threshold_mb=100):
#     """
#     Monitors running background apps on Windows and identifies those exceeding 
#     a specified memory usage threshold.

#     Args:
#         memory_threshold_mb (int, optional): The memory usage threshold in MB. 
#             Processes exceeding this limit will be flagged. Defaults to 100 MB.
#     """

#     try:
#         # Connect to WMI
#         c = wmi.WMI()

#         print("** Background Apps Monitoring Report **")
#         print(f"Memory Threshold: {memory_threshold_mb} MB")
#         print("--------------------------------------")

#         # Query for running processes
#         processes = c.Win32_Process()

#         # Loop through processes and display information
#         for process in processes:
#             memory_usage_mb = int(process.WorkingSetSize) / (1024 * 1024)  # Convert bytes to MB
#             if memory_usage_mb > memory_threshold_mb:
#                 print("** High Memory Usage Alert! **")
#             print(f"Process Name: {process.Name}")
#             print(f"Process ID: {process.ProcessId}")
#             print(f"Memory Usage: {memory_usage_mb:.2f} MB")  # Format to 2 decimal places
#             print("-------------------------")
    
#     except Exception as e:
#         print(f"Error occurred while monitoring background apps: {e}")

# # Example Usage
# monitor_background_apps()  # Run with default 100 MB threshold

# # Adjust memory threshold if desired
# monitor_background_apps(memory_threshold_mb=50)  # Monitor for processes using over 50 MB





# import psutil

# def get_background_apps_cpu_times():
#     """
#     Retrieves CPU times for background apps using psutil.
#     """
#     try:
#         print("** Background Apps CPU Times **")
#         print("--------------------------------")
#         for proc in psutil.process_iter(['pid', 'name', 'cpu_times']):
#             # Check if the process is a background app (you may need to customize this condition)
#             if "background_app_criteria" in proc.info['name']:
#                 print(f"Process Name: {proc.info['name']}")
#                 print(f"Process PID: {proc.info['pid']}")
#                 print(f"CPU Times: {proc.info['cpu_times']}")
#                 print("-------------------------")
#     except Exception as e:
#         print(f"Error occurred while retrieving CPU times: {e}")

# # Example Usage
# get_background_apps_cpu_times()




import psutil

def get_all_processes_cpu_times():
    """
    Retrieves CPU times for all running processes using psutil.
    """
    try:
        print("** All Processes CPU Times **")
        print("-----------------------------")
        for proc in psutil.process_iter(['pid', 'name', 'cpu_times']):
            print(f"Process Name: {proc.info['name']}")
            print(f"Process PID: {proc.info['pid']}")
            print(f"CPU Times: {proc.info['cpu_times']}")
            print("-------------------------")
    except Exception as e:
        print(f"Error occurred while retrieving CPU times: {e}")

# Example Usage
get_all_processes_cpu_times()
