def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate: "))
    t = float(input("Enter Time: "))

    si = simple_interest(p, r, t)
    print("Simple Interest:", si)
