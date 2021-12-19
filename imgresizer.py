import cv2
import img2pdf
import os

                 
def resiz(path,output_size) :
    
    img = cv2.imread(path)
    x=((output_size*1024*2)/(int(img.shape[1])*int(img.shape[0])))**(0.5)

    width=int(img.shape[1]*x)
    height=int(img.shape[0]*x)
    
    dim=(width,height)
    resize=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
    return resize

def pdf(paths,svimg,path,output_size) :  
    cv2.imwrite(paths+svimg+".jpg",resiz(path,output_size))
    pdf=img2pdf.convert(paths+svimg+".jpg")
    file=open(paths+svimg+".pdf",'wb')
    file.write(pdf)
    cv2.destroyAllWindows()
    os.remove(paths+svimg+".jpg")   
    file.close()

def image(paths,svimg,path,output_size) :
    cv2.imwrite(paths+svimg+".jpg",resiz(path,output_size))
    cv2.destroyAllWindows()


