"""
نوشته شده در: روزی که threading رو کشف کردم
وضعیت روحی: می‌خواستم کامپیوترم رو منفجر کنم
هدف: تست محدودیت تردهای پایتون
نتیجه: سیستم هنگ کرد، مامانم گفت چرا فن لپتاپ اینقدر صدا میده
هشدار: اجرا نکن. جدی میگم. اجرا نکن.
"""

import threading;

def h():
    import sys
    if "sys" in sys.modules:
        import sys
        return threading.Thread(target=h).start()

h()
