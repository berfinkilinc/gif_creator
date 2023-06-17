import imageio

images = ["hummingbird/*"]
for filename in images:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images)