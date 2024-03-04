from PIL import Image, ImageOps, ImageFilter
import math

def ImgNegative(img_input, coldepth):
    #solusi 1
    #img_output=ImageOps.invert(img_input)
    #solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgRotate(img_input, coldepth, deg, direction):
    #solusi 1
    # img_output = img_input.rotate(deg)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction == 'C':
                r, g, b = img_input.getpixel((j, img_output.size[0]-i-1))
            elif direction == 'CC':
                r, g, b = img_input.getpixel((img_input.size[1]-j-1, i))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgFlipping(img_input, coldepth, methode):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if methode == "horizontal":
                r,g,b = img_input.getpixel((img_input.size[0]-1-i,j))
            elif methode == "vertikal":
                r,g,b = img_input.getpixel((i,img_input.size[1]-1-j))
            elif methode == "horizontalvertikal":
                r, g, b = img_input.getpixel((img_input.size[0]-1-i, img_input.size[1]-1-j))
            pixels[i,j] = (r,g,b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgTranslasi(img_input, coldepth, methode, n):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixel = img_input.load()
    pixels = img_output.load()

    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):

            r, g, b = img_input.getpixel((i, j))
            r = 0
            g = 0
            b = 0

            if methode == "TX":
                if i <= n:
                    pixels[i,j] = (r,g,b)
                else:
                    pixels[i,j] = pixel[i - n, j]
            elif methode == "TY":
                if j <= n:
                    pixels[i,j] = (r,g,b)
                else:
                    pixels[i,j] = pixel[i, j -n]
            elif methode == "TXY":
                if i <= n:
                    pixels[i,j] = (r,g,b)
                elif j <= n:
                    pixels[i,j] = (r,g,b)
                else:
                    pixels[i,j] = pixel[i - n, j - n]
            else:
                pixels[i,j] = pixel[i, j]
    
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

def ImgThresholding(img_input, coldepth,vT):
    
    if coldepth != 24:
        img_input = img_input.convert('RGB')
        
    img_output = Image.new('RGB',(img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r,g,b = img_input.getpixel((i,j))
            if r and g and b > vT:
                pixels[i,j]=(255,255,255)
            else:
                pixels[i,j] = (0,0,0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgBrightness(img_input, coldepth, vB):

    if coldepth != 24:
        img_input = img_input.convert('RGB')
        
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (vB+r, vB+g, vB+b)
            if pixels[i,j] > (255,255,255):
                pixels[i,j] = (255,255,255)
            elif pixels[i,j] < (0,0,0):
                pixels[i,j] = (0,0,0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgLogarithmic(img_input, coldepth,c):
   
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    img_output = Image.new('RGB',(img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r,g,b = img_input.getpixel((i,j))
            pixels[i,j] = (c*int(math.log(1+r)),c*int(math.log(1+g)),c*int(math.log(1+b)))

    if coldepth ==1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgScalingZoomInOut(img_input,coldepth, scalefactor, methode):
   
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    
    if methode == "zoomout":
        img_output = Image.new('RGB',(int(img_input.size[0]/scalefactor), int(img_input.size[1]/scalefactor)))
    elif methode == "zoomin":
        img_output = Image.new('RGB',(img_input.size[0]*scalefactor, img_input.size[1]*scalefactor))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range (img_output.size[1]):
            if methode == "zoomout":
                r,g,b = img_input.getpixel((i*scalefactor,j*scalefactor))
            elif methode == "zoomin":
                r,g,b = img_input.getpixel((int(i/scalefactor),int(j/scalefactor)))
            pixels[i,j] = (r,g,b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgBlending(img_input, img_input2):
    
    img_width = img_input.size[0] > img_input2.size[0] and img_input.size[0] or img_input2.size[0]
    img_height = img_input.size[1] > img_input2.size[1] and img_input.size[1] or img_input2.size[1]
    img_input = img_input.resize((img_width, img_height))
    img_input2 = img_input2.resize((img_width, img_height))

    img_input = img_input.convert("RGB")
    img_input2 = img_input2.convert("RGB")
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            r2,g2,b2 = img_input2.getpixel((i,j))
            pixels[i, j] = (r+r2, g+g2, b+b2)
            if pixels[i, j] >(255,255,255):
                pixels[i,j]=(255,255,255)
            elif pixels[i, j] < (0,0,0):
                pixels[i,j] = (0,0,0)

    return img_output

def ImgMedianMeanConvolution(img_input, coldepth, methode):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    temp1=[]
    temp2=[]
    temp3=[]
    kernel = 3
    c_kernel=[1,1,1,1,1,1,1,1,1]

    index = kernel // 2
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            for z in range (kernel):
                if i + z - index < 0 or i + z - index > img_input.size[0] - 1:
                    for c in range (kernel):
                        temp1.append(0)
                        temp2.append(0)
                        temp3.append(0)
                else:
                    if j + z - index < 0 or j + index > img_input.size[1] - 1:
                        temp1.append(0)
                        temp2.append(0)
                        temp3.append(0)
                    else:
                        for k in range (kernel):
                            r,g,b = img_input.getpixel((i+z-index,j+k-index))
                            if methode == "konvolusi":
                                temp1.append(r*c_kernel[k])
                                temp2.append(g*c_kernel[k])
                                temp3.append(b*c_kernel[k])
                            else:
                                temp1.append(r)
                                temp2.append(g)
                                temp3.append(b)
            if methode == "median":
                temp1.sort()
                temp2.sort()
                temp3.sort()
                ldata1 = int((len(temp1)+1)/2)
                ldata2 = int((len(temp2)+1)/2)
                ldata3 = int((len(temp3)+1)/2)
                pixels[i,j] = (round(temp1[ldata1-1]), round(temp2[ldata2-1]),round(temp3[ldata3-1]))
                temp1=[]
                temp2=[]
                temp3=[]
            elif methode == "mean":
                pixels[i,j] = (round((sum(temp1))/len(temp1)), round((sum(temp2))/len(temp2)),round((sum(temp3))/len(temp3)))
                temp1=[]
                temp2=[]
                temp3=[]
            elif methode == "konvolusi":
                pixels[i,j] = (round(sum(temp1)/len(c_kernel)), round(sum(temp2)/len(c_kernel)),round(sum(temp3)/len(c_kernel)))
                temp1=[]
                temp2=[]
                temp3=[]
           
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

def ImgEdge(img_input, coldepth, methode):

    if coldepth !=24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    if methode == "sobel":
        kernel = [-1,-2,-1,
                0,0,0,
                1,2,1]
        kernel2=[1,0,-1,
                2,0,-2,
                1,0,-1]
    elif methode == "prewitt":
        kernel = [-1, 0, 1,
                -1, 0, 1,
                -1, 0, 1]
        kernel2=[1, 1, 1,
                0, 0, 0,
                -1, -1, -1]
    elif methode == "canny":
        kernel = [-1, 0, 1,
                -2, 0, 2,
                -1, 0, 1]
        kernel2=[1, 2, 1,
                0, 0, 0,
                -1, -2, -1]
    temp1=[]
    temp2=[]
    temp3=[]
    temp4=[]
    temp5=[]
    temp6=[]
    index = len(kernel)//2
    for i in range (index,img_input.size[0]-index):
        for j in range (index,img_input.size[1]-index):
            dataA = [img_input.getpixel  ((i-1, j-1)),
                    img_input.getpixel  ((i-1, j)),
                    img_input.getpixel  ((i-1, j+1)),
                    img_input.getpixel  ((i, j-1)),
                    img_input.getpixel  ((i,j)),
                    img_input.getpixel  ((i, j+1)),
                    img_input.getpixel  ((i+1, j-1)),
                    img_input.getpixel  ((i+1, j)),
                    img_input.getpixel  ((i+1, j+1))]
            
            r2,g2,b2 = (0,0,0)
            for x in range(8):
                r2,g2,b2 = dataA[x]
                temp1.append(r2*kernel[x])
                temp2.append(g2*kernel[x])
                temp3.append(b2*kernel[x])
                temp4.append(r2*kernel2[x])
                temp5.append(g2*kernel2[x])
                temp6.append(b2*kernel2[x])
            pixels[i,j] = (abs(sum(temp1)+abs(sum(temp4))),abs(sum(temp2)+abs(sum(temp5))),abs(sum(temp3)+abs(sum(temp6))))
            temp1=[]
            temp2=[]
            temp3=[]
            temp4=[]
            temp5=[]
            temp6=[]

    if coldepth ==1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgLaplacian(img_input, coldepth):

    if coldepth !=24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    kernel = [0,1,0,
              1,-4,1,
              0,1,0]
    temp1=[]
    temp2=[]
    temp3=[]
    offset = len(kernel)//2
    for i in range(1, img_input.size[0] - 1):
        for j in range (1,img_input.size[1] -1):
            dataA = [img_input.getpixel  ((i-1, j-1)),
                    img_input.getpixel  ((i-1, j)),
                    img_input.getpixel  ((i-1, j+1)),
                    img_input.getpixel  ((i, j-1)),
                    img_input.getpixel  ((i,j)),
                    img_input.getpixel  ((i, j+1)),
                    img_input.getpixel  ((i+1, j-1)),
                    img_input.getpixel  ((i+1, j)),
                    img_input.getpixel  ((i+1, j+1))]
            
            r2,g2,b2 = (0,0,0)
            for x in range(8):
                r2,g2,b2 = dataA[x]
                temp1.append(r2*kernel[x])
                temp2.append(g2*kernel[x])
                temp3.append(b2*kernel[x])

            pixels[i,j] = (round(sum(temp1)), round(sum(temp2)), round(sum(temp3)))
            temp1=[]
            temp2=[]
            temp3=[]

    if coldepth ==1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgGaussian(img_input, coldepth):

    if coldepth !=24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    kernel = [1,2,1,
              2,4,2,
              1,2,1]
    temp1=[]
    temp2=[]
    temp3=[]
    for i in range(1, img_input.size[0] - 1):
        for j in range (1,img_input.size[1] -1):
            dataA = [img_input.getpixel  ((i-1, j-1)),
                    img_input.getpixel  ((i-1, j)),
                    img_input.getpixel  ((i-1, j+1)),
                    img_input.getpixel  ((i, j-1)),
                    img_input.getpixel  ((i,j)),
                    img_input.getpixel  ((i, j+1)),
                    img_input.getpixel  ((i+1, j-1)),
                    img_input.getpixel  ((i+1, j)),
                    img_input.getpixel  ((i+1, j+1))]
            
            r2,g2,b2 = (0,0,0)
            for x in range(8):
                r2,g2,b2 = dataA[x]
                temp1.append(r2*kernel[x])
                temp2.append(g2*kernel[x])
                temp3.append(b2*kernel[x])

            pixels[i,j] = (round(sum(temp1)/16), round(sum(temp2)/16), round(sum(temp3)/16))
            temp1=[]
            temp2=[]
            temp3=[]

    if coldepth ==1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output



def filter(Mask, konstanta):
    r, g, b = Mask
    r = round (r * konstanta)
    g = round (g * konstanta)
    b = round (b * konstanta)
    MaskBaru = (r, g, b)
    return MaskBaru

def ImgSharpen(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]), "white")
    pixels = img_output.load()
    pixel = img_input.load()
    
    mask = [(0,0)] * 9
    masker = [(0,0)] * 9

    for i in range(1, img_input.size[0] - 1):
        for j in range (1,img_input.size[1] -1):
            r = 0
            g = 0
            b = 0

            mask[0] = img_input.getpixel((i-1,j-1))
            mask[1] = img_input.getpixel((i-1,j))
            mask[2] = img_input.getpixel((i-1,j+1))
            mask[3] = img_input.getpixel((i,j-1))
            mask[4] = img_input.getpixel((i,j))
            mask[5] = img_input.getpixel((i,j+1))
            mask[6] = img_input.getpixel((i+1,j-1))
            mask[7] = img_input.getpixel((i+1,j))
            mask[8] = img_input.getpixel((i+1,j+1))

            for a in range(8):
                if ((a + 1) % 5) == 0:
                    konstanta = 5
                    masker[a] = filter(mask[a], konstanta)
                elif ((a + 1) % 2) == 0:
                    konstanta = (-1)
                    masker[a] = filter(mask[a], konstanta)
                else:
                    konstanta = 0
                    masker[a] = filter(mask[a], konstanta)
                r2,g2,b2 = masker[a]
                r = r + r2
                g = g + g2
                b = b + b2
            pixels[i,j] = (r,g,b)
    
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgMorfologiErosiDilasi(img_input, coldepth,methode):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    temp1=[]
    temp2=[]
    temp3=[]
    kernel = 3

    index = kernel // 2
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            for z in range (kernel):
                if i + z - index < 0 or i + z - index > img_input.size[0] - 1:
                    for c in range (kernel):
                        temp1.append(0)
                        temp2.append(0)
                        temp3.append(0)
                        

                else:
                    if j + z - index < 0 or j + index > img_input.size[1] - 1:
                        temp1.append(0)
                        temp2.append(0)
                        temp3.append(0)

                    else:
                        for k in range (kernel):
                            r,g,b = img_input.getpixel((i+z-index,j+k-index))
                            temp1.append(r)
                            temp2.append(g)
                            temp3.append(b)
            if methode == "erosi":
                pixels[i,j] = (min(temp1),min(temp2),min(temp3))
            elif methode == "dilasi":
                pixels[i,j] = (max(temp1),max(temp2),max(temp3))
            temp1=[]
            temp2=[]
            temp3=[]
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

def ImgOpeningClosing(img_input, coldepth,methode):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output_sementara = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixelsementara = img_output_sementara.load()
    pixels = img_output.load()
    temp1=[]
    temp2=[]
    temp3=[]
    kernel = 3

    index = kernel // 2
    
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            for z in range (kernel):
                if i + z - index < 0 or i + z - index > img_input.size[0] - 1:
                    for c in range (kernel):
                        temp1.append(0)
                        temp2.append(0)
                        temp3.append(0)
                else:
                    if j + z - index < 0 or j + index > img_input.size[1] - 1:
                        temp1.append(0)
                        temp2.append(0)
                        temp3.append(0)
                    else:
                        for k in range (kernel):
                            r,g,b = img_input.getpixel((i+z-index,j+k-index))
                            temp1.append(r)
                            temp2.append(g)
                            temp3.append(b)
            
            if methode == "open":
                pixelsementara[i,j] = (max(temp1) ,max(temp2),max(temp3))
            elif methode == "close":
                pixelsementara[i,j] = (min(temp1) ,min(temp2),min(temp3))
            temp1=[]
            temp2=[]
            temp3=[]

    for i in range(img_output_sementara.size[0]):
        for j in range(img_output_sementara.size[1]):
            for z in range (kernel):
                if i + z - index < 0 or i + z - index > img_input.size[0] - 1:
                    for c in range (kernel):
                        temp1.append(0)
                        temp2.append(0)
                        temp3.append(0)
                else:
                    if j + z - index < 0 or j + index > img_input.size[1] - 1:
                        temp1.append(0)
                        temp2.append(0)
                        temp3.append(0)
                    else:
                        for k in range (kernel):
                            r,g,b = img_output_sementara.getpixel((i+z-index,j+k-index))
                            temp1.append(r)
                            temp2.append(g)
                            temp3.append(b)
            if methode == "open":
                pixels[i,j] = (min(temp1),min(temp2),min(temp3))
            elif methode == "close":
                pixels[i,j] = (max(temp1),max(temp2),max(temp3))
            temp1=[]
            temp2=[]
            temp3=[]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def RGBtoGrayscalehsl(img_input, coldepth, methode):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    

    for i in range(1, img_input.size[0] - 1):
        for j in range(1, img_input.size[1] - 1):
            r, g, b = img_input.getpixel((i, j))

            if methode == "grayscale":
                r2 = r * 0.2989
                g2 = g * 0.5870
                b2 = b * 0.1140
                gray = round(r2 + g2 + b2)
                pixels[i,j] = (gray,gray,gray)
            elif methode == "hsl":
                r, g, b = r / 255.0, g / 255.0, b / 255.0
            
                cmax = max(r, g, b)
                cmin = min(r, g, b)
                diff = cmax-cmin
            
                if cmax == cmin:
                    h = 0
                elif cmax == r:
                    h = (60 * ((g - b) / diff) + 360) % 360
                elif cmax == g:
                    h = (60 * ((b - r) / diff) + 120) % 360
                elif cmax == b:
                    h = (60 * ((r - g) / diff) + 240) % 360
                if cmax == 0:
                    s = 0
                else:
                    s = (diff / cmax) * 100
                v = cmax * 100

                pixels[i,j] = (round(h),round(s),round(v))


    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


