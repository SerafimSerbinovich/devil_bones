from devils_bones import DevilsBones
from utils import check_result


bones = DevilsBones()

print('Привет предлагаю сыграть в кости,\nТы подбросишь кости пять раз\n'
      'И я подброшу кости пять раз. Кто наберет больше - тот победил!')

user_answer = input('Готов?')
if user_answer.lower().strip() != 'да':
    print('Очень жаль. Приходи в другой раз')
    quit()

user_count = 0
computer_count = 0

for _ in range(5):
    first_cube, second_cube = bones.throw_bones()
    computer_count += first_cube + second_cube

    print('Моя очередь')
    print(f'Оу, я набрал {first_cube} и {second_cube}. Итого {computer_count}.')
    print()

    user_input = input('Напиши "б" чтобы бросить кости')
    while user_input.lower().strip() != 'б':
        user_input = input('Ты так и не бросил кости))')
        print()

    first, second = bones.throw_bones()
    user_count += first + second
    print(f'Оу, тебе выпало {first} и {second}. Итого {user_count}')
    print()

print(check_result(user_count, computer_count))


