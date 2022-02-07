import pygame


def frames_from_spritesheet(img_name, xstart, ystart, height, width, frame_nb) -> [pygame.image]:
    """

    Returns a frame list from the image img_name.

    :param img_name:
    :param xstart:
    :param ystart:
    :param height:
    :param width:
    :param frame_nb:
    :return: Array of frames
    """
    frames = []
    sheet = pygame.image.load(img_name).convert()
    for f in range(frame_nb):
        rect = pygame.Rect(xstart + f * width, ystart, height, width)
        frames.append(sheet.subsurface(rect))
    if want_flip:
        for f in range(frame_nb):
            rect = pygame.Rect(xstart + f * width, ystart, height, width)
            frames.append(pygame.transform.flip(sheet.subsurface(rect), True, False))
    return frames


