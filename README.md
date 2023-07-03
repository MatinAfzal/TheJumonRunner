![JummonRunnerBanner](https://github.com/MatinAfzal/TheJumonRunner/assets/128434167/7856597d-ab7f-4f60-8d97-2f8933e0e963)


the jumon runner
It is a game made with pygame library
In this game, the main character named Matin must try to escape from the spells (Jumons) and try to survive.
In making this game, many features of the pygame library and game mechanics have been used
The initial version of this game was programmed by me in 4 days
My main goal was to learn how to work with another Python library better.


## The Jumon Runner
https://github.com/MatinAfzal/TheJumonRunner/assets/128434167/609c74d8-79ee-4ecc-bd0c-04b85530291a




## The challenges I faced
I faced many challenges during this project
I will describe two of the most difficult ones for you:
The first challenge was to be able to process the spritesheet well and cut it into different frames relative to the pixels. In the initial version, the movements of the main character only have 4 frames in 4 directions (up, down, right and left), which Pressing each key will change the frame. In the future, if I have time, I will try to process and place more frames to make the character movement look more natural

The second challenge was to build a mechanism where the Jumons could follow the character on the screen
The solution to build this mechanism is by calculating the distance between the spawned spell (outside the screen) and the main character (inside the screen) and calculating the normalized direction vector.
Finally, you can use that vector to move the spells to the main character at a specified speed


## Requirements
Python 3.10.7 >  https://www.python.org/downloads/  
pygame           https://www.pygame.org/  


## Installation
You can download the execute version (.exe) of JummonRunner from here (recommended) Or you can clone this repository

execute (.exe) download:

OR

Clone of this repository: 

---
    git clone https://github.com/MatinAfzal/TheJumonRunner
---


## Usage

Open cmd:
```
C:\Windows\system32> cd ./<path>/TheJumonRunner

C:\TheJumonRunner> python main.py

```

## Creator
- Created by Matin Afzal
- E-mail: contact.matin@yahoo.com
- Github: [@MatinAfzal](https://www.github.com/MatinAfzal)
