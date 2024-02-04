from PIL import Image

k=Image.open('12.jpg')
b=k.convert('L')
b.save('black.jpg')
k.show()
b.show()