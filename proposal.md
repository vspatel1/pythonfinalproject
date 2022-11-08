# Proposal

## What will (likely) be the title of your project?

LightsOut

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

My project will be a game that gives an n x n grid with a light (a block) off or on (as in, it will be assigned 0 or 1, respectively), but which lights are on/off are randomized. The goal of the game is to shut off each light.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

As mentioned above, there will be a randomized n x n grid that has each block at 0 or 1, meaning the light is off or on. The goal is to turn each light off. In the original game, when clicking/inputing a specific light, each light adjacent (but not diaganal) are switched from on to off or off to on. In my version of the game, when a specific light is input, random lights will switch, but not the same lights will switch each input. Although, there will be a pattern of which lights switch, so the game is not pointless and impossible to solve. The game will be executed with command line, or through a UI.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

I will definitely accomplish the grid with on/off lights which switch with an input, and a final outcome with all lights off, which means a win.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

I hope to accomplish a grid with on/off lights which switch with an input in patterns (in other words, a different light switches in each move), so that the game will be harder for the user.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The best outcome for the project is that an easy mode or a hard mode can be chosen, and each will have their own patterns/methods of switching the identity of a light. The best outcome will also feature a UI, such as a window that the user can click on the lights for input.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

The next step for the project will have to be developing the grid. I have already figured out how to give the lights/blocks a random identity: this would be by generating a radom integer between 1 and 10000000, lets say, and then taking that integer and using the modulus operater to get the remainder when divided by 2, giving the light an random identity of 0 or 1.
