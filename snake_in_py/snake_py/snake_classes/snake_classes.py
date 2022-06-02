class Snake:
    """
    Class creates a snake
    with color,lenght,and holds
    its positions on the map.

    the object can set the snake
    position,make the snake grow
    and define its color.

    :author:Mr-76
    """
    def __init__(self,snake_lenght,snake_color):
        """
        Constructor of the object

        The constructor recives 2 value
        with the snake lenght and its color
        all the other atributes have
        default values.


        :param snake_lenght: snake lenght
        :type snake_lenght: int

        :param snake_color: snake color
        :type snake_color: tuple
        """
        self._snake_lenght = snake_lenght
        self._snake_body = []
        self._snake_color = snake_color
        self._snake_x_pos = 0 #call map to set it on creation
        self._snake_y_pos = 0
        self._snake_head = [] #unset every loop
        self._snake_x_add_pace = 0
        self._snake_y_add_pace = 0

    def get_snake_color(self):
        """
        Returns the current snake color

        :return _snake_color:
        """
        return self._snake_color

    def snake_grow(self):
        """
        This method makes the snake
        grow in size.
        """
        self._snake_lenght += 1

    def set_position(self,x_axis,y_axis):
        """
        This method sets the snake
        position atributes on bases on
        the x and y axis values.

        :param x_axis: x axis value
        :type x_axis: int

        :param y_axis: y axis value
        :type y_axis: int
        """

        self._snake_x_pos = x_axis
        self._snake_y_pos = y_axis

    def add_pace(self,x_pace,y_pace):
        """
        This method adds a pace value
        to the current snake,position
        based at the time the keys
        for movement are used.

        :param x_pace: pace on x axis
        :type x_pace: int

        :param y_pace: pace on y axis
        :type y_pace: int
        """
        self._snake_x_add_pace = x_pace
        self._snake_y_add_pace = y_pace

    def sub_pace(self,x_pace,y_pace):
        """
        This method subtracs a pace value
        to the current snake,position
        based at the time the keys
        for movement are used.

        :param x_pace: pace on x axis
        :type x_pace: int

        :param y_pace: pace on y axis
        :type y_pace: int
        """
        self._snake_x_add_pace = x_pace * (-1)
        self._snake_y_add_pace = y_pace * (-1)

    def change_pos(self):
        """
        This method moves the
        snake by changing its x and y
        axis variable values.
        """
        self._snake_x_pos += self._snake_x_add_pace
        self._snake_y_pos += self._snake_y_add_pace
        self._snake_head = []
        self._snake_head.append(self._snake_x_pos)
        self._snake_head.append(self._snake_y_pos)
        self._snake_body.append(self._snake_head)

    def check_size_eat_self(self):
        """
        This method checks if the snake
        eats it self wich means game over
        as well checks the size of it so
        it can keep goin on,so it deletes
        its last position to not be
        rendered on the screen.

        :return game_over: boolean.
        """
        gamer_over = False
        if len(self._snake_body) > self._snake_lenght:
            del self._snake_body[0]

        for list_snake in self._snake_body[:-1]:
            if list_snake == self._snake_head:
                game_over = True
                return game_over
        return gamer_over

    def get_pos_body(self):
        """
        Method returns the snake
        body.

        :return _snake_body: snake body
        witch means all the positions it
        holds.
        """
        return self._snake_body

    def get_x_y_pos(self):
        """
        Method returns a list with
        the snake x and y position.
        """
        return [self._snake_x_pos,self._snake_y_pos]
