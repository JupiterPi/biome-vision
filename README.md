# BiomeVision
BiomeVision is an AI project for reading biome data from Minecraft screenshots.


## Topic

BiomeVision is an image recognition AI that can recognize Minecraft biomes from screenshots. It will probably learn to read that information from the present colors and shapes like trees. Part of the project is generating the dataset in a fully automated way. 

## Steps

Generating the dataset

- *Research* - research possible implementations of necessary processes: Take screenshots, take biome labels, transform screenshots and biome data to correct format (matrix form with color information and numerics), automatic teleportation with correct orientation
- *Conceptualization* - choose Python or Java as the programming language
- *Conceptualization* - saving the dataset for reading it in later (fast)
- *Implementation* - write program to generate the dataset
- *Generating* - generate big dataset (60,000+ images)

Creating the image recognition network

- *Research* - further reading about CNNs with TensorFlow (also utilization of color information)
- *Implementation* - figure out image resolution well-suited for training and classification
- *Implementation & Optimization* - train and optimize the CNN

## Project Roadmap

| KW                  | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---------------------|----|----|----|----|----|----|----|----|----|
| **Dataset**         |    |    |    |    |    |    |    |    |    |
| *Research*          | x  |    |    |    |    |    |    |    |    |
| *Conceptualization* | x  |    |    |    |    |    |    |    |    |
| *Implementation*    |    | x  | x  |    |    |    |    |    |    |
| *Generating*        |    |    | x  |    |    |    |    |    |    |
|                     |    |    |    |    |    |    |    |    |    |
| **Network**         |    |    |    |    |    |    |    |    |    |
| *Research*          |    |    |    | x  | x  |    |    |    |    |
| *Implementation*    |    |    |    |    |    | x  | x  |    |    |
| *Optimization*      |    |    |    |    |    |    | x  | x  | x  |
