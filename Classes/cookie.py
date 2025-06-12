class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie_one = Cookie('Green')
cookie_two = Cookie('Orange')

print("Color of cookie one is "+ cookie_one.get_color())
print("Color of cookie two is "+ cookie_two.get_color())

print("==================After Updating the color of Second Cookie==================")

cookie_two.set_color('Blue')
print("Color of cookie one is "+ cookie_one.get_color())
print("Color of cookie two is "+ cookie_two.get_color())