import qrcode  # pyright: ignore[reportMissingImports]
url=input("please input your url: ")
filename=input('please input your file name : ')
if not(filename.endswith('.png')):
    filename=filename+".png"
img = qrcode.make('url')
type(img)  # qrcode.image.pil.PilImage
img.save(filename)