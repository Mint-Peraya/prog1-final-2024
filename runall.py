import run_ball
from seven_segments_proc import seven_seg

tom_color = (255, 0, 0)
Tom = seven_seg(tom_color)
delay_in_seconds = 0.2
while True:
    for i in range(0, 10):
        Tom.clear()
        Tom.draw(i)
        Tom.my_delay(delay_in_seconds)
Tom.done()