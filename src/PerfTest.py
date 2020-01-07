import timeit
import numpy as np
import cv2
import augmentedReality

def twoImageExperiment():
    fileName = '10twoImageExperiment.mp4'
    frames = augmentedReality.run('mg.mp4','marilyn.png', 'marilynAdvert.jpg', 33, 0.73, 'george.png', 'georgeAdvert.jpg', 28, 0.73, show=False)
    print(frames, "frames processed. Output saved to file",fileName)

def marilynExperiment():
    fileName = '11marilynExperiment.mp4'
    frames = augmentedReality.run('marilyn.mp4','marilyn.png', 'marilynAdvert.jpg', 33, 0.73, outputFile= fileName, show=False)
    print(frames, "frames processed. Output saved to file",fileName)

def georgeExperiment():
    fileName = '12georgeExperiment.mp4'
    frames = augmentedReality.run('george.mp4','george.png', 'georgeAdvert.jpg', 28, 0.73, outputFile= fileName, show=False)
    print(frames, "frames processed. Output saved to file",fileName)

def twoImageExperiment1():
    fileName = '00twoImageExperiment.mp4'
    frames = augmentedReality.run('mg.mp4','marilyn.png', 'marilynAdvert.jpg', 33, 0.73, 'george.png', 'georgeAdvert.jpg', 28, 0.73, show=False)
    print(frames, "frames processed. Output saved to file",fileName)

def marilynExperiment1():
    fileName = '01marilynExperiment.mp4'
    frames = augmentedReality.run('marilyn.mp4','marilyn.png', 'marilynAdvert.jpg', 33, 0.73, outputFile= fileName, show=False)
    print(frames, "frames processed. Output saved to file",fileName)

def georgeExperiment1():
    fileName = '02georgeExperiment.mp4'
    frames = augmentedReality.run('george.mp4','george.png', 'georgeAdvert.jpg', 28, 0.73, outputFile= fileName, show=False)
    print(frames, "frames processed. Output saved to file",fileName)


if __name__ == '__main__':
    print(timeit.timeit("marilynExperiment1()", setup="from __main__ import marilynExperiment1", number=3))
    print(timeit.timeit("georgeExperiment1()", setup="from __main__ import georgeExperiment1", number=3))
    print(timeit.timeit("twoImageExperiment1()", setup="from __main__ import twoImageExperiment1", number=3))
    print(timeit.timeit("marilynExperiment()", setup="from __main__ import marilynExperiment", number=3))
    print(timeit.timeit("georgeExperiment()", setup="from __main__ import georgeExperiment", number=3))
    print(timeit.timeit("twoImageExperiment()", setup="from __main__ import twoImageExperiment", number=3))
