from random import randint


class BoardTexts:
    @staticmethod
    def generate_list(size=50, luck=10, bad=10):
        blank = size - luck - bad
        texts = [[], [], []]

        for i in range(size):
            if blank > 0:
                index = randint(0, 7)
                txts = [
                    '',
                    '',
                    'Continue!',
                    '',
                    '',
                    'Indo bem!',
                    '',
                    ''
                ]

                texts[0].append([txts[index]])
                blank -= 1

            else:
                value = randint(50, 500)

                if luck > 0:
                    texts[1].append([f'+ R$ {value}', value])
                    luck -= 1

                elif bad > 0:
                    texts[2].append([f'- R$ {value}', value * -1])
                    bad -= 1

        return texts
