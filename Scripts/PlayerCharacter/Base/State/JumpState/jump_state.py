from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
class JumpState(CharacterState):
  #base function
  def enter(self):
    super().enter()
    print("Enter Jump")
    self.state_machine.character.need_reset_jumpkey = True

  def exit(self):
    super().exit()
    print("Exit Jump")

  def update(self):
    super().update()
    #check state
    self.on_fall()
    self.on_idle()


    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.MOVE_SPEED_MODIFIER)
    self.move_vertical(GameConstants.BASE_JUMP_FORCE,GameConstants.JUMP_FORCE_MODIFIER)


    #animation
    self.update_sprite_animation(self.state_machine.character.jump_spritesheet,GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[2],False)


  
  # animation
  def draw(self, surface):
    img = pygame.transform.flip(self.state_machine.character.jump_spritesheet[self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x, self.state_machine.character.rect.y))