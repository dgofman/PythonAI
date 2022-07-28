import hw5_exercise2
import hw5_exercise3

for i in range(2, 15):
    sw = hw5_exercise2.init(i)
    slides = hw5_exercise3.main(i)
    directSlides = []
    transitionSlides = []
    for r in range(0, i):
        row = slides[r]
        for c in range(0, len(row)):
            if row[c] == 1:
                if r + 1 == c:
                    directSlides.append([r + 1, c + 1])
                else:
                    transitionSlides.append([r + 1, c + 1])
    
    directSlides1 = str(['{} -> {}'.format(s.level, s.directSlide.level) for s in sw.directSlides])
    directSlides2 = str(['{} -> {}'.format(s[0], s[1]) for s in directSlides])
    if directSlides1 != directSlides2:
        print('Nodes:',  i)
        print('Direct Slides 1 (New):')
        print(directSlides1)
        print('Direct Slides 2 (Old):')
        print(directSlides1)

    transitionSlides1 = str(['{} -> {}'.format(s[0].level, s[1].level) for s in sorted(sw.transitionSlides, key=lambda s: (s[0].level, s[1].level))]) 
    transitionSlides2 = str(['{} -> {}'.format(s[0], s[1]) for s in transitionSlides])
    if transitionSlides1 != transitionSlides2:
        print('Nodes:',  i)
        print('Transition Slides 1 (New):')
        print(transitionSlides1)
        print('Transition Slides 2 (Old):')
        print(transitionSlides2)
