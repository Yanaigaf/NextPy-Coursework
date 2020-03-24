'''
6.2.5
import the previous file
create class BirthdayCard which inherits from GreetingCard. Add attribute _sender_age
'''


import nextpy6_2_1


class BirthdayCard(nextpy6_2_1.GreetingCard):
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch', sender_age=0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print(f'Happy {self._sender_age} birthday!')
