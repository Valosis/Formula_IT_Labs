SALARY = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
MONTHS = 10  # Количество месяцев, которое планируется протянуть без долгов
INCREASE = 0.03  # Ежемесячный рост цен

moneySpent = 0
for i in range(10):
    moneySpent += spend
    spend *= (1 + INCREASE)

moneyCapital = round(moneySpent - 10*SALARY, 2)

print(f"Подушка безопасности, чтобы протянуть {MONTHS} месяцев без долгов:", moneyCapital)