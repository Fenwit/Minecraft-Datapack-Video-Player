import os
import numpy as np
from PIL import Image
import math
import random
import threading

directory_path = input("Path to video frames: ")

blocks = {}

try:
    contents = os.listdir(directory_path)
except FileNotFoundError:
    print(f"Error: Directory not found at '{directory_path}'")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

blocks = {'pink_concrete': [213.5, 101.01171875, 142.8671875], 'dark_prismarine': [51.86328125, 91.63671875, 75.94921875], 'nether_bricks': [44.29296875, 21.87109375, 26.09765625], 'andesite': [136.15234375, 136.26171875, 136.77734375], 'terracotta': [152.1328125, 94.015625, 67.71875], 'red_terracotta': [143.109375, 61.01953125, 46.90625], 'lime_wool': [112.2109375, 185.1953125, 25.796875], 'gray_wool': [62.74609375, 68.234375, 71.5546875], 'stripped_cherry_log': [215.078125, 145.16015625, 148.9453125], 'basalt': [73.20703125, 72.52734375, 77.921875], 'redstone_block': [175.56640625, 24.78125, 5.125], 'mangrove_planks': [117.953125, 54.08203125, 48.6640625], 'light_blue_wool': [58.0703125, 175.046875, 217.31640625], 'exposed_copper': [161.078125, 125.703125, 103.93359375], 'mud_bricks': [137.14453125, 103.7734375, 79.07421875], 'cobblestone': [127.7890625, 127.3046875, 127.59765625], 'stripped_warped_stem': [57.5703125, 150.92578125, 147.77734375], 'oxidized_cut_copper': [79.71875, 153.6171875, 126.4296875], 'stone_bricks': [122.45703125, 121.81640625, 122.45703125], 'acacia_log': [103.25, 96.578125, 86.91796875], 'emerald_block': [42.37890625, 203.44921875, 87.80078125], 'blue_terracotta': [74.29296875, 59.68359375, 91.109375], 'pink_terracotta': [161.92578125, 78.27734375, 78.66796875], 'prismarine_bricks': [99.25, 171.625, 158.4296875], 'stripped_pale_oak_log': [245.828125, 238.18359375, 236.9453125], 'yellow_wool': [248.78125, 197.9609375, 39.6328125], 'copper_block': [192.41796875, 107.65625, 79.8203125], 'orange_concrete': [224.34375, 97.13671875, 0.6328125], 'cut_sandstone': [217.80859375, 206.4453125, 159.8125], 'stripped_oak_log': [177.45703125, 144.1015625, 86.05078125], 'stripped_spruce_log': [115.6484375, 89.96484375, 52.44140625], 'brown_terracotta': [77.234375, 51.1796875, 35.703125], 'stripped_mangrove_log': [119.54296875, 54.4296875, 47.9921875], 'orange_terracotta': [161.59765625, 83.87109375, 37.671875], 'jungle_log': [85.21484375, 67.98046875, 25.1796875], 'pale_oak_log': [87.60546875, 77.58203125, 75.015625], 'stripped_jungle_log': [171.48828125, 132.8359375, 84.58203125], 'stripped_birch_log': [196.9921875, 176.015625, 118.37109375], 'light_blue_concrete': [35.59765625, 137.0390625, 198.9140625], 'warped_planks': [43.05078125, 104.87109375, 99.140625], 'netherrack': [97.58203125, 38.4140625, 38.4140625], 'lime_concrete': [94.08984375, 168.8046875, 24.5], 'light_gray_wool': [142.03125, 142.1640625, 134.6015625], 'calcite': [223.47265625, 224.46484375, 220.6640625], 'dark_oak_planks': [66.66015625, 43.09765625, 20.21875], 'oak_planks': [162.203125, 130.8203125, 78.62890625], 'birch_log': [216.55859375, 215.0078125, 210.296875], 'cyan_concrete': [21.4453125, 119.21875, 136.1875], 'bamboo_planks': [193.37109375, 173.1015625, 80.47265625], 'yellow_terracotta': [186.26953125, 133.140625, 35.36328125], 'black_wool': [20.6015625, 21.296875, 25.6328125], 'light_gray_concrete': [125.03125, 125.03125, 115.03125], 'mossy_stone_bricks': [115.43359375, 121.125, 105.140625], 'yellow_concrete': [240.98828125, 175.41015625, 21.44921875], 'brown_concrete': [96.44921875, 59.546875, 31.59765625], 'mud': [60.1015625, 57.48828125, 60.62890625], 'cherry_log': [54.71875, 33.01171875, 44.3984375], 'dark_oak_log': [60.39453125, 46.55859375, 26.15625], 'coal_block': [16.0234375, 15.91796875, 15.91796875], 'polished_granite': [154.1015625, 106.84765625, 89.2265625], 'granite': [149.4296875, 103.2421875, 85.97265625], 'diamond_block': [98.1640625, 237.13671875, 228.12109375], 'acacia_planks': [168.1328125, 90.37109375, 50.2265625], 'green_terracotta': [76.0078125, 83.2890625, 42.3359375], 'white_terracotta': [209.63671875, 178.03515625, 161.34765625], 'light_blue_terracotta': [113.484375, 108.53125, 137.9921875], 'jungle_planks': [160.44140625, 115.19140625, 80.79296875], 'oak_log': [109.09375, 85.125, 50.6875], 'white_wool': [233.58984375, 236.296875, 236.7734375], 'birch_planks': [192.46875, 175.29296875, 121.2421875], 'lime_terracotta': [103.53515625, 117.67578125, 52.796875], 'cherry_planks': [226.51171875, 178.7265625, 172.71484375], 'red_sandstone': [186.73046875, 99.34375, 29.18359375], 'diorite': [188.71875, 188.453125, 188.98046875], 'sandstone': [216.43359375, 203.2578125, 155.8359375], 'weathered_copper': [108.296875, 153.00390625, 110.359375], 'black_concrete': [8.40234375, 10.40234375, 15.40234375], 'magenta_terracotta': [149.66796875, 88.1015625, 108.6796875], 'magenta_wool': [189.54296875, 68.765625, 179.91796875], 'cyan_wool': [21.24609375, 137.7265625, 145.3515625], 'iron_block': [220.1171875, 220.0078125, 220.0078125], 'gray_concrete': [54.6171875, 57.6171875, 61.6171875], 'black_terracotta': [37.21875, 22.828125, 16.38671875], 'red_wool': [160.96875, 39.3203125, 34.640625], 'stripped_bamboo_block': [193.37109375, 173.1015625, 80.47265625], 'white_concrete': [207.109375, 213.078125, 214.07421875], 'cyan_terracotta': [86.71484375, 91.01171875, 91.00390625], 'chiseled_stone_bricks': [119.78125, 118.90625, 119.78125], 'purple_terracotta': [118.4453125, 70.26953125, 86.08984375], 'stripped_dark_oak_log': [72.83203125, 56.890625, 36.03515625], 'orange_wool': [240.65234375, 118.078125, 19.51171875], 'mangrove_log': [83.61328125, 66.74609375, 41.140625], 'cut_copper': [191.171875, 106.8671875, 80.56640625], 'polished_diorite': [192.98046875, 193.078125, 194.55078125], 'spruce_planks': [114.91796875, 84.84375, 48.55859375], 'blue_wool': [53.0546875, 57.25390625, 157.4921875], 'pink_wool': [237.9140625, 141.37890625, 172.3515625], 'spruce_log': [58.83203125, 37.6640625, 16.91015625], 'blue_concrete': [44.5390625, 46.5390625, 143.421875], 'lapis_block': [30.6484375, 67.37109375, 140.109375], 'gold_block': [246.41796875, 208.3203125, 61.625], 'mossy_cobblestone': [110.109375, 118.5, 94.9375], 'green_concrete': [73.40625, 91.33984375, 36.4921875], 'exposed_cut_copper': [154.66015625, 121.75390625, 101.265625], 'brown_wool': [114.234375, 71.609375, 40.5859375], 'dirt': [134.25, 96.296875, 67.0], 'light_gray_terracotta': [135.25390625, 106.8828125, 97.5], 'stripped_crimson_stem': [137.3203125, 57.3203125, 90.05078125], 'stripped_acacia_log': [174.7421875, 92.93359375, 59.77734375], 'polished_andesite': [132.2578125, 134.75390625, 133.99609375], 'magenta_concrete': [169.20703125, 48.4765625, 159.2109375], 'weathered_cut_copper': [109.37109375, 145.3671875, 107.53125], 'green_wool': [84.83203125, 109.53515625, 27.50390625], 'clay': [160.6796875, 166.4609375, 179.4453125], 'cobbled_deepslate': [77.2734375, 77.2734375, 80.609375], 'purple_wool': [121.875, 42.2109375, 172.5078125], 'pale_oak_planks': [227.69140625, 217.5234375, 216.38671875], 'oxidized_copper': [82.42578125, 162.66796875, 132.8671875], 'crimson_planks': [101.03515625, 48.78125, 70.56640625], 'red_concrete': [142.3828125, 32.8125, 32.8125], 'purple_concrete': [100.4140625, 31.62109375, 156.3828125], 'gray_terracotta': [57.78515625, 42.4140625, 35.5625]}

x1 = 0
y1 = -60
z1 = 0

x2 = 1
y2 = -60
z2 = 0

filepath = input("Output path for .mcfunction files: ")

def GetBlockFromPixel(PixelRGB):
    testlist = []
    for i in blocks:
        CurrentBlockRGB = blocks[i]
        d = math.sqrt(math.pow(((PixelRGB[0]-CurrentBlockRGB[0])*1), 2) + math.pow(((PixelRGB[1]-CurrentBlockRGB[1])*1), 2) + math.pow(((PixelRGB[2]-CurrentBlockRGB[2])*1), 2))
        
        #d = sqrt(((r2-r1)*0.3)^2 + ((g2-g1)*0.59)^2 + ((b2-b1)*0.11)^2)

        testlist.append(d + random.randint(0, 1)/2)
    
    closest = testlist.index(min(testlist))

    testlist_keys_list = list(blocks.keys())

    ClosestBlock = testlist_keys_list[closest]
    
    return(ClosestBlock)

def GenerateFrame(FrameStart):
    print("start!")
    f = open(f"{filepath}/videoframe{FrameStart}.mcfunction", "x")

    im = Image.open(f"{directory_path}{FrameStart}.jpg")
    pix = im.load()
    size = im.size

    ycoordinate = -60
    for xcord in range(size[0]):
        current2 = []
        ycoordinate = (-60 + size[1] + 1)
        ToSet = GetBlockFromPixel(pix[xcord, 0])
        current2.append(ToSet)
        for ycord in range(size[1]):

            ToSet = GetBlockFromPixel(pix[xcord, ycord])
            current2.append(ToSet)
            if ycord > -1 and current2[0] == current2[1] and ycord != size[1] - 1:
                pass
            else:
                with open(f"{filepath}/videoframe{FrameStart}.mcfunction", "a") as f:
                    f.write("\n"+f"fill {x1 + xcord} {ycoordinate} {z1} {x2 + xcord} {y2 + size[1] - ycord} {z2} {current2[0]}")
                ycoordinate = (-60 + size[1] - ycord + 1)
            if len(current2) > 1:
                current2.pop(0)
    with open(f"{filepath}/videoframe{FrameStart}.mcfunction", "a") as f:
        f.write("\n"+f"schedule function uh:videoframe{FrameStart+1} 4t")
    print(f"Video Frame {FrameStart+1} done")

# def GenerateNumberFrames(StartNum, StopNum):
#     for i in range(StartNum, StopNum):
#         GenerateFrame(i)

# GenerateNumberFrames(0, 2)

for i in range(33, int(input("# frames (divisible by 3): "))+33, 3):
    frames1 = threading.Thread(target=GenerateFrame, args=(i,))
    frames2 = threading.Thread(target=GenerateFrame, args=(i+1,))
    frames3 = threading.Thread(target=GenerateFrame, args=(i+2,))

    frames1.start()
    frames2.start()
    frames3.start()

    frames1.join()
    frames2.join()
    frames3.join()


# for i in range(2):
#     GenerateFrame(i)
