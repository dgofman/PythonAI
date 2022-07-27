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

>> python hw5_exercise1.py 5 50

Direct Slides:
[1 -> 2, 4 -> 5]
Transition Slides:
['1 -> 3 -> 4', '1 -> 3 -> 5']
['2 -> 3 -> 4', '2 -> 3 -> 5']

'''

from math import floor 
from sys import argv
import matplotlib.pyplot as plt #Run python -m pip install matplotlib

class SlideWorld():
    def __init__(self):
        self.slides = []
        self.maxSlides = 11
        self.slideColor = 'pink'
        self.transitionSlideColor = 'red'
        self.transitionLineColor = 'y'
        self.directSlides = []
        self.transitionSlides = []
    
    #calculate number of slides using divide-and-conquer algorithm
    def design(self, mid):
        # Big  O(n / 2)
        for i in range(mid):
            index1 = i
            index2 = mid + i
            
            s1 = self.slides[mid] #transition slide  
            s2 = self.slides[index1] #n ->  transition slide 
            s3 = self.slides[index2] #transition slide  -> n

            #add related slides on the left
            s2.directSlide = self.slides[index1 + 1]
            self.directSlides.insert(i, s2)

            if index2 + 1 < self.maxSlides:
                s3.directSlide = self.slides[index2 + 1]
                #add related slides on the right
                self.directSlides.append(s3)

            #direct slides to transition point (left)
            self.addTransition(s2, s1)
            
            if i < mid - 1 and mid + 2 + i < self.maxSlides:
                #slides from transition point (right)
                self.addTransition(s1, self.slides[mid + 2 + i])

            
            for j in range(index1 + 2, mid - 1, 2):
                #find indirect slides on the left
                self.addTransition(self.slides[index1], self.slides[j])

            for j in range(index2 + 3, self.maxSlides, 3):
                if j + 1 < self.maxSlides:
                    #find indirect slides on the right
                    self.addTransition(self.slides[index2 + 1], self.slides[j + 1])

    def addTransition(self, s1, s2):
        if s1.directSlide != s2 and s2.directSlide != s1:
            self.transitionSlides.append([s1, s2])

    #draw slides
    def develop(self, mid):
        for s in self.slides:
            plt.scatter(s.x, s.y, s=200, color=self.slideColor)

            if s.directSlide != None:
                plt.plot([s.x, s.directSlide.x], [s.y, s.directSlide.y], alpha=0.3, label='{} -> {}'.format(s.level, s.directSlide.level))

            plt.annotate(s.level,
                    (s.x, s.y), # these are the coordinates to position the label
                    textcoords='offset points', # how to position the text
                    xytext=(0, 0), # distance from text to points (x,y)
                    ha='center',
                    va='center')

        for slides in self.transitionSlides:
            s1 = slides[0]
            s2 = slides[1]
            if s1.x == s2.x:
                shift = 5
                if s2.level > mid + 2:
                    shift = -5
                plt.plot([s1.x, s2.x - shift, s2.x], [s1.y, s1.y + 5, s2.y], color=self.transitionLineColor, alpha=0.3, label='{} -> {}'.format(s1.level, s2.level))
            else:
                plt.plot([s1.x, s2.x], [s1.y, s2.y], color=self.transitionLineColor, alpha=0.3, label='{} -> {}'.format(s1.level, s2.level))

class Slide():
    def __init__(self, level, x, y):
        self.level = level
        self.x = x
        self.y = y
        self.directSlide = None

    def __str__(self):
        return str(self.level)
    
    def __repr__(self):
        return str(self)
    
def main(argv):
    #create a theme park, 
    sw = SlideWorld()
    if len(argv) > 1:
        sw.maxSlides = int(argv[1])

    mid = floor(sw.maxSlides / 2)

    #dynamically create left and right slides
    for i in range(0, sw.maxSlides):
        x = 10
        y = i
        if i > mid - 1:
            x = 30
            y -= mid
        s = Slide(i + 1, x, (y + 1) * 10)
        sw.slides.append(s)
    
    sw.design(mid)
    sw.develop(mid)

    print('Direct Slides:')
    print(['{} -> {}'.format(s.level, s.directSlide.level) for s in sw.directSlides])

    print('Transition Slides:')
    print(['{} -> {}'.format(s[0].level, s[1].level) for s in sw.transitionSlides])

    print('Number of points:', sw.maxSlides, ' Total slides:', len(sw.directSlides) + len(sw.transitionSlides))

    plt.axis([0, 40, 0, sw.maxSlides / 2 * 10 + 20])   
    plt.title('SlideWorld')
    plt.legend(bbox_to_anchor=(1, 1), ncol=2)
    plt.tight_layout()
    plt.savefig('slide_world.png', dpi=150)

if __name__ == '__main__':
    main(argv)
    plt.show()
