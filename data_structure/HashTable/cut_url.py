from random import randint


class MarsURLEncoder:

    def __init__(self, my_dict=dict()):
        self.my_dict = my_dict

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        rnd_string = 'QWWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
        my_string = ''
        for i in range(6):
            a = rnd_string[randint(0, len(rnd_string)-1)]
            my_string += a
        self.my_dict[my_string] = long_url
        return 'https://ma.rs/' + my_string

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        short_url = short_url[14:len(short_url)]
        if short_url in self.my_dict:
            return self.my_dict[short_url]


first = MarsURLEncoder()
b = first.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html')
print(b)
print(b[14: len(b)])
print(first.decode(b))
