def Morphology3(img_input, coldepth, methode):
    img_input.convert('L')

    if methode == "TopHat": 
        img_morphology1 = ImgOpeningClosing(img_input, coldepth, "open")
        # img_morphology1.show()
    elif methode == "BottomHat": 
        img_morphology1 = ImgOpeningClosing(img_input, coldepth, "close")
        # img_morphology1.show()
    
    row = int(img_input.size[0])
    col = int(img_input.size[1])
    img_output = Image.new('L', (row, col))
    print(row)
    print(col)
    mask = [(0,0)] * 9
    mask_pure = [(0,0)] * 9
    singlePixel = [(0,0)] * 9
    for i in range(row-1):
        for j in range(col-1):
            
            mask_pure[0] = img_input.getpixel((i-1, j-1))
            mask_pure[1] = img_input.getpixel((i-1, j))
            mask_pure[2] = img_input.getpixel((i-1, j+1))
            mask_pure[3] = img_input.getpixel((i, j-1))
            mask_pure[4] = img_input.getpixel((i, j))
            mask_pure[5] = img_input.getpixel((i, j+1))
            mask_pure[6] = img_input.getpixel((i+1, j-1))
            mask_pure[7] = img_input.getpixel((i+1, j))
            mask_pure[8] = img_input.getpixel((i+1, j+1)) 
            
            
            mask[0] = img_morphology1.getpixel((i-1, j-1))
            mask[1] = img_morphology1.getpixel((i-1, j))
            mask[2] = img_morphology1.getpixel((i-1, j+1))
            mask[3] = img_morphology1.getpixel((i, j-1))
            mask[4] = img_morphology1.getpixel((i, j))
            mask[5] = img_morphology1.getpixel((i, j+1))
            mask[6] = img_morphology1.getpixel((i+1, j-1))
            mask[7] = img_morphology1.getpixel((i+1, j))
            mask[8] = img_morphology1.getpixel((i+1, j+1)) 

            for k in range(9):
                singlePixel[k] = mask[k][0]
                # print(singlePixel[k])
                
            if methode == "TopHat":
                for t in range(8):
                    img_output.putpixel((i, j),(mask_pure[t][0] - singlePixel[t]))
            elif methode == "BottomHat":
                for t in range(8):
                    img_output.putpixel((i, j),(singlePixel[t] - mask_pure[t][0]))
            
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
                
    return img_output




# temp4=[]
    # temp5=[]
    # temp6=[]
    # vT = 100


# c_kernel1=[-1,-2,-1,0,0,0,1,2,1]
    # c_kernel2=[1,0,-1,2,0,-2,1,0,-1]

# elif methode == "edge":
                            #     temp1.append(r*c_kernel1[k])
                            #     temp2.append(g*c_kernel1[k])
                            #     temp3.append(b*c_kernel1[k])
                            #     temp4.append(r*c_kernel2[k])
                            #     temp5.append(g*c_kernel2[k])
                            #     temp6.append(b*c_kernel2[k])

                             # elif methode == "edge":

            #     r2,g2,b2 = ((abs(sum(temp1))+abs(sum(temp4))),(abs(sum(temp2))+abs(sum(temp5))),(abs(sum(temp3))+abs(sum(temp6))))
            #     temp1=[]
            #     temp2=[]
            #     temp3=[]
            #     temp4=[]
            #     temp5=[]
            #     temp6=[]


def pembantuBagiFilter(Mask, konstanta):
    r, g, b = Mask
    r = round (r * konstanta / 9)
    g = round (g * konstanta / 9)
    b = round (b * konstanta / 9)
    MaskBaru = (r, g, b)
    return MaskBaru





def divFilterPlus(Mask, konstanta):
    r, g, b = Mask
    r = round (r * konstanta)
    g = round (g * konstanta)
    b = round (b * konstanta)
    MaskBaru = (r, g, b)
    return MaskBaru

def ImgEdge(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]), "white")
    pixels = img_output.load()
    
    mask = [(0,0)] * 9
    masker = [(0,0)] * 9

    for i in range(1, img_input.size[0] - 1):
        for j in range(1, img_input.size[1] - 1):
            r2 = 0
            g2 = 0
            b2 = 0

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
                if (a + 1) == 4 | 5 | 6:
                    konstanta = 0
                    masker[a] = divFilterPlus(mask[a], konstanta)
                elif (a + 1) == 1 | 3:
                    konstanta = (-1)
                    masker[a] = divFilterPlus(mask[a], konstanta)
                elif (a + 1) == 2:
                    konstanta = (-2)
                    masker[a] = divFilterPlus(mask[a], konstanta)
                elif (a + 1) == 8:
                    konstanta = 2
                    masker[a] = divFilterPlus(mask[a], konstanta)
                elif (a + 1) == 7 | 9:
                    konstanta = 1
                    masker[a] = divFilterPlus(mask[a], konstanta)
                r,g,b = masker[a]
                r2 = r2 + r
                g2 = g2 + g
                b2 = b2 + b
            pixels[i,j] = (r2,g2,b2)
            
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output







