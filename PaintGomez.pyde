def setup():
    size(1920,1080)
    background(255)
    fill(255,0,0)
    rect(0,0,50,30)
    fill(0,0,255)
    rect(50,0,50,30)
    fill(0,255,0)
    rect(100, 0, 50, 30)
    fill(255, 192, 203)
    rect(150 , 0, 50, 30)
    

    fill(255)
    rect(200, 0, 50, 30)
    
def draw():
    if mouseButton and mouseY < 30:
        if mouseX < 50:
           fill(255,0,0)
        elif mouseX < 100:
           fill(0,0,255)
        elif mouseX < 150:
            fill(0,255,0)
        elif mouseX < 200:
            fill(255,192,203)
        elif mouseX < 250:
            fill(random(255),random(255),random(255))
   
    elif mouseButton and mouseY > 30:
        noStroke()
        ellipse(mouseX, mouseY, 10,10)
