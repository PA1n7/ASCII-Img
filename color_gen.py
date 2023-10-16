import pygame, json

def percentage(screen:pygame.Surface):
    size = screen.get_size()
    total=size[0]*size[1]
    count = 0
    for x in range(size[0]):
        for y in range(size[1]):
            if screen.get_at((x, y)) == (0, 0, 0):
                count+=1
    return count/total

def test(space=True, values_tested = ["S", "#", "$", "=", "-", "+", "8", "@", " ", ";", ".", ",", "░", "▒", "▓", "█", "▄", "▌", "■", "╔", "╬", "\"", "'"]):
    tester = pygame.Surface((500, 500))
    percentage_equivalence = []
    pygame.font.init()
    font = pygame.font.Font(pygame.font.match_font("arial"), 400)

    for value in values_tested:
        text = font.render(value, True, (0, 0, 0), None)
        tester.fill((255, 255, 255))
        tester.blit(text, (0, 0))
        percentage_equivalence.append(percentage(tester))

    #fixing percentages
    __ = []
    for per in percentage_equivalence:
        __.append(per/max(percentage_equivalence))
    percentage_equivalence = __

    #converting to 255 scale
    color_version = [int(s*255) for s in percentage_equivalence]

    out_dict = {}

    for key in range(len(color_version)):
        out_dict[str(color_version[key])] = values_tested[key]

    # organize dict in decreasing key value
    _temp = {}
    _temp_keys = sorted([int(key) for key in out_dict.keys()])[::-1] #Flip to get in descending order
    for key in _temp_keys:
        _temp[str(key)] = out_dict[str(key)]

    out_dict = _temp
    #space out equally without paying much attention, returns crisper value
    if space:
        _spaced = {}
        index = 255
        step = int(255/len(out_dict.keys()))
        for value in out_dict.values():
            _spaced[str(index)]=value
            index-=step
        out_dict=_spaced
    
    #writing to file
    open("color_equivalence.json", "w", encoding="UTF-8").write(json.dumps(out_dict, indent=4))

test(True)