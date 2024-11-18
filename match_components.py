import cv2 as cv

def extract_components(filename):

    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    r_temp = get_template_contour(cv.imread("resistor_template.png"))
    
    

    return components

def get_template_contour(temp):
    cont, hier = cv.findContours(temp, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i in range(len(cont)):
        c = cont[i]
        h = hier[0, i]
        if h[3] != -1:
            return c

extract_components("mini_circuit.JPG")