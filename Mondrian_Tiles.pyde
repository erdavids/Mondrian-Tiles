w, h = 1000, 1000

subdivisions = 50000

# Not too small
min_diff = 80

# Space between quads
sep = 1

# Piet Mondrian Color Palette
colors = [(38, 71, 124), (240, 217, 92), (162, 45, 40), (223, 224, 236), (223, 224, 236), (223, 224, 236), (223, 224, 236), (223, 224, 236)]

# Subdivision adjustment
splits = [.5, 1, 1.5]

# Canvas Border
edge = 10

def setup():
    size(w, h)
    pixelDensity(2)
    
    background(255)

    quads = []
    # Add the initial rectangle
    quads.append([(edge, edge), (w - edge, edge), (w - edge, h - edge), (edge, h - edge)])
    
    # Start splitting things up
    for i in range(subdivisions):
        q_index = int(random(len(quads)))
        q = quads[q_index]
        q_lx = q[0][0]
        q_rx = q[1][0]
        q_ty = q[0][1]
        q_by = q[2][1]
        
        s = splits[int(random(len(splits)))]
        if (random(1) < .5):
            if ((q_rx - q_lx) > min_diff):
                # Get new shapes x value (y is same)
                x_split = (q_rx - q_lx)/2 * s + q_lx
                
                quads.pop(q_index)
                quads.append([(q_lx, q_ty), (x_split - sep, q_ty), (x_split - sep, q_by), (q_lx, q_by)])
                quads.append([(x_split + sep, q_ty), (q_rx, q_ty), (q_rx, q_by), (x_split + sep, q_by)])
            
            
        else:
            if ((q_by - q_ty) > min_diff):
                y_split = (q_by - q_ty)/2 * s + q_ty
                
                quads.pop(q_index)
                quads.append([(q_lx, q_ty), (q_rx, q_ty), (q_rx, y_split - sep), (q_lx, y_split - sep)])
                quads.append([(q_lx, y_split + sep), (q_rx, y_split + sep), (q_rx, q_by), (q_lx, q_by)])
        

    stroke(0)
    strokeWeight(2)
    for q in quads:
        fill(*colors[int(random(len(colors)))])
        beginShape()
        for p in q:
            vertex(p)
        endShape(CLOSE)
    
    save("Examples/Classic/" + str(int(random(10000))) + ".png")
