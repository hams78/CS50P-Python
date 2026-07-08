# نطلب التحية من المستخدم وننظفها ونحولها لحروف صغيرة فوراً
greeting = input("Greeting: ").strip().lower()

# الشرط الأول: لو بدأت التحية بـ hello
if greeting.startswith("hello"):
    print("$0")
# الشرط الثاني: لو بدأت بحرف h فقط (ولم تكن hello لأن الشرط الأول بيفلترها)
elif greeting.startswith("h"):
    print("$20")
# أي حالة أخرى
else:
    print("$100")
