from input_answer import input_answer
from prompt_dataclasses import forward_logic, hangup_logic, hello_logic, main_logic, action_tag_mapping


class LogicActions:

    @classmethod
    def hello(cls, name, next_func):
        answer = input_answer(name + ',' + ' ' + hello_logic.hello) # Вася добрый день, удобно?
        tag = ''

        while tag not in action_tag_mapping.values():

            if answer == 'Да':
                next_func()  # MainLogicActions.recommend() # Готовы рекомендовать...ПЕРЕХОД к др классу
                break

            if answer == '':
                answer = input_answer(hello_logic.hello_null)  # не слышно повторите

                if answer == '':
                    print(hangup_logic.hangup_null)  # не слышно перезвоню пока пока
                    tag = cls.hangup_action('hangup_null')  # проблемы с распознаванием КОНЕЦ

            elif answer == 'Нет':
                print(hangup_logic.hangup_wrong_time) # извините пока пока
                tag = cls.hangup_action('hangup_wrong_time') # нет времени КОНЕЦ

            elif answer == 'Занят':
                print(hangup_logic.hangup_wrong_time) # извините пока пока
                tag = cls.hangup_action('hangup_wrong_time') # нет времени КОНЕЦ

            elif answer == 'Ещё раз':
                answer = input_answer(hello_logic.hello_repeat) # вам удобно говорить

            else:
                next_func()  # MainLogicActions.recommend() # Готовы рекомендовать...ПЕРЕХОД к др классу
                break

    @classmethod
    def recommend(cls):
        answer = input_answer(main_logic.recommend_main) # Готовы рекомендовать.
        tag = ''

        while tag not in action_tag_mapping.values():

            if answer == 'Да':
                answer = input_answer(main_logic.recommend_score_positive) # 8-9 или может 10

            elif answer in ['9', '10']:
                print(hangup_logic.hangup_positive) # отлично пока пока
                tag = cls.hangup_action('hangup_positive') # высокая оценка

            elif answer in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                print(hangup_logic.hangup_negative)  # понял пока пока
                tag = cls.hangup_action('hangup_negative')  # низкая оценка

            elif answer == 'Возможно':
                answer = input_answer(main_logic.recommend_score_neutral)  # от 0-10 оцените

            elif answer == 'Нет':
                answer = input_answer(main_logic.recommend_score_negative)  # 9-10

            elif answer == 'Ещё раз':
                answer = input_answer(main_logic.recommend_repeat)  # Как бы вы оценили....

            elif answer == 'Не знаю':
                answer = input_answer(main_logic.recommend_repeat_2)  # Ну если бы вас попросили рекомендовать...

            elif answer == 'Занят':
                print(hangup_logic.hangup_wrong_time)  # извините пока пока
                tag = cls.hangup_action('hangup_wrong_time')  # нет времени КОНЕЦ

            elif answer == '':
                answer = input_answer(main_logic.recommend_null)  # не слышно повторите

                if answer == '':
                    print(hangup_logic.hangup_null)  # не слышно перезвоню пока пока
                    tag = cls.hangup_action('hangup_null')  # проблемы с распознаванием КОНЕЦ

            elif answer == 'Вопрос':
                print(forward_logic.forward)  # чтобы разобраться с вопросом даю оператора
                tag = cls.bridge_action() # перевод на оператора КОНЕЦ

            else:
                answer = input_answer(main_logic.recommend_default)  # повторите
                if answer not in ['Да', '', 'Нет', 'Возможно', 'Ещё раз', 'Не знаю', 'Занят', 'Вопрос'] \
                        and answer not in ['9', '10'] \
                        and answer not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    print(hangup_logic.hangup_null)  # не слышно перезвоню пока пока
                    tag = cls.hangup_action('hangup_null')  # проблемы с распознаванием КОНЕЦ

    @classmethod
    def hangup_action(cls, action_name: str):
        tag = action_tag_mapping[action_name]
        return tag

    @classmethod
    def bridge_action(cls):
        tag = action_tag_mapping['forward']
        return tag



