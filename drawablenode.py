"""DrawableNode"""
import pygame


class DrawableNode(object):
    '''drawable node'''

    def __init__(self, graphnode, ident):
        posx = graphnode.value[0]
        posy = graphnode.value[1]
        self.string = ""

        size = 200
        self.width = size
        self.height = size
        self.identification = ident
        self.index = (posx, posy)
        self.value = self.index
        self.xpos = (5 + self.width) * posx + 5
        self.ypos = (5 + self.height) * posy + 5
        self.pos = (self.width * posx, self.height * posy)
        self.screenpos = (self.xpos, self.ypos)
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height))
        self._color = (102, 255, 102)

    def printpos(self, mousepos):
        """Test"""
        x = mousepos[0]
        y = mousepos[1]
        if (x > self.rect.left and x < self.rect.right and y > self.rect.top and y <
                self.rect.bottom):
            return self

    def draw(self, screen, font, init=True, text=True):
        """Draw"""
        self.surface.fill(self._color)
        screen.blit(self.surface, self.screenpos)

        if self.identification == 0:
            self.string = "Seek"
        elif self.identification == 1:
            self.string = "Flee"
        else:
            self.string = "Wander"

        textg = font.render(str(self.string), True, (1, 1, 1))
        textgpos = (self.xpos + self.width / 2 - 35,
                    self.ypos + self.height / 2 - 20)  # middle

        if init and text:
            screen.blit(textg, textgpos)
