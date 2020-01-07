import timeit
import numpy as np
import cv2
import augmentedReality

def twoImageExperiment():
    fileName = '03twoImageExperiment.mp4'
    frames = augmentedReality.run('mg.mp4','marilyn.png', 'marilynAdvert.jpg', 33, 0.73, 'george.png', 'georgeAdvert.jpg', 28, 0.73, outputFile=fileName, show=False)
    print(frames, "frames processed. Output saved to file",fileName)

def marilynExperiment():
    fileName = '01marilynExperiment.mp4'
    frames = augmentedReality.run('marilyn.mp4','marilyn.png', 'marilynAdvert.jpg', 33, 0.73, outputFile= fileName, show=False)
    print(frames, "frames processed. Output saved to file",fileName)

def georgeExperiment():
    fileName = '02georgeExperiment.mp4'
    frames = augmentedReality.run('george.mp4','george.png', 'georgeAdvert.jpg', 28, 0.73, outputFile= fileName, show=False)
    print(frames, "frames processed. Output saved to file",fileName)

def twoImageExperiment1():
    frames = augmentedReality.run('mg.mp4','marilyn.png', 'marilynAdvert.jpg', 33, 0.73, 'george.png', 'georgeAdvert.jpg', 28, 0.73)
    print(frames, "frames processed.")

def marilynExperiment1():
    frames = augmentedReality.run('marilyn.mp4','marilyn.png', 'marilynAdvert.jpg', 33, 0.73)
    print(frames, "frames processed.")

def georgeExperiment1():
    frames = augmentedReality.run('george.mp4','george.png', 'georgeAdvert.jpg', 28, 0.73)
    print(frames, "frames processed.")


if __name__ == '__main__':
    # marilynExperiment1()
    # georgeExperiment1()
    # twoImageExperiment1()
    print( "--- Executing Augmented Reality Experiment 1---")
    print( "--- Searching for Marilyn Monroe in Video---")
    marilynExperiment()
    print( "--- Executing Augmented Reality Experiment 2---")
    print( "--- Searching for George Washington in Video---")
    georgeExperiment()
    print( "--- Executing Augmented Reality Experiment 3---")
    print( "--- Searching for 2 objects in Video---")
    twoImageExperiment()
