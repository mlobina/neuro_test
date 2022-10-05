from libraries import NeuroNetLibrary, NeuroNluLibrary, NeuroNluRecognitionResult, NeuroVoiceLibrary
from prompt_dataclasses import forward_logic, hangup_logic, hello_logic, main_logic, action_tag_mapping


nn = NeuroNetLibrary()  # объект для работы с диалогом диалога
nlu = NeuroNluLibrary()  # обрабатывает диалог и возвращает распознный результат
nv = NeuroVoiceLibrary()  # объект для реализации логики внутри диалога


class Script:

    def __init__(self, name):
        self.name = name

    @classmethod
    def hello(cls, name, next_func):
        nv.say(f'{name},', hello_logic.hello) # Вася добрый день, удобно?
        tag = ''

        while tag not in action_tag_mapping.values():
            with nv.listen(entities=['confirm', 'wrong_time', 'repeat']) as r:
                result = nlu.extract(r)

                if result.entity('confirm') == 'True':
                    next_func()  # Script.recommend() Готовы рекомендовать...ПЕРЕХОД к др методу
                    break

                elif result.entity('confirm') == 'False':
                    nv.say(hangup_logic.hangup_wrong_time)  # извините пока пока
                    tag = cls.hangup_action('hangup_wrong_time')  # нет времени КОНЕЦ

                elif result.entity('wrong_time') == 'True':
                    nv.say(hangup_logic.hangup_wrong_time)  # извините пока пока
                    tag = cls.hangup_action('hangup_wrong_time')  # нет времени КОНЕЦ

                elif result.entity('repeat') == 'True':
                    nv.say(hello_logic.hello_repeat)  # вам удобно говорить

                elif not result.has_entities():
                    nv.say(hello_logic.hello_null) # не слышно повторите
                    with nv.listen(entities=['confirm', 'wrong_time', 'repeat']) as r:
                        result = nlu.extract(r)

                        if not result.has_entities():
                            nv.say(hangup_logic.hangup_null) # не слышно перезвоню пока пока
                            tag = cls.hangup_action('hangup_null')  # проблемы с распознаванием КОНЕЦ

                else:
                    next_func()  # LogicActions.recommend() # Готовы рекомендовать?..ПЕРЕХОД к др методу
                    break

    @classmethod
    def recommend(cls):
        nv.say(main_logic.recommend_main)  # Готовы рекомендовать?
        tag = ''

        while tag not in action_tag_mapping.values():
            with nv.listen(entities=['recommendation_score',
                                     'recommendation',
                                     'question',
                                     'wrong_time',
                                     'repeat',
                                     'dont_know']) as r:
                result = nlu.extract(r)

                if result.entity('recommendation') == 'positive':
                    nv.say(main_logic.recommend_score_positive)  # 8-9 или может 10

                elif result.entity('recommendation_score') in ['9', '10']:
                    nv.say(hangup_logic.hangup_positive)  # отлично пока пока
                    tag = cls.hangup_action('hangup_positive')  # высокая оценка

                elif result.entity('recommendation_score') in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    nv.say(hangup_logic.hangup_negative)  # понял пока пока
                    tag = cls.hangup_action('hangup_negative')  # низкая оценка

                elif result.entity('recommendation') == 'neutral':
                    nv.say(main_logic.recommend_score_neutral)  # от 0-10 оцените

                elif result.entity('recommendation') == 'negative':
                    nv.say(main_logic.recommend_score_negative)  # 0 -7

                elif result.entity('repeat') == 'True':
                    nv.say(main_logic.recommend_repeat)  # Как бы вы оценили....

                elif result.entity('recommendation') == 'dont_know':
                    nv.say(main_logic.recommend_repeat_2)  # Ну если бы вас попросили рекомендовать...

                elif result.entity('wrong_time') == 'True':
                    nv.say(hangup_logic.hangup_wrong_time)  # извините пока пока
                    tag = cls.hangup_action('hangup_wrong_time')  # нет времени КОНЕЦ

                elif not result.has_entities():
                    nv.say(main_logic.recommend_null)  # не слышно повторите
                    with nv.listen(entities=['recommendation_score',
                                             'recommendation',
                                             'question',
                                             'wrong_time',
                                             'repeat',
                                             'dont_know']) as r:
                        result = nlu.extract(r)

                        if not result.has_entities():
                            nv.say(hangup_logic.hangup_null)  # не слышно перезвоню пока пока
                            tag = cls.hangup_action('hangup_null')  # проблемы с распознаванием КОНЕЦ

                elif result.entity('question') == 'True':
                    nv.say(forward_logic.forward)  # чтобы разобраться с вопросом даю оператора
                    tag = cls.bridge_action()  # перевод на оператора КОНЕЦ

                else:
                    nv.say(main_logic.recommend_default)  # повторите
                    with nv.listen(entities=['recommendation_score',
                                             'recommendation',
                                             'question',
                                             'wrong_time',
                                             'repeat',
                                             'dont_know']) as r:
                        result = nlu.extract(r)
                        if not result.has_entities():
                            nv.say(hangup_logic.hangup_null)  # не слышно перезвоню пока пока
                            tag = cls.hangup_action('hangup_null')  # проблемы с распознаванием КОНЕЦ

    @classmethod
    def hangup_action(cls, action_name: str):
        tag = action_tag_mapping[action_name]
        return tag

    @classmethod
    def bridge_action(cls):
        tag = action_tag_mapping['forward']
        return tag


if __name__ == '__main__':
    script = Script('Den')
    nn.call('88005555777', '05-10-2022 05:07:00', script.hello('Den', script.recommend))