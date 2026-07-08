def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # نشيل علامة الدولار ونحول النص لرقم عشري
    return float(d.replace("$", ""))


def percent_to_float(p):
    # نشيل علامة النسبة المئوية ونحول النص لرقم ونقسمه على 100
    return float(p.replace("%", "")) / 100


main()
