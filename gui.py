import tkinter as tk
import imgresizer

root = tk.Tk()
root.geometry("670x435")
root.minsize(670,435)
root.title("hello world")

img_var=tk.StringVar()
out_var=tk.StringVar()
paths_var=tk.StringVar()
svimg_var=tk.StringVar()
pdf_var=tk.StringVar()
image_var=tk.StringVar()
def submit() :
   img=img_var.get()
   out=out_var.get()
   paths=paths_var.get()
   svimg=svimg_var.get()
   pdf=pdf_var.get()
   image=image_var.get()
   try :
       if pdf=='pdf' :
           imgresizer.pdf(paths,svimg,img,int(out))
       if image=='image' :
           imgresizer.image(paths,svimg,img,int(out))
       success=tk.Label(root,text='Successfull!',font=('calibre',10, 'bold'))
       success.grid(row=4,column=0)
   except :
       fail =tk.Label(root,text='Failed!!',font=('calibre',10, 'bold'))
       fail.grid(row=4,column=0)

   img_var.set('')
   out_var.set('')
   paths_var.set('')
   svimg_var.set('')
   pdf_var.set('')
   image_var.set('')


img_label=tk.Label(root,text='Original Image Path',font=('calibre',10, 'bold'))
out_label=tk.Label(root,text='Resized Image size in KB',font=('calibre',10, 'bold'))
paths_label=tk.Label(root,text='Path to save',font=('calibre',10, 'bold'))
svimg_label=tk.Label(root,text='Name to save',font=('calibre',10, 'bold'))
img_entry=tk.Entry(root,textvariable=img_var,font=('calibre',10, 'bold'))
out_entry=tk.Entry(root,textvariable=out_var,font=('calibre',10, 'bold'))
paths_entry=tk.Entry(root,textvariable=paths_var,font=('calibre',10, 'bold'))
svimg_entry=tk.Entry(root,textvariable=svimg_var,font=('calibre',10, 'bold'))
pdf_check=tk.Checkbutton(root,text='PDF',variable=pdf_var,onvalue='pdf',offvalue='')
image_check=tk.Checkbutton(root,text='Image',variable=image_var,onvalue='image',offvalue='')
sub_but=tk.Button(root,text='Submit',command=submit)
img_label.grid(row=0,column=0)
img_entry.grid(row=0,column=2)
out_label.grid(row=1,column=0)
out_entry.grid(row=1,column=2)
paths_label.grid(row=2,column=0)
paths_entry.grid(row=2,column=2)
svimg_label.grid(row=3,column=0)
svimg_entry.grid(row=3,column=2)
pdf_check.grid(row=4,column=1)
image_check.grid(row=4,column=2)
sub_but.grid(row=6,column=1)

root.mainloop()