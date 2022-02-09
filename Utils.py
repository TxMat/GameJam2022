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
    sheet = pygame.image.load(img_name)
    for f in range(frame_nb):
        rect = pygame.Rect(xstart + f * width, ystart, height, width)
        frames.append(sheet.subsurface(rect))
    return frames


def scale(frame, scale):
    fscale = (frame.get_height() * scale, frame.get_width() * scale)
    return pygame.transform.scale(frame, fscale)


def draw_line(surface, start_pos, end_pos, width=1, color=(79, 32, 15)):
    pygame.draw.line(surface, color, start_pos, end_pos, width)
