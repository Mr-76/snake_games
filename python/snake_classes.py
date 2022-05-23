class snake:
    def __init__(self,snake_lenght,snake_color,snake_pace):
        self._snake_lenght = snake_lenght
        self._snake_body = []
        self._snake_color = snake_color
        self._snake_default_pace = snake_pace
        self._snake_x_pos = 0 #call map to set it on creation 
        self._snake_y_pos = 0
        self._snake_head = [] #unset every loop
        _snake_x_add_pace = 0#+ and - operation  
        _snake_y_add_pace = 0
    
    def add_pace(x_pace,y_pace):
        self._snake_x_add_pace = x_pace
        self._snake_y_add_pace = y_pace
    def sub_pace(x_pace,y_pace):
        self._snake_x_add_pace = x_pace * (-1)
        self._snake_y_add_pace = y_pace * (-1)

    def change_pos(_snake_x_add_pace,_snake_y_add_pace):
        self._snake_x_pos += _snake_x_add_pace
        self._snake_y_pos += _snake_y_add_pace
        self._snake_head.append(self._snake_x_pos)
        self._snake_head.append(self._snake_y_pos)
        self._snake_body.append(self._snake_head)

    def check_size_eat_self():
        if len(self._snake_body) > self._snake_lenght:
            del self._snake_body[0]

        for list_snake in self._snake_body[:-1]:
            if list_snake == self._snake_head:
                game_over = True
            else:
                game_over = False
        return game_over



class SnakeGameMap:
    def __init__(self,):
 
