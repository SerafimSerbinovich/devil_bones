def check_result(user_count, computer_count):
    if user_count > computer_count:
        return 'Поздравляю, вы выиграли'
    elif user_count == computer_count:
        return 'В этот раз ничья!'
    return 'К сожалению, вы проиграли. Повезет в другой раз'
