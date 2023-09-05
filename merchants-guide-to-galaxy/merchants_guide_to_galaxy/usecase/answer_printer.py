from merchants_guide_to_galaxy.usecase.answer_queries_use_case import Answer


class AnswerPrinter:
    @staticmethod
    def print(answers: list[Answer]) -> None:
        answer_statements = [answer.outcome for answer in answers]
        print('\n'.join(answer_statements))
