import os
import platform
from datetime import datetime

print(f"os: {platform.system()} {platform.release()}")
print(f"machine: {platform.machine()}")
print(f"python: {platform.python_version()}")
print(f"hostname: {platform.node()}")
print(f"cwd: {os.getcwd()}")
print(f"pid: {os.getpid()}")
print(f"time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
try:
    stat = os.statvfs("/")
    free = stat.f_bfree * stat.f_frsize / (1024**3)
    total = stat.f_blocks * stat.f_frsize / (1024**3)
    print(f"disk: {free:.1f}gb free / {total:.1f}gb total")
except:
    pass
# updated
