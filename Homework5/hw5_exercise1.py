'''
Problem 1. Landing the slides at SlideWorld
You have won a contract for the design of a new theme park, SlideWorld. The primary attraction
of the park is to consist of n landings, numbered 1 through n, which will be connected by a
number of slides. Each slide (i, j) connects a landing i to a landing j > i, which means that
slide (i, j) goes from landing i directly to landing j. See Figure 1 for an example of the possible
slides when n = 3.
Slideworld wants to let the customers begin their trip at any landing b and end at any other
landing e > b. Putting in all the combination slides in the park is going to break the bank. 
So you have been asked to determine a set of slides so that any customer can get from any landing b to any landing e > b using at most two slides. 
That is, it should be possible to get from any b to any e > b either by taking a direct slide (b, e) or by taking two slides (b, m) and (m, e). 
To be clear, a solution of your algorithm is a set of slides.

Using divide-and-conquer, we will find a solution that uses only O(n*log n) slides while
ensuring that any customer can get from any landing b to any landing e > b using at most two
Slides.

Figure 1: An example of all possible slides when n = 3. The slides are (1, 2); (1, 3); and (2, 3).
(a) For the base cases n = 1;2, design a system using at most 1 slide.
(b) For n > 2 we will use divide-and-conquer. Assume that we already put in place slides
connecting the first half landings and slides connecting the second half landings so that if i
and j both belong to the same half, we can get from i to j in at most 2 slides. Show how to
add O(n) additional slides so that if i is in the first half and j is in the second half we can
get from i to j using only two slides.
(c) Using part (b), write a divide-and-conquer algorithm that takes as input
the number of landings n and outputs the list of all the slides used by your attraction.
'''

from math import sqrt
from sys import argv
import numpy as np
import matplotlib.pyplot as plt #Run python -m pip install matplotlib

class SlideWorld():
    def __init__(self):
        self.slides = []
        self.maxSlides = 10
        self.maxSquareFeet = 100
        self.slideColor = 'y'
        self.transitionSlideColor = 'r'
        self.transitionLineColor = 'y'
        self.directLineColor = 'b'
    
    #create slides
    def design(self):
        midPoint = self.maxSquareFeet / 2
        nearest = float('inf')

        xs = np.random.randint(0, self.maxSquareFeet, size=self.maxSlides)
        ys = np.random.randint(0, self.maxSquareFeet, size=self.maxSlides)
        for i in range(0, self.maxSlides):
            slide = Slide(i + 1, xs[i], ys[i])
            #find the distance to the nearest midpoint
            distance = self.find_distance(slide.x, slide.y, midPoint, midPoint)
            if distance < nearest:
                nearest = distance
                self.transitionSlide = slide
            self.slides.append(slide)

        
        #divide-and-conquer algorithm to find the distance to the nearest sibling
        n = len(self.slides)
        self.slides.sort(key = lambda s: [s.x, s.y])
        for i in range(n):
            s1 = self.slides[i]
            if s1 != self.transitionSlide:
                for j in range(i + 1, n):
                    s2 = self.slides[j]
                    distance = self.find_distance(s1.x, s1.y, s2.x, s2.y)
                    if distance < s1.minimum and s2 != self.transitionSlide:
                        s1.minimum = distance
                        s1.directSlide = s2

    #draw slides
    def develop(self):
        for s in self.slides:
            if s != self.transitionSlide:
                plt.plot([s.x, self.transitionSlide.x], [s.y, self.transitionSlide.y], color=self.transitionLineColor, alpha=0.3)
                plt.scatter(s.x, s.y, s=200, color=self.slideColor)

            if s.directSlide != s:
                plt.plot([s.x, s.directSlide.x], [s.y, s.directSlide.y], alpha=0.3, label=s.__str__())

            plt.annotate(s.index,
                    (s.x, s.y), # these are the coordinates to position the label
                    textcoords='offset points', # how to position the text
                    xytext=(0, 0), # distance from text to points (x,y)
                    ha='center',
                    va='center')

    def find_distance(self, x1, y1, x2, y2):
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Slide():
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.directSlide = self
        self.minimum = float('inf')
    
    def __str__(self):
        return 'Slide {} -> {}'.format(self.index, self.directSlide.index)
    
    def __repr__(self):
        return str(self)

def main(argv):
    sw = SlideWorld()
    if len(argv) > 1:
        sw.maxSlides = int(argv[1])
    if len(argv) > 1:
        sw.maxSquareFeet = int(argv[2])

    sw.design()
    sw.develop()

    plt.plot(0, 0, color=sw.transitionLineColor, label='Transition Slide') #legend item
    plt.scatter(sw.transitionSlide.x, sw.transitionSlide.y, s=200, color=sw.transitionSlideColor, label='1. Transition Point')

    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('slide_world.png', dpi=150)
    print('Transition Slide:', sw.transitionSlide.index)
    print('Direct Slides:', sw.slides)

if __name__ == '__main__':
    main(argv)
    plt.show()