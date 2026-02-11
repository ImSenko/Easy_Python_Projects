import imageio. v3 as iio
filenames = []
images = []
filenames.append(input("Enter the name of the first image: "))
filenames.append(input("Enter the name of the second image: "))
for filename in filenames:
  images.append(iio.imread(filename))
iio.imwrite('new-gif.gif', images, duration=500, loop = 0)
print("GIF created successfully! Check the local directory for the file named 'new-gif.gif'.")