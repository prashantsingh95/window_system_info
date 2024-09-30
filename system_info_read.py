import psutil
import time
import schedule

def get_system_info():
    battery = psutil.sensors_battery()
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")  # Assuming root directory
    net_io = psutil.net_io_counters()

    print(f"Battery: {battery.percent}%")
    print(f"CPU: {cpu_usage}%")
    print(f"Memory Usage: {mem_usage.percent}%")
    print(f"Disk Usage: {disk_usage.percent}%")
    print(f"Network In: {net_io.bytes_recv / 1024**2:.2f} MB/s")
    print(f"Network Out: {net_io.bytes_sent / 1024**2:.2f} MB/s")

def run_background_task():
    schedule.every(5).minutes.do(get_system_info)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_background_task()