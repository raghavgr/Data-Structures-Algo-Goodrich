""" Draw an english ruler with ticks according to the given major length """
def draw_line(tick_length, tick_label=''):
    """ Draw one line with given tick length along with optional label"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """ Draw tick interval based on the central tick length"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """ Main function that calls subfunctions draw_interval and draw_line """
    draw_line(major_length, '0')
    for i in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(i))

draw_ruler(3, 3)