def ImgEdge(img_input, coldepth):
    
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixel = img_output.load()
    mask = [(0,0)] * 9
    r = [(0,0)] * 9
    g = [(0,0)] * 9
    b = [(0,0)] * 9
    
    for i in range(1, img_input.size[0] - 1):
        for j in range(1, img_input.size[1] - 1):
            r2 = 0
            g2 = 0
            b2 = 0
            mask[0] = img_input.getpixel((i-1,j-1))
            mask[1] = img_input.getpixel((i-1,j))
            mask[2] = img_input.getpixel((i-1,j+1))
            mask[3] = img_input.getpixel((i,j-1))
            mask[4] = img_input.getpixel((i,j))
            mask[5] = img_input.getpixel((i,j+1))
            mask[6] = img_input.getpixel((i+1,j-1))
            mask[7] = img_input.getpixel((i+1,j))
            mask[8] = img_input.getpixel((i+1,j+1))
            
            
            for k in range(8): 
                r[k], g[k], b[k] = mask[k]
                
                if (k + 1) == 1 or (k + 1) == 3:
                    const = (-1)
                    r[k] = int(r[k] * const)
                    g[k] = int(g[k] * const)
                    b[k] = int(b[k] * const)
                    
                elif (k + 1) == 2:
                    const = -2
                    r[k] = int(r[k] * const)
                    g[k] = int(g[k] * const)
                    b[k] = int(b[k] * const)
                    
                elif (k + 1) == 4 or (k + 1) == 5 or (k + 1) == 6:
                    const = 0
                    r[k] = int(r[k] * const)
                    g[k] = int(g[k] * const)
                    b[k] = int(b[k] * const)
                    
                elif (k + 1) == 7 or (k + 1) == 9:
                    const = 1
                    r[k] = int(r[k] * const)
                    g[k] = int(g[k] * const)
                    b[k] = int(b[k] * const)   
                
                elif (k + 1) == 8:
                    const = 2
                    r[k] = int(r[k] * const)
                    g[k] = int(g[k] * const)
                    b[k] = int(b[k] * const)  
                 
                r2 = r2 + r[k]
                g2 = g2 + g[k]
                b2 = b2 + b[k]

            pixel[i,j] = (r2, g2, b2)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
        
    return img_output



























