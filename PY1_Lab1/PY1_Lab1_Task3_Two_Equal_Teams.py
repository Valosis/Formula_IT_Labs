list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Assuming that the number of players is an even number
indexMiddlePlayer = int(len(list_players)/2)

print(list_players[:indexMiddlePlayer])
print(list_players[indexMiddlePlayer:])