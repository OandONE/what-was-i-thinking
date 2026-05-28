"""
نوشته شده در: روزی که با list.remove آشنا شدم
وضعیت روحی: کی نیاز به regex داره وقتی میتونی ۲۰ خط remove بنویسی؟
هدف: استخراج یه چیزی از لینک روبیکا
نتیجه: ValueError (چون کاراکترها رو بیشتر از حد remove کردم)
"""

def renkfsdidnn(m):
    o = list(m)
    o.remove("j")
    o.remove("o")
    o.remove("i")
    o.remove("n")
    o.remove(" ")
    o.remove("h")
    o.remove("t")
    o.remove("t")
    o.remove("p")
    o.remove("s")
    o.remove(":")
    o.remove("/")
    o.remove("/")
    o.remove("r")
    o.remove("u")
    o.remove("b")
    o.remove("i")
    o.remove("k")
    o.remove("a")
    o.remove(".")
    o.remove("i")
    o.remove("r")
    o.remove("/")
    # o.remove("j")
    # o.remove("o")
    # o.remove("i")
    # o.remove("n")
    # o.remove("g")
    # o.remove("/")
    dn = ""
    for ydni in o:
        dn += ydni
    print(f"r : {dn}")

print("ifbofk")
print(renkfsdidnn("join https://rubika.ir/BUDJIDNODNIOFBOWNIONIOAPPOSNC"))