def ImgFilter(img_input, coldepth, n):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]), "white")
    pixels = img_output.load()
    pixel = img_input.load()
    
    mask = [(0,0)] * 9
    masker = [(0,0)] * 9
    

    for i in range(1, img_input.size[0] - 1):
        for j in range(1, img_input.size[1] - 1):
            _Rahmat = 0
            _Gah = 0
            _Bahaduri = 0

            mask[0] = img_input.getpixel((i-1,j-1))
            mask[1] = img_input.getpixel((i-1,j))
            mask[2] = img_input.getpixel((i-1,j+1))
            mask[3] = img_input.getpixel((i,j-1))
            mask[4] = img_input.getpixel((i,j))
            mask[5] = img_input.getpixel((i,j+1))
            mask[6] = img_input.getpixel((i+1,j-1))
            mask[7] = img_input.getpixel((i+1,j))
            mask[8] = img_input.getpixel((i+1,j+1))
            
            
            if n == "Mean":
                for a in range(8):
                    konstanta = 1
                    masker[a] = pembantuBagiFilter(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

            elif n == "WeightMean":
                for a in range(8):
                    if ((a + 1) % 5) == 0:
                        konstanta = 4
                        masker[a] = pembantuBagiFilterWeight(mask[a], konstanta)
                    elif ((a + 1) % 2) == 0:
                        konstanta = 2
                        masker[a] = pembantuBagiFilterWeight(mask[a], konstanta)
                    else:
                        konstanta = 1
                        masker[a] = pembantuBagiFilterWeight(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

            elif n == "Sharpen":
                for a in range(8):
                    if ((a + 1) % 5) == 0:
                        konstanta = 5
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif ((a + 1) % 2) == 0:
                        konstanta = (-1)
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    else:
                        konstanta = 0
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

            elif n == "Laplacian":
                for a in range(8):
                    if ((a + 1) % 5) == 0:
                        konstanta = (-4)
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif ((a + 1) % 2) == 0:
                        konstanta = 1
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    else:
                        konstanta = 0
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

            elif n == "Edge":
                for a in range(8):
                    if (a + 1) == 4 | 5 | 6:
                        konstanta = 0
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif (a + 1) == 1 | 3:
                        konstanta = (-1)
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif (a + 1) == 2:
                        konstanta = (-2)
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif (a + 1) == 8:
                        konstanta = 2
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif (a + 1) == 7 | 9:
                        konstanta = 1
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

                
            elif n == "Median":
                mask.sort()
                r, g, b = mask[4]
                pixels[i,j] = (r,g,b)

            elif n == "Max":
                mask.sort()
                r, g, b = mask[8]
                pixels[i,j] = (r,g,b)

            elif n == "Min":
                mask.sort()
                r, g, b = mask[0]
                pixels[i,j] = (r,g,b)

            else:
                pixels[i,j] = pixel[i,j]



    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output




def pembantuBagiFilter(Mask, konstanta):
    r, g, b = Mask
    r = round (r * konstanta / 9)
    g = round (g * konstanta / 9)
    b = round (b * konstanta / 9)
    MaskBaru = (r, g, b)
    return MaskBaru

def pembantuBagiFilterWeight(Mask, konstanta):
    r, g, b = Mask
    r = round ((r * konstanta) / 16)
    g = round ((g * konstanta) / 16)
    b = round ((b * konstanta) / 16)
    MaskBaru = (r, g, b)
    return MaskBaru

def pembantuBagiFilterplus(Mask, konstanta):
    r, g, b = Mask
    r = round (r * konstanta)
    g = round (g * konstanta)
    b = round (b * konstanta)
    MaskBaru = (r, g, b)
    return MaskBaru



def ImgFilter(img_input, coldepth, n):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]), "white")
    pixels = img_output.load()
    pixel = img_input.load()
    
    mask = [(0,0)] * 9
    masker = [(0,0)] * 9
    

    for i in range(1, img_input.size[0] - 1):
        for j in range(1, img_input.size[1] - 1):
            _Rahmat = 0
            _Gah = 0
            _Bahaduri = 0

            mask[0] = img_input.getpixel((i-1,j-1))
            mask[1] = img_input.getpixel((i-1,j))
            mask[2] = img_input.getpixel((i-1,j+1))
            mask[3] = img_input.getpixel((i,j-1))
            mask[4] = img_input.getpixel((i,j))
            mask[5] = img_input.getpixel((i,j+1))
            mask[6] = img_input.getpixel((i+1,j-1))
            mask[7] = img_input.getpixel((i+1,j))
            mask[8] = img_input.getpixel((i+1,j+1))
            
            
            if n == "Mean":
                for a in range(8):
                    konstanta = 1
                    masker[a] = pembantuBagiFilter(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

            elif n == "WeightMean":
                for a in range(8):
                    if ((a + 1) % 5) == 0:
                        konstanta = 4
                        masker[a] = pembantuBagiFilterWeight(mask[a], konstanta)
                    elif ((a + 1) % 2) == 0:
                        konstanta = 2
                        masker[a] = pembantuBagiFilterWeight(mask[a], konstanta)
                    else:
                        konstanta = 1
                        masker[a] = pembantuBagiFilterWeight(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

            elif n == "Sharpen":
                for a in range(8):
                    if ((a + 1) % 5) == 0:
                        konstanta = 5
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif ((a + 1) % 2) == 0:
                        konstanta = (-1)
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    else:
                        konstanta = 0
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

            elif n == "Laplacian":
                for a in range(8):
                    if ((a + 1) % 5) == 0:
                        konstanta = (-4)
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif ((a + 1) % 2) == 0:
                        konstanta = 1
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    else:
                        konstanta = 0
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

            elif n == "Edge":
                for a in range(8):
                    if (a + 1) == 4 | 5 | 6:
                        konstanta = 0
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif (a + 1) == 1 | 3:
                        konstanta = (-1)
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif (a + 1) == 2:
                        konstanta = (-2)
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif (a + 1) == 8:
                        konstanta = 2
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    elif (a + 1) == 7 | 9:
                        konstanta = 1
                        masker[a] = pembantuBagiFilterplus(mask[a], konstanta)
                    r,g,b = masker[a]
                    _Rahmat = _Rahmat + r
                    _Gah = _Gah + g
                    _Bahaduri = _Bahaduri + b
                pixels[i,j] = (_Rahmat,_Gah,_Bahaduri)

                
            elif n == "Median":
                mask.sort()
                r, g, b = mask[4]
                pixels[i,j] = (r,g,b)

            elif n == "Max":
                mask.sort()
                r, g, b = mask[8]
                pixels[i,j] = (r,g,b)

            elif n == "Min":
                mask.sort()
                r, g, b = mask[0]
                pixels[i,j] = (r,g,b)

            else:
                pixels[i,j] = pixel[i,j]



    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


    # def ImgEdgeGausianSmoothBlur(img_input,coldepth,methode):
#     if coldepth !=24:
#         img_input = img_input.convert('RGB')
    
#     img_width = img_input.size[0]
#     img_height = img_input.size[1]
#     img_input = img_input.resize((img_width, img_height))
#     img_input = img_input.convert("RGB")
#     if methode == "edge":
#         img_output = img_input.filter(ImageFilter.FIND_EDGES)
#     elif methode == "gausian":
#         img_output = img_input.filter(ImageFilter.GaussianBlur(radius=2))
#     elif methode == "smooth":
#         img_output = img_input.filter(ImageFilter.SMOOTH)
#     elif methode == "blur":
#         img_output = img_input.filter(ImageFilter.BLUR)

#     if coldepth ==1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")

#     return img_output




# def ImgOpeningClosing(img_input, coldepth, methode):

#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     img_output_temp = Image.new('RGB', (img_input.size[0], img_input.size[1]))
#     img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
#     pixel_temp = img_output_temp.load()
#     pixels = img_output.load()

#     mask = [(0,0)] * 9
    
#     for i in range(1, img_input.size[0] - 1):
#         for j in range(1, img_input.size[1] - 1):
#             mask[0] = img_input.getpixel((i-1,j-1))
#             mask[1] = img_input.getpixel((i-1,j))
#             mask[2] = img_input.getpixel((i-1,j+1))
#             mask[3] = img_input.getpixel((i,j-1))
#             mask[4] = img_input.getpixel((i,j))
#             mask[5] = img_input.getpixel((i,j+1))
#             mask[6] = img_input.getpixel((i+1,j-1))
#             mask[7] = img_input.getpixel((i+1,j))
#             mask[8] = img_input.getpixel((i+1,j+1))
            
#             mask.sort()
#             if methode == "open":
#                 r, g, b = mask[8]
#             elif methode == "close":
#                 r, g, b = mask[0]
#             pixel_temp[i,j] = (r,g,b)

#     for i in range(1, img_output_temp.size[0] - 1):
#         for j in range(1, img_output_temp.size[1] - 1):

#             mask[0] = img_output_temp.getpixel((i-1,j-1))
#             mask[1] = img_output_temp.getpixel((i-1,j))
#             mask[2] = img_output_temp.getpixel((i-1,j+1))
#             mask[3] = img_output_temp.getpixel((i,j-1))
#             mask[4] = img_output_temp.getpixel((i,j))
#             mask[5] = img_output_temp.getpixel((i,j+1))
#             mask[6] = img_output_temp.getpixel((i+1,j-1))
#             mask[7] = img_output_temp.getpixel((i+1,j))
#             mask[8] = img_output_temp.getpixel((i+1,j+1))
            
#             mask.sort()
#             if methode == "open":
#                 r, g, b = mask[0]
#             elif methode == "close":
#                 r, g, b, = mask[8]
#             pixels[i,j] = (r,g,b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")

#     return img_output

# def ImgMorfologiErosiDilasi(img_input, coldepth, methode):
#     img_input = img_input.convert('L')
#     T =50
#     img_output = Image.new('L',(img_input.size[0], img_input.size[1]))
#     pixels = img_output.load()

#     kernel = [255,255,255,
#               255,255,255,
#               255,255,255]  

#     offset = len(kernel)//2
#     for i in range (offset,img_input.size[0]-offset):
#         for j in range (offset,img_input.size[1]-offset):
#             dataA = [img_input.getpixel  ((i-1, j-1)),
#                     img_input.getpixel  ((i-1, j)),
#                     img_input.getpixel  ((i-1, j+1)),
#                     img_input.getpixel  ((i, j-1)),
#                     img_input.getpixel  ((i,j)),
#                     img_input.getpixel  ((i, j+1)),
#                     img_input.getpixel  ((i+1, j-1)),
#                     img_input.getpixel  ((i+1, j)),
#                     img_input.getpixel  ((i+1, j+1))]
            
#             if methode == "erosi":
#                 pixels[i,j] = min(dataA)
#             elif methode == "dilasi":
#                 pixels[i,j] = max(dataA)         

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")

#     return img_output

# baru