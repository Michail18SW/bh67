import keyboard as keyboard


# class Button:
#     def __init__(self, text: str, link: str):
#         self.text = text
#         self.link = link
#
#     def dict(self) -> dict:
#         return{'text': self.text, 'link': self.link}
#
# button1 = Button('Hi', 'http://some-site.com')
# print(button1.dict())
#
# class Keyboard:
#     def __init__(self, name: str, *buttons: Button) -> None:
#         self.name = name
#         self.buttons = buttons
#
#     def dict(this):
#         return {
#             'name': this.name,
#             'buttons': [button.dict() for button in this.buttons]
#         }
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         try:
#             return self.buttons[self.i].dict()
#         except IndexError:
#             self.i = -1
#             raise StopIteration
#
# buttons = [Button(f'button{i}', f'http://link.{i}') for i in range(1, 11)]
# keyboard1 = Keyboard('Keyboard 1', *buttons)
# i = iter(keyboard1)
# print(next(i))
# for button in keyboard1:
#     print(button)
# print(Keyboard.dict(keyboard1))
# print(keyboard.dict())

def is_palindrome(text: str):
    pass

