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

>> python hw5_exercise1.py   
Direct Slides:
[1 -> 3, 3 -> 4, 6 -> 7, 7 -> 8, 8 -> 9]
Transition Slides:
['1 -> 5 -> 6', '1 -> 5 -> 7', '1 -> 5 -> 8', '1 -> 5 -> 9']
['2 -> 5 -> 6', '2 -> 5 -> 7', '2 -> 5 -> 8', '2 -> 5 -> 9']
['3 -> 5 -> 6', '3 -> 5 -> 7', '3 -> 5 -> 8', '3 -> 5 -> 9']
['4 -> 5 -> 6', '4 -> 5 -> 7', '4 -> 5 -> 8', '4 -> 5 -> 9']

>> python hw5_exercise1.py 5

Direct Slides:
[1 -> 2, 4 -> 5]
Transition Slides:
['1 -> 3 -> 4', '1 -> 3 -> 5']
['2 -> 3 -> 4', '2 -> 3 -> 5']

>> python python hw5_exercise1.py 5 50

Direct Slides:
[1 -> 2, 4 -> 5]
Transition Slides:
['1 -> 3 -> 4', '1 -> 3 -> 5']
['2 -> 3 -> 4', '2 -> 3 -> 5']

'''

from math import sqrt, ceil
from sys import argv
import numpy as np
import matplotlib.pyplot as plt #Run python -m pip install matplotlib

class SlideWorld():
    def __init__(self):
        self.slides = []
        self.maxSlides = 9
        self.maxFeet = 100
        self.transitionSlide = None
        self.slideColor = 'y'
        self.transitionSlideColor = 'r'
        self.transitionLineColor = 'y'
        self.directLineColor = 'b'
        self.directSlides = []
    
    #create slides
    def design(self):
        midPoint = self.maxFeet / 2
        nearest = float('inf')

        xs = np.random.randint(0, self.maxFeet, size=self.maxSlides)
        ys = np.random.randint(0, self.maxFeet, size=self.maxSlides)
        for i in range(0, self.maxSlides):
            slide = Slide(xs[i], ys[i])
            #find the distance to the nearest midpoint
            distance = self.find_distance(slide.x, slide.y, midPoint, midPoint)
            if distance < nearest:
                if self.transitionSlide:
                    self.slides.append(self.transitionSlide)
                nearest = distance
                self.transitionSlide = slide
            else:
                self.slides.append(slide)
        
        self.slides.sort(key = lambda s: [s.x, s.y])
        n = len(self.slides) + 1
        #move the transition slide to the middle
        self.transitionSlide.level = ceil(n / 2)
        self.slides.insert(self.transitionSlide.level - 1, self.transitionSlide)
        
        #divide-and-conquer algorithm to find the distance to the nearest sibling
        for i in range(n):
            s1 = self.slides[i]
            if s1 != self.transitionSlide:
                s1.level = i + 1
                for j in range(i + 1, n):
                    s2 = self.slides[j]
                    distance = self.find_distance(s1.x, s1.y, s2.x, s2.y)
                    if distance < s1.minimum and s2 != self.transitionSlide:
                        s1.minimum = distance
                        s1.directSlide = s2

                    if i < self.transitionSlide.level and j + 2 > self.transitionSlide.level:
                        s1.transitions.add(self.transitionPath(i + 1, min(j + 2, n)))

    #draw slides
    def develop(self):
        for s in self.slides:
            if s != self.transitionSlide:
                plt.plot([s.x, self.transitionSlide.x], [s.y, self.transitionSlide.y], color=self.transitionLineColor, alpha=0.3)
                plt.scatter(s.x, s.y, s=200, color=self.slideColor)

            path = self.transitionPath(s.level, s.directSlide.level)
            if path in s.transitions:
                s.directSlide = None #restrict direct path if you can use transition
            elif s.directSlide != s:
                self.directSlides.append(s)
                plt.plot([s.x, s.directSlide.x], [s.y, s.directSlide.y], alpha=0.3, label=s.__str__())

            plt.annotate(s.level,
                    (s.x, s.y), # these are the coordinates to position the label
                    textcoords='offset points', # how to position the text
                    xytext=(0, 0), # distance from text to points (x,y)
                    ha='center',
                    va='center')

    def find_distance(self, x1, y1, x2, y2):
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def transitionPath(self, beginLevel, endLevel):
        return '{} -> {} -> {}'.format(beginLevel, self.transitionSlide.level, endLevel)


class Slide():
    def __init__(self, x, y):
        self.level = None
        self.x = x
        self.y = y
        self.directSlide = self
        self.transitions = set()
        self.minimum = float('inf')

    def __str__(self):
        return '{} -> {}'.format(self.level, self.directSlide.level)
    
    def __repr__(self):
        return str(self)
    
def main(argv):
    sw = SlideWorld()
    if len(argv) > 1:
        sw.maxSlides = int(argv[1])
    if len(argv) > 2:
        sw.maxFeet = int(argv[2])

    sw.design()
    sw.develop()

    plt.plot(0, 0, color=sw.transitionLineColor, label='Transition Slide') #legend item
    plt.scatter(sw.transitionSlide.x, sw.transitionSlide.y, s=200, color=sw.transitionSlideColor, label='Transition Point')

    plt.title('SlideWorld - {:,} ft²'.format(sw.maxFeet**2))
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('slide_world.png', dpi=150)
    
    print('Direct Slides:')
    print(sw.directSlides)
    print('Transition Slides:')
    for i in range(ceil(len(sw.slides) / 2) - 1):
        print(sorted(sw.slides[i].transitions))

if __name__ == '__main__':
    main(argv)
    plt.show()
