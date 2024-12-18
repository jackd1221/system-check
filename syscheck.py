import psutil

def check_disk_usage():
    try:
        disk_usage = psutil.disk_usage('/')
        return f"Disk Usage: {disk_usage.percent}%"
    except Exception as e:
        return f"Error checking disk usage: {e}"

def check_memory_usage():
    try:
        memory_info = psutil.virtual_memory()
        return f"Memory Usage: {memory_info.percent}%"
    except Exception as e:
        return f"Error checking memory usage: {e}"

def check_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        return f"CPU Usage: {cpu_usage}%"
    except Exception as e:
        return f"Error checking CPU usage: {e}"

def check_per_cpu_usage():
    try:
        per_cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        return "Per-CPU Usage: " + ", ".join([f"CPU {i}: {usage}%" for i, usage in enumerate(per_cpu_usage)])
    except Exception as e:
        return f"Error checking per-CPU usage: {e}"

def check_swap_memory_usage():
    try:
        swap = psutil.swap_memory()
        return (f"Swap Memory - Total: {swap.total / (1024 ** 3):.2f} GB, "
                f"Used: {swap.used / (1024 ** 3):.2f} GB, "
                f"Free: {swap.free / (1024 ** 3):.2f} GB, "
                f"Usage: {swap.percent}%")
    except Exception as e:
        return f"Error checking swap memory usage: {e}"

def check_disk_io():
    try:
        disk_io = psutil.disk_io_counters()
        return (f"Disk I/O - Read: {disk_io.read_bytes} bytes, "
                f"Write: {disk_io.write_bytes} bytes")
    except Exception as e:
        return f"Error checking disk I/O: {e}"

def check_network_io():
    try:
        net_io = psutil.net_io_counters()
        return f"Network I/O - Sent: {net_io.bytes_sent} bytes, Received: {net_io.bytes_recv} bytes"
    except Exception as e:
        return f"Error checking network I/O: {e}"

def check_network_connections():
    try:
        connections = psutil.net_connections()
        return f"Active Network Connections: {len(connections)}"
    except Exception as e:
        return f"Error checking network connections: {e}"

def check_detailed_memory_info():
    try:
        memory_info = psutil.virtual_memory()
        return (f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB\n"
                f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB\n"
                f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB\n"
                f"Memory Usage: {memory_info.percent}%")
    except Exception as e:
        return f"Error checking detailed memory info: {e}"

def main():
    report = [
        check_disk_usage(),
        check_memory_usage(),
        check_cpu_usage(),
        check_per_cpu_usage(),
        check_swap_memory_usage(),
        check_disk_io(),
        check_network_io(),
        check_network_connections(),
        check_detailed_memory_info(),
    ]

    with open('system_health_report.txt', 'w') as file:
        for line in report:
            file.write(line + '\n')

    print("System health report generated.")

if __name__ == "__main__":
    main()