def increment_strength(game):
    strength_cost = 5 * game.player.stats['strength']
    if game.player.stats['gold'] >= strength_cost:
        game.player.stats['gold'] -= strength_cost
        game.player.stats['strength'] += 1
        game.menu_bar.update_stats_tbox()
