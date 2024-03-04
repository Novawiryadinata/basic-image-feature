import PySimpleGUI as sg 
import os.path 
from PIL import Image, ImageOps
from processing_list import *

sg.theme('DarkTeal9')
# Kolom Area No 1: Area open folder and select image 
for_image = 1
file_list_column = [
    [ 
        sg.Text("Open Image Folder :"), 
    ],
    [ 
        sg.In(size=(20, 1), enable_events=True, key="ImgFolder"), 
        sg.FolderBrowse(), 
    ],
    [ 
        sg.Text("Choose an image from list :" + str(for_image), key="ImgSelector"), 
    ],
    [
        sg.Button("Change", size=(15,1), key = "SelectFor"),
    ],
    [ 
        sg.Listbox( 
        values=[], enable_events=True, size=(18, 20), key="ImgList" 
        ) 
    ],
]

# Kolom Area No 2: Area viewer image input 
image_viewer_column2row1 = [ 
    [sg.Text("Image Input 1")], 
    [sg.Text(size=(40, 1), key="FilepathImgInput")], 
    [sg.Image(key="ImgInputViewer")], 
]

image_viewer_column2row2 = [ 
    [sg.Text("Image Input 2:")], 
    [sg.Text(size=(40, 1), key="FilepathImgInput2")], 
    [sg.Image(key="ImgInputViewer2")], 
]

# Kolom Area No 3: Area Image info dan Tombol list of processing 
list_processing = [ 
    [ 
        sg.Text("Image Information:"), 
    ],
    [ 
        sg.Text(size=(20, 1), key="ImgSize"), 
    ], 
    [ 
        sg.Text(size=(20, 1), key="ImgColorDepth"), 
    ],
    [ 
        sg.Text("List of Processing:"), 
    ],
    [ 
        sg.Button("Image Negative", size=(20, 1), key="ImgNegative"), 
    ],
    [ 
        sg.Text("Image Rotate"), 
    ],
    [ 
        sg.Button("CCW", size=(9,1), key="ImgRotateCcw"), 
        sg.Button("CW", size=(9,1), key="ImgRotate"),
    ],
    [ 
        sg.Text("Image Flipping & Translasi"), 
    ],
    [ 
        sg.Button("H", size=(5,1), key="ImgFlippingH"), 
        sg.Button("V", size=(5,1), key="ImgFlippingV"),
        sg.Button("HV", size=(5,1), key="ImgFlippingHV"),
    ],
    [ 
        sg.Button("X", size=(3,1), key="Imgtx"), 
        sg.Button("Y", size=(3,1), key="Imgty"),
        sg.Button("XY", size=(3,1), key="Imgtxy"),
        sg.Input("0", key="TextTargetTranslasi", visible=True, size=(4, 1)),
    ],
    [ 
        sg.Text("Image Scaling"), 
    ],
    [
        sg.Button("Zoom In", size=(9,1), key="ImgZoomIn"),
        sg.Button("Zoom Out", size=(9,1), key="ImgZoomOut"),
    ],
    [
        sg.Button("Image Thresholding", size=(20,1), key="ImgThresholding"),
    ],
    [
        sg.Slider(orientation = 'horizontal', key = 'SliderTargetThreshold', range = (0,255), visible=True)
    ],
    [
        sg.Button("Image Brightness", size=(20,1), key="ImgBrightness"),
    ],
    [
        sg.Slider(orientation = 'horizontal', key = 'SliderTargetBright', range = (0,255), visible=True)
    ],
    [
        sg.Button("Image Logarithmic", size=(20,1), key="ImgLogarithmic"),
    ],
    [
        sg.Slider(orientation = 'horizontal', key = 'SliderTargetLog', range = (0,255), visible=True)
    ],
    [
        sg.Button("Image Blending", size=(20,1), key="ImgBlending"),
    ],
    [
        sg.Button("Median", size=(9,1), key="ImgMedian"),
        sg.Button("Mean", size=(9,1), key="ImgMean"),
    ],
    [
        sg.Button("Image Konvolusi", size=(20,1), key="ImgKonvolusi"),
    ],
    [
        sg.Button("Sobel", size=(9,1), key="ImgEdgeSobel"),
        sg.Button("Laplacian", size=(9,1), key="ImgLaplacial"),
    ],
    [
        sg.Button("Prewitt", size=(9,1), key="ImgEdgePrewitt"),
        sg.Button("Canny", size=(9,1), key="ImgEdgeCanny"),
    ],
    [
        sg.Button("Gaussian", size=(9,1), key="ImgGaussian"),
        sg.Button("Sharpen", size=(9,1), key="ImgSharpen"),
    ],
    [
        sg.Button("Erosi", size=(9,1), key="ImgErosi"),
        sg.Button("Dilasi", size=(9,1), key="ImgDilasi"),
    ],
    [
        
        sg.Button("Opening", size=(9,1), key="ImgOpening"),
        sg.Button("Closing", size=(9,1), key="ImgClosing"),
    ],
    [
        
        sg.Button("Grayscale", size=(9,1), key="ImgGrayscale"),
        sg.Button("HSL", size=(9,1), key="ImgHSL"),
    ],
]

