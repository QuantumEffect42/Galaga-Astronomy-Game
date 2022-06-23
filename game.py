import pygame
import constants


class Game(object):
    def __init__(self, screen, states, startState) -> None:
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = constants.FPS
        self.states = states
        self.stateName = startState
        self.state = self.states[self.stateName]

    def eventLoop(self):
        for event in pygame.event.get():
            self.state.getEvent(event)
    
    def flipSate(self):
        nextState = self.state.nextState
        self.state.done = False
        self.stateName = nextState
        self.state = self.states[self.stateName]
        self.state.startup()

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flipSate()
        self.state.update(dt)
    
    def draw(self):
        self.screen.fill((0,0,0))
        self.state.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.eventLoop()
            self.update(dt)
            self.draw()
            pygame.display.update()