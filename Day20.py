import numpy

image = []
binary_converter = numpy.array([2 ** i for i in range(8, -1, -1)])
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day20.txt") as puzzle_input:
        pixelmap = [1 if c == "#" else 0 for c in puzzle_input.readline().strip()]
        puzzle_input.readline()
        for line in puzzle_input:
                image.append([1 if c == "#" else 0 for c in line.strip()])

infinite_ones = False                
for i in range(50):
        if infinite_ones:
                padded_image = numpy.ones((len(image) + 4, len(image[0]) + 4), int)
                if pixelmap[-1] == 0:
                        infinite_ones = False
        else:
                padded_image = numpy.zeros((len(image) + 4, len(image[0]) + 4), int)
                if pixelmap[0] == 1:
                        infinite_ones = True
        padded_image[2:-2,2:-2] = image
        image = numpy.zeros((len(image) + 2, len(image[0]) + 2), int)
        
        for y in range(len(image)):
                for x in range(len(image[0])):
                        image[x,y] = pixelmap[padded_image[x:x+3, y:y+3].flatten().dot(binary_converter)]

print(sum(image.flatten()))
