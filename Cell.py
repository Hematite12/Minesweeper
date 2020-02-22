from Constants import *

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pressed = False
        self.mine = False
        self.flag = False
        self.number = 0
    
    def getPos(self):
        return (MARGIN + self.x * CELLDIM, MARGIN + self.y * CELLDIM)
    
    def show(self):
        if self.pressed:
            fill(*CELLCOLORPRESSED)
        else:
            fill(*CELLCOLORUNPRESSED)
        xPos, yPos = self.getPos()
        rect(xPos, yPos,CELLDIM,CELLDIM)
        if self.pressed:
            if self.mine:
                fill(*MINECOLOR)
                ellipse(xPos + CELLDIM // 2, yPos + CELLDIM // 2, 
                        (CELLDIM-1)-CELLDIM//CELLMARGIN, (CELLDIM-1)-CELLDIM//CELLMARGIN)
            elif self.number > 0:
                fill(*NUMBERCOLOR)
                textSize(TEXTSIZE)
                textAlign(LEFT)
                text(str(self.number), xPos+2*CELLMARGIN, yPos+CELLDIM-CELLMARGIN)
        elif self.flag:
            fill(*FLAGCOLOR)
            ellipse(xPos + CELLDIM // 2, yPos + CELLDIM // 2, 
                    (CELLDIM-1)-2*CELLDIM//CELLMARGIN, (CELLDIM-1)-2*CELLDIM//CELLMARGIN)
    
    def showHover(self):
        if not self.pressed:
            fill(*CELLCOLORHOVER)
            rect(self.x*CELLDIM+MARGIN,self.y*CELLDIM+MARGIN,CELLDIM,CELLDIM)
            if self.flag:
                xPos, yPos = self.getPos()
                fill(*FLAGCOLOR)
                ellipse(xPos + CELLDIM // 2, yPos + CELLDIM // 2, 
                    (CELLDIM-1)-2*CELLDIM//CELLMARGIN, (CELLDIM-1)-2*CELLDIM//CELLMARGIN)