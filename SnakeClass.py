class Snake:
    def __init__(self):
        self.wspX = [10]
        self.wspY = [10]
        self.dir = 'up'
        self.len_ch = False
        self.old_dir = ''

    def move(self):
        self.old_dir = self.dir
        if self.dir == 'up' and self.old_dir != 'down':
            self.wspX.insert(0,self.wspX[0])
            self.wspY.insert(0,self.wspY[0] - 1)
        if self.dir == 'down' and self.old_dir != 'up':
            self.wspX.insert(0, self.wspX[0])
            self.wspY.insert(0, self.wspY[0] + 1)
        if self.dir == 'left' and self.old_dir != 'right':
            self.wspX.insert(0, self.wspX[0] - 1)
            self.wspY.insert(0, self.wspY[0])
        if self.dir == 'right' and self.old_dir != 'left':
            self.wspX.insert(0, self.wspX[0]+1)
            self.wspY.insert(0, self.wspY[0])
        if not self.len_ch:
            self.wspX.pop(-1)
            self.wspY.pop(-1)
        else:
            self.len_ch = False

    def collision(self):
        kwadrat = 15
        game_over = False
        if self.wspX[0] < -1 or self.wspX[0] > 53:
            game_over = True
        if self.wspY[0] < -1 or self.wspY[0] > 39:
            game_over = True
        return game_over

    def collision_with_snake(self):
        for i in range(len(self.wspY)):
            if i != 0:
                if self.wspX[0] == self.wspX[i] and self.wspY[0] == self.wspY[i]:
                    game_over = True
                    return True
        return False
    def eat(self, obj):
        if self.wspX[0] == obj.wspX and self.wspY[0] == obj.wspY:
            obj.RandPos()
            self.len_ch = True
            return True
        return False