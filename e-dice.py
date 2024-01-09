o=(0,0,0)
b=(0,0,255)
one_img= [o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o, 
          o,o,o,b,b,o,o,o, 
          o,o,o,b,b,o,o,o, 
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o]
two_img = [b,b,o,o,o,o,o,o, 
          b,b,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,b,b, 
          o,o,o,o,o,o,b,b]  
three_img = [b,b,o,o,o,o,o,o, 
          b,b,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o, 
          o,o,o,b,b,o,o,o, 
          o,o,o,b,b,o,o,o, 
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,b,b, 
          o,o,o,o,o,o,b,b] 
four_img = [b,b,o,o,o,o,b,b, 
          b,b,o,o,o,o,b,b,
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o, 
          o,o,o,o,o,o,o,o, 
          b,b,o,o,o,o,b,b, 
          b,b,o,o,o,o,b,b]
five_img = [b,b,o,o,o,o,b,b, 
          b,b,o,o,o,o,b,b,
          o,o,o,o,o,o,o,o, 
          o,o,o,b,b,o,o,o, 
          o,o,o,b,b,o,o,o, 
          o,o,o,o,o,o,o,o, 
          b,b,o,o,o,o,b,b, 
          b,b,o,o,o,o,b,b]
six_img = [b,b,o,o,o,o,b,b, 
          b,b,o,o,o,o,b,b,
          o,o,o,o,o,o,o,o, 
          b,b,o,o,o,o,b,b, 
          b,b,o,o,o,o,b,b, 
          o,o,o,o,o,o,o,o, 
          b,b,o,o,o,o,b,b, 
          b,b,o,o,o,o,b,b]
          
def number_gen(event): 
    if event.action == “pressed”: 
        val = random.randint(1,6) 
    print(val) 
    if val == 1: 
        sense.set_pixels(one_img) 
    if val == 2: 
        sense.set_pixels(two_img) 
    if val == 3: 
        sense.set_pixels(three_img) 
    if val == 4: 
        sense.set_pixels(four_img) 
    if val == 5: 
        sense.set_pixels(five_img) 
    if val == 6: 
        sense.set_pixels(six_img)
    sleep(2) 
    sense.clear()