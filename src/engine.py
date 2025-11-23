def create_player():
    return {
        'oxygen': 100,
        'life': 100,
        'energy': 100,
        'sanity': 100,
        'sector': "0000-A",
        'log': [],
    }


def show_status(player):
    print('oxygen', player['oxygen'])
    print('life', player['life'])
    print('energy', player['energy'])
    print('sanity', player['sanity'])
    print('sector', player['sector'])
    print('log', player['log'])


def lose_oxygen(player, amount=5):
    player['oxygen'] -= amount
    if player['oxygen'] < 0:
        player['oxygen'] = 0