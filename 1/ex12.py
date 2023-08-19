graus = input("digite se a temperatura eh em celsius(c) ou fahrenheit(f): ")
temp = float(input("digite a temperatura: "))

if graus == "c" or graus == "C":
    tf = (9 / 5) * temp + 32
    print(f"{temp} graus celsius eh igual a {tf} graus fahrenheit")

elif graus == "f" or graus == "F":
    tc = (5 / 9) * (temp - 32)
    print(f"{temp} graus fahrenheit eh igual a {tc} graus celsius")
