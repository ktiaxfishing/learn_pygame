import pygame

def rescale_img_with_scale(img, new_scale):
    assert type(img) ==  pygame.Surface, 'you can use pygame.image.load()'
    assert type(new_scale) == float or type(new_scale) == int
    w_old, h_old = img.get_size()
    w_new = w_old * new_scale
    h_new = h_old * new_scale
    # assert type(w_old) == float
    # assert type(h_new) == float
    scaled_img = pygame.transform.scale(img, (w_new, h_new))
    return scaled_img

def rescale_img_with_width(img, new_width):
    old_width, old_height = img.get_size()

    # scale_w = w / new_width
    # height = h * scale_w
    # scaled_img = pygame.transform.scale(img, (scale_w,height))

    scale = new_width / old_width
    new_height = old_height * scale
    scaled_img = pygame.transform.scale(img, (new_width, new_height))
    return scaled_img

def rescale_img(img, scale=None, width=None):
    if scale is not None and width is None:
        return rescale_img_with_scale(img, scale)
    elif scale is None and width is not None:
        return rescale_img_with_width(img, width) 
    else:
        assert False, 'wrong input'