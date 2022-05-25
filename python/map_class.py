class Map_snake:
    def __init__(self,screen_h,screen_w,food_color):
        self._screen_h = screen_h
        self._screen_w = screen_w
        self._food_color = food_color
        self._foodx = 0
        self._foody = 0


    def get_screen_h(self):
        return self._screen_h 

    def get_screen_w(self):
        return self._screen_w
    def get_food_color(self):
        return self._food_color

    def get_foodx(self):
        return self._foodx

    def get_foody(self):
        return self._foody
    
    def set_food_pos(self,foodx,foody):
        self._foodx = foodx
        self._foody = foody










