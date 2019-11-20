## 验证码的几种方式


### 1. 方式1：读指定的图片

    views.py的内容
    def get_valid_img(request):
        with open("static/img/valid.jpg", "rb") as f:
          data = f.read()
        return HttpResponse(data)

    loin.html的内容（/get_valid_img/）：
      <img src="/get_valid_img/" alt="验证码" width="200px" height=40px" id="img">

### 2. 方式2：基于PIL模块创建验证码图片

1. pip install pillow
2. 在views.py上面导入pillow
   
        from PIL import Image

   
   
3.  views.py的内容
   
          img = Image.new("RGB", (350, 46), color='red')

          #生成valid.png图片
          f = open("valid.png", "wb")
          img.save(f, "png")
          print("OK,sir")

        #将图片渲染到前端页面
         with open("valid.png","rb") as f:
          data = f.read()
        return HttpResponse(data)

### 3. 方式3：内存方式读取验证码

    from io import BytesIO
    def get_random_color():
        import random
        return(random.randint(0, 255), random.randint(0,255), random.randint(0,255) )
    img = Image.new("RGB",(300,38),get_random_color())
    f = BytesIO()
    img.save(f,"png")
    data = f.getvalue()

    return HttpResponse(data)

### 4. 方式4，：在3的基础上完善文本

    from PIL import Image,ImageDraw,ImageFont
    from io import BytesIO
    import random
    def get_random_image():
        pass
        return(random.randint(0,255),random.randint(0,255),random.randint(0,255),)
    img = Image.new("RGB",(200,38),get_random_image())
    word = random.randint(10000, 99999)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font='static/fonts/Alibaba-PuHuiTi-Bold.ttf',size=24)
    draw.text((50,0),str(word),get_random_image(),font=font)
    f = BytesIO()
    img.save(f,"png")
    data = f.getvalue()
    return HttpResponse(data)


### 5. 方式5，：在4的基础上完善随机验证码

from PIL import Image,ImageDraw,ImageFont
    from io import BytesIO
    import random
    def get_random_image():
        pass
        return(random.randint(0,255),random.randint(0,255),random.randint(0,255),)
    img = Image.new("RGB",(200,38),get_random_image())
    word = random.randint(10000, 99999)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font='static/fonts/Alibaba-PuHuiTi-Bold.ttf', size=24)
    
    #增加了这一部分，随机大小写、数字验证码
    for i in range(6):
        random_num = str(random.randint(0,9))
        random_lowcase = chr(random.randint(97,122))
        random_upcase = chr(random.randint(65,90))
        random_word = random.choice([random_num,random_lowcase,random_upcase])
        draw.text((i*20+50,0),random_word,get_random_image(),font=font)


    f = BytesIO()
    img.save(f,"png")
    data = f.getvalue()
    return HttpResponse(data)

### 这是加噪点的（在上面的for in range最后加）

        #width和height不能超过img = Image.new("RGB",(200,38)里的值
        width=350
        height=38
        for i in range(100):
            x1=random.randint(0,width)
            x2=random.randint(0,width)
            y1=random.randint(0,height)
            y2=random.randint(0,height)
            draw.line((x1,y1,x2,y2),fill=get_random_color())

        for i in range(500):
            draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())





