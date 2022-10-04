from dataclasses import dataclass


@dataclass(frozen=True)
class HangupLogic:
    hangup_positive: str = 'Отлично! Большое спасибо за уделенное время! Всего Вам доброго!'
    hangup_negative: str = 'Я вас понял. В любом случае большое спасибо за уделенное время!' \
                           'Всего вам доброго!'
    hangup_wrong_time: str = 'Извините, пожалуйста, за беспокойство. Всего вам доброго!'
    hangup_null: str = 'Вас всё-равно не слышно, будет лучше, если я перезвоню. Всего вам доброго!'


@dataclass(frozen=True)
class ForwardLogic:
    forward: str = 'Чтобы разобраться в вашем вопросе, я переключу звонок на моих коллег.' \
                    'Пожалуйста, оставайтесь на линии'


@dataclass(frozen=True)
class MainLogic:
    recommend_main: str = 'Скажите, а готовы ли вы рекомендовать нашу компанию своим друзьям?' \
                          'Оцените, пожалуйста, по шкале от «0» до «10», где «0» - не буду рекомендовать,' \
                          '«10» - обязательно порекомендую.'
    recommend_repeat: str = 'Как бы вы оценили возможность порекомендовать нашу компанию своим знакомым' \
                            'по шкале от 0 до 10, где 0 - точно не порекомендую,' \
                            '10 - обязательно порекомендую.'
    recommend_repeat_2: str = 'Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым,' \
                              'вы бы стали это делать? Если «да» - то оценка «10»,' \
                              'если точно нет – «0».'
    recommend_score_negative: str = 'Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?'
    recommend_score_neutral: str = 'Ну а от 0 до 10 как бы вы оценили ?'
    recommend_score_positive: str = 'Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10  ?'
    recommend_null: str = 'Извините, вас совсем не слышно, повторите, пожалуйста?'
    recommend_default: str = 'Повторите, пожалуйста!'


@dataclass(frozen=True)
class HelloLogic:
    hello: str = 'Добрый день! Вас беспокоит компания X, мы проводим опрос удовлетворенности нашими услугами.' \
                 'Подскажите, вам удобно сейчас говорить?'
    hello_repeat: str = 'Это компания X  Подскажите, вам удобно сейчас говорить?'
    hello_null: str = 'Извините, вас не слышно. Вы могли бы повторить'


hello_logic = HelloLogic()
hangup_logic = HangupLogic()
forward_logic = ForwardLogic()
main_logic = MainLogic()

action_tag_mapping = {
    'hangup_positive': 'высокая оценка',
    'hangup_negative': 'низкая оценка',
    'hangup_wrong_time': 'нет времени для разговора',
    'hangup_null': 'проблемы с распознаванием',
    'forward': 'перевод на оператора',
}







