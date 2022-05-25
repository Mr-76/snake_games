class snake:
    def __init__(self,snake_lenght,snake_color,snake_pace):
        self._snake_lenght = snake_lenght
        self._snake_body = []
        self._snake_color = snake_color
        self._snake_default_pace = snake_pace
        self._snake_x_pos = 0 #call map to set it on creation 
        self._snake_y_pos = 0
        self._snake_head = [] #unset every loop
        self._snake_x_add_pace = 0  
        self._snake_y_add_pace = 0
    
    def get_snake_color(self):
        return self._snake_color

    def snake_grow(self):
        self._snake_lenght += 1
    
    def set_position(self,x,y):
        self._snake_x_pos = x
        self._snake_y_pos = y

    def add_pace(self,x_pace,y_pace):
        self._snake_x_add_pace = x_pace
        self._snake_y_add_pace = y_pace
    
    def sub_pace(self,x_pace,y_pace):
        self._snake_x_add_pace = x_pace * (-1)
        self._snake_y_add_pace = y_pace * (-1)

    def change_pos(self):
        self._snake_x_pos += self._snake_x_add_pace
        self._snake_y_pos += self._snake_y_add_pace
        self._snake_head = []
        self._snake_head.append(self._snake_x_pos)
        self._snake_head.append(self._snake_y_pos)
        self._snake_body.append(self._snake_head)

    def check_size_eat_self(self):
        gamer_over = False
        if len(self._snake_body) > self._snake_lenght:
            del self._snake_body[0]
        
        for list_snake in self._snake_body[:-1]:
            if list_snake == self._snake_head:
                game_over = True
                return game_over
            else:
                game_over = False
        return gamer_over 
        
    def get_pos_body(self):
        return self._snake_body
    
    def get_x_y_pos(self):
        return [self._snake_x_pos,self._snake_y_pos]

