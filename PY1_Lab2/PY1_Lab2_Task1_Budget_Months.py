moneyCapital = 20000   # Подушка безопасности
SALARY = 5000           # Ежемесячная зарплата
spend = 6000            # Траты за первый месяц
INCREASE = 0.05         # Ежемесячный рост цен

monthsCounter = 0
while (moneyCapital+SALARY >= spend):
    moneyCapital += SALARY
    moneyCapital -= spend
    monthsCounter += 1
    spend *= (1+INCREASE)

print("Количество месяцев, которое можно протянуть без долгов:", monthsCounter)