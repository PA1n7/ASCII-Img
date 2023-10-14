import pygame, os
from pixelize import pixel

color_equivalence = {
    230: "█",
    200: "▓",
    170: "@",
    150: "▒",
    100: "#",
    50: "░",
    0: "+"
}

def convert_to_ascii(source:pygame.Surface, out_file:str):
    out = ""
    size = source.get_size()
    for y in range(size[1]):
        for x in range(size[0]):
            color=source.get_at((x, y))[0]
            for k, v in color_equivalence.items():
                if color>k:
                    out+=v
                    break
        out+="\n"
    print(out)
    open(out_file, "w", encoding="UTF-8").write(out)
                
def desaturate(source:pygame.Surface, dest:pygame.Surface):
    size = source.get_size()
    for y in range(size[1]):
        for x in range(size[0]):
            color = source.get_at((x, y))
            avg = sum(color)/len(color)
            pygame.draw.rect(dest, (avg, avg, avg), pygame.Rect(x, y, 1, 1))

def ascii(img_file:str, out_file:str, size:int):
    pixel(img_file, "temp.png", size)
    pixelized = pygame.image.load("temp.png")
    pixelized = pygame.transform.scale(pixelized, (size, size))
    desaturate(pixelized, pixelized)
    convert_to_ascii(pixelized, out_file)
    os.remove("temp.png")