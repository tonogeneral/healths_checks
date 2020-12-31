import sys
import shutil
import os

def check_reboot():
    return os.path.exists("/run/reboot-required")


def check_cpu_constrained():
    return psutil.cpu_percent(1) > 75


def check_disk_full(disk,min_absolute,min_percent):
    "Return true if there isnt enough disk space"
    du = shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #Calculate how many of free gygabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

# realizamos modificaciones
# Tenemos algunos problemas
def main():
    if check_reboot():
        print("pending reboot")
        sys.exit(1)
    if check_disk_full(disk = "/",min_gb=2,min_percent=10):
        print("Disco LLeno")
        sys.exit(1)
    print("Todo OK, Jajaja")
    sys.exit(0)
main()
