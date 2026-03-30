class GameRenderer:
    """Responsável apenas por desenhas os elementos do jogo na tela."""
    def __init__(self, screen, bg_coplor, ship, bullets, aliens) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passsagem pelo laço."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()

    def _draw_bullets(self) -> None:
        """Desenmha os projéteis na tela."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()   