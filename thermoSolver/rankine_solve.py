from PIL import Image, ImageDraw, ImageFont

def Simple_Rankine_Cycle():
    im = Image.open("/home/arjun/thermoSolver/thermoSolver/Simple_Rankine.png")

    draw = ImageDraw.Draw(im)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("/home/arjun/thermoSolver/thermoSolver/arial.ttf",100)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0),"Sample Text For Testing",(255,255,0),font=font)
    im.save("/home/arjun/thermoSolver/thermoSolver/out.png")
    im1 = Image.open("/home/arjun/thermoSolver/thermoSolver/out.png")
    im1.show()