# Kolom Area No 4: Area viewer image output 
image_viewer_column3 = [ 
    [sg.Text("Image Processing Output:")], 
    [sg.Text(size=(40, 1), key="ImgProcessingType")], 
    [sg.Image(key="ImgOutputViewer")], 
]

input = [
    [sg.Column(image_viewer_column2row1)],
    [sg.Text("_" * 40)],
    [sg.Column(image_viewer_column2row2, key="blend", visible=False)],
]

# Gabung Full layout 
layout = [ 
    [ 
        sg.Column(file_list_column), 
        sg.VSeperator(), 
        sg.Column(input), 
        sg.VSeperator(), 
        sg.Column(list_processing), 
        sg.VSeperator(), 
        sg.Column(image_viewer_column3), 
    ] 
]

window = sg.Window("Mini Image Editor", layout,resizable=True,finalize=True)

#nama image file temporary setiap kali processing output 
filename_out = "out.png"

# Run the Event Loop 
while True: 
    event, values = window.read() 
    if event == "Exit" or event == sg.WIN_CLOSED: break 
    
    # Folder name was filled in, make a list of files in the folder 
    if event == "ImgFolder":
        folder = values["ImgFolder"]
            
        try: 
            # Get list of files in folder 
            file_list = os.listdir(folder) 
        except: 
                    file_list = [] 
        fnames = [ 
            f 
            for f in file_list 
            if os.path.isfile(os.path.join(folder, f)) 
            and f.lower().endswith((".png",".jpg", ".gif")) 
        ] 
        
        window["ImgList"].update(fnames)
    
    elif event == "SelectFor":
        for_image = for_image == 2 and 1 or 2
        window["ImgSelector"].update("Choose an image from list for image " + str(for_image))

    elif event == "ImgList": # A file was chosen from the listbox 
        try: 
            filename = os.path.join( 
            values["ImgFolder"], values["ImgList"][0] 
            )
            if for_image == 1: 
                window["FilepathImgInput"].update(filename)
                window["ImgInputViewer"].update(filename=filename) 
                window["ImgProcessingType"].update(filename) 
                window["ImgOutputViewer"].update(filename=filename) 
                img_input = Image.open(filename) 
                #img_input.show() 
                
                #Size 
                img_width, img_height = img_input.size 
                window["ImgSize"].update("Image Size : "+str(img_width)+" x "+str(img_height)) 
                
                #Color depth 
                mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 
                24, "HSV": 24, "I": 32, "F": 32} 
                coldepth = mode_to_coldepth[img_input.mode] 
                window["ImgColorDepth"].update("Color Depth : "+str(coldepth))
            else:
                window["FilepathImgInput2"].update(filename)
                window["ImgInputViewer2"].update(filename=filename)
                img_input2 = Image.open(filename)
                window["blend"].update(visible=True)
        except: 
            pass

    elif event == "ImgNegative": 
 
        try:

            window["ImgProcessingType"].update("Image Negative") 
            img_output=ImgNegative(img_input,coldepth) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
            
            window["blend"].update(visible=False)

        except: 
            pass

    elif event == "ImgRotate":
        
        try:

            window["ImgProcessingType"].update("Image Rotate Clockwise")
            img_output=ImgRotate(img_input,coldepth,90,"C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
            
        except:
            pass

    elif event == "ImgRotateCcw":
        try:

            window["ImgProcessingType"].update("Image Rotate Counterclockwise")
            img_output=ImgRotate(img_input,coldepth,-90,"CC")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
            
        except:
            pass

    elif event == "ImgFlippingH":
        try:
            window["ImgProcessingType"].update("Image Flipping Horizontal")
            img_output=ImgFlipping(img_input, coldepth, "horizontal")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
            
        except:
            pass

    elif event == "ImgFlippingV":
        try:

            window["ImgProcessingType"].update("Image Flipping Vertikal")
            img_output=ImgFlipping(img_input, coldepth, "vertikal")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
            
        except:
            pass

    elif event == "ImgFlippingHV":
        try:

            window["ImgProcessingType"].update("Image Flipping Horizontal + Vertikal")
            img_output=ImgFlipping(img_input, coldepth, "horizontalvertikal")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
            
        except:
            pass
    
    elif event == "Imgtx":
        try:
            n = int(values["TextTargetTranslasi"])
            window["ImgProcessingType"].update("Image Translasi Sumbu X")
            img_output=ImgTranslasi(img_input, coldepth,"TX",n)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            
            window["blend"].update(visible=False)
        except:
            pass
    
    elif event == "Imgty":
        try:
            n = int(values["TextTargetTranslasi"])
            window["ImgProcessingType"].update("Image Translasi Sumbu Y")
            img_output=ImgTranslasi(img_input, coldepth,"TY",n)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            
            window["blend"].update(visible=False)
        except:
            pass
        
    elif event == "Imgtxy":
        try:
            n = int(values["TextTargetTranslasi"])
            window["ImgProcessingType"].update("Image Translasi Sumbu X dan Y")
            img_output=ImgTranslasi(img_input, coldepth,"TXY",n)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            
            window["blend"].update(visible=False)
        except:
            pass

    elif event == "ImgThresholding":
        
        try:

            vT = int(values["SliderTargetThreshold"])
            window["ImgProcessingType"].update("Image Thresholding")
            img_output=ImgThresholding(img_input,coldepth,vT)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
            
        except:
            pass

    elif event == "ImgBrightness": 
 
        try:

            vB = int(values["SliderTargetBright"])
            window["ImgProcessingType"].update("Image Brightness") 
            img_output=ImgBrightness(img_input,coldepth,vB) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out)
            window["blend"].update(visible=False)
            
        except: 
            pass

    elif event == "ImgLogarithmic":

        try:
            c = int(values["SliderTargetLog"])
            window["ImgProcessingType"].update("Image Logarithmic")
            img_output=ImgLogarithmic(img_input,coldepth,c)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
            
        except:
            pass

    elif event == "ImgZoomIn":
        try:

            window["ImgProcessingType"].update("Image Zoom In")
            img_output=ImgScalingZoomInOut(img_input, coldepth, 2, "zoomin")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        
        except:
            pass
    
    elif event == "ImgZoomOut":
        try:
            window["ImgProcessingType"].update("Image Zoom Out")
            img_output=ImgScalingZoomInOut(img_input, coldepth, 2, "zoomout")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        
        except:
            pass

    elif event == "ImgBlending":
        try:

            window["ImgProcessingType"].update("Image Blending")
            img_output=ImgBlending(img_input, img_input2)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=True)
        except:
            pass

    elif event == "ImgMedian":
        try:

            window["ImgProcessingType"].update("Image Median")
            img_output=ImgMedianMeanConvolution(img_input, coldepth,"median")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass
    
    elif event == "ImgMean":
        try:

            window["ImgProcessingType"].update("Image Mean")
            img_output=ImgMedianMeanConvolution(img_input, coldepth, "mean")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass

    elif event == "ImgKonvolusi":
        try:

            window["ImgProcessingType"].update("Image Konvolusi")
            img_output=ImgMedianMeanConvolution(img_input, coldepth, "konvolusi")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass
    elif event == "ImgEdgeSobel":
        try:

            window["ImgProcessingType"].update("Image Sobel")
            img_output=ImgEdge(img_input, coldepth, "sobel")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass

    elif event == "ImgEdgePrewitt":
        try:

            window["ImgProcessingType"].update("Image Prewitt")
            img_output=ImgEdge(img_input, coldepth, "prewitt")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass
    
    elif event == "ImgEdgeCanny":
        try:

            window["ImgProcessingType"].update("Image Canny")
            img_output=ImgEdge(img_input, coldepth, "canny")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass
    
    elif event == "ImgLaplacial":
        try:

            window["ImgProcessingType"].update("Image Laplacian")
            img_output=ImgLaplacian(img_input, coldepth)    
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass
    
    elif event == "ImgGaussian":
        try:

            window["ImgProcessingType"].update("Image Gausian")
            img_output=ImgGaussian(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass

    elif event == "ImgSharpen":
        try:

            window["ImgProcessingType"].update("Image Sharpen")
            img_output=ImgSharpen(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass

    

    elif event == "ImgErosi":
        try:

            window["ImgProcessingType"].update("Image Erosi")
            img_output=ImgMorfologiErosiDilasi(img_input, coldepth, "erosi")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass
    
    elif event == "ImgDilasi":
        try:

            window["ImgProcessingType"].update("Image Dilasi")
            img_output=ImgMorfologiErosiDilasi(img_input, coldepth, "dilasi")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass

    elif event == "ImgOpening":
        try:

            window["ImgProcessingType"].update("Image Opening")
            img_output=ImgOpeningClosing(img_input, coldepth, "open")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass

    elif event == "ImgClosing":
        try:

            window["ImgProcessingType"].update("Image Closing")
            img_output=ImgOpeningClosing(img_input, coldepth, "close")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass
    
    elif event == "ImgGrayscale":
        try:

            window["ImgProcessingType"].update("Image RGB -> Grayscale")
            img_output=RGBtoGrayscalehsl(img_input, coldepth, "grayscale")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass
    
    elif event == "ImgHSL":
        try:

            window["ImgProcessingType"].update("Image RGB -> HSL")
            img_output=RGBtoGrayscalehsl(img_input, coldepth, "hsl")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["blend"].update(visible=False)
        except:
            pass


window.close()
