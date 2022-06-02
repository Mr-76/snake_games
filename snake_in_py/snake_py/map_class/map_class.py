class MapSnake:
    """
    This class holds the screen related
    operations to the snake game as well as
    some properties of the screen such as
    screen width the screen height the food color
    and its position.

    :author Mr-76.
    """
    def __init__(self,screen_h,screen_w,food_color):
        """
        Class constructor,builds a Map_snake object.

        :param screen_h: screen height.
        :type screen_h: int

        :param screen_w: screen widht.
        :type screen_w: int

        :param food_color: food color.
        :type food_color: tuple
        """
        self._screen_h = screen_h
        self._screen_w = screen_w
        self._food_color = food_color
        self._foodx = 0
        self._foody = 0


    def get_screen_h(self):
        """
        Returns the current screen
        height.

        :return: screen height
        """
        return self._screen_h

    def get_screen_w(self):
        """
        Returns the current screen
        width.

        :return: screen width
        """
        return self._screen_w

    def get_food_color(self):
        """
        Returns the snake game
        food color.

        :return: food color
        """
        return self._food_color

    def get_foodx(self):
        """
        Return the food
        position on the x axis

        :return: x axis int.
        """
        return self._foodx

    def get_foody(self):
        """
        Return the food
        position on the y axis

        :return: y axis int.
        """
        return self._foody

    def set_food_pos(self,foodx,foody):
        """
        Sets the food postion on the
        map
        """
        self._foodx = foodx
        self._foody = foody

