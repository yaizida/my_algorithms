class Ghost():
    def __init__(self, nickname, color):
        self.nickname = nickname
        self.color = color

    def print_info(self):
        print('Тебя приветствует', self.nickname + '!')
        print(self.nickname, '- это', self.color, 'Pac-Man.')
        print('Хочешь поиграть с ним?')


character = Ghost('Blinky', 'красный')
character.print_info()


print(character.nickname)
