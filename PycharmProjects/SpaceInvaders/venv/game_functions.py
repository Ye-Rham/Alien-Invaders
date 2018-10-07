import sys
from time import sleep

import pygame
from pygame.sprite import Group
import random

from bullet import Bullet
from bullet import AlienBullet
from alien import Alien1
from alien import Alien2
from alien import Alien3

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def alien_bullet(ai_settings, screen, alien, alienbullets):
    new_bullet = AlienBullet(ai_settings, screen, alien)
    alienbullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, high_score_button, ship, aliens1, aliens2, aliens3,
                 bullets, alienbullets, spritesheet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens1, aliens2, aliens3, bullets,
                             alienbullets, mouse_x, mouse_y, spritesheet)
            check_high_score_button(stats, sb, high_score_button, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens1, aliens2, aliens3, bullets, alienbullets,
                      mouse_x, mouse_y, spritesheet):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens1.empty()
        aliens2.empty()
        aliens3.empty()
        alienbullets.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens1, aliens2, aliens3, spritesheet)
        ship.center_ship()

def check_high_score_button(stats, sb, high_score_button, mouse_x, mouse_y):
    button_clicked = high_score_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not sb.highscores_active and not stats.game_active:
        sb.highscores_active = True
    elif button_clicked and sb.highscores_active:
        sb.highscores_active = False

def update_screen(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                  play_button, high_score_button, back_button, title1, title2, title3, alienpoints):

    screen.fill(ai_settings.bg_color)
    sb.show_score()
    if not ship.hit:
        ship.blitme()
    else:
        ship.blithit()
    if pygame.time.get_ticks() % 30 == 0:
        for alien1 in aliens1.sprites():
            alien1.next_frame()
        for alien2 in aliens2.sprites():
            alien2.next_frame()
        for alien3 in aliens3.sprites():
            alien3.next_frame()
        if alien4.active:
            alien4.next_frame()
        if alien4.destroyed:
            if alien4.msgtime % 5 == 0:
                alien4.destroyed = False
                alien4.msgtime += 1
    if alien4.destroyed:
        if alien4.msgtime % 5 != 0:
            alien4.blitdead()
    for alien1 in aliens1.sprites():
        alien1.blitme()
    for alien2 in aliens2.sprites():
        alien2.blitme()
    for alien3 in aliens3.sprites():
        alien3.blitme()
    if alien4.active:
        alien4.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alienbullet in alienbullets.sprites():
        alienbullet.draw_bullet()

    if sb.highscores_active:
        screen.fill(ai_settings.start_color)
        if back_button.rect.collidepoint(pygame.mouse.get_pos()):
            back_button.button_color = ai_settings.button_hover_color
            back_button.text_color = ai_settings.text_hover_color
        else:
            back_button.button_color = ai_settings.button_color
            back_button.text_color = ai_settings.text_color
        for x in range(0, len(stats.high_score_list)):
            sb.show_high_score_list(stats.high_score_list, x)
        title3.draw()
        back_button.draw_button()

    elif not stats.game_active:
        if play_button.rect.collidepoint(pygame.mouse.get_pos()):
            play_button.button_color = ai_settings.button_hover_color
            play_button.text_color = ai_settings.text_hover_color
        elif high_score_button.rect.collidepoint(pygame.mouse.get_pos()):
            high_score_button.button_color = ai_settings.button_hover_color
            high_score_button.text_color = ai_settings.text_hover_color
        else:
            play_button.button_color = ai_settings.button_color
            play_button.text_color = ai_settings.text_color
            high_score_button.button_color = ai_settings.button_color
            high_score_button.text_color = ai_settings.text_color
        screen.fill(ai_settings.start_color)
        title1.draw()
        title2.draw()
        alienpoints.draw()
        play_button.draw_button()
        high_score_button.draw_button()

    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                   spritesheet):
    if pygame.time.get_ticks() % 30:
        for alien1 in aliens1:
            if random.randint(1, 500) == 10:
                alien_bullet(ai_settings, screen, alien1, alienbullets)
        for alien2 in aliens2:
            if random.randint(1, 500) == 10:
                alien_bullet(ai_settings, screen, alien2, alienbullets)
        for alien3 in aliens3:
            if random.randint(1, 500) == 10:
                alien_bullet(ai_settings, screen, alien3, alienbullets)
        if alien4.active:
            if random.randint(1, 25) == 10:
                alien_bullet(ai_settings, screen, alien4, alienbullets)

    bullets.update()
    alienbullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    for alienbullet in alienbullets.copy():
        if alienbullet.rect.bottom >= ai_settings.screen_height:
            alienbullets.remove(alienbullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets,
                                  alienbullets, spritesheet)
    check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets,
                                 alienbullets, spritesheet)

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4,
                                  bullets, alienbullets, spritesheet):
    aliens4 = Group()
    aliens4.add(alien4)
    collisions1 = pygame.sprite.groupcollide(bullets, aliens1, True, True)
    collisions2 = pygame.sprite.groupcollide(bullets, aliens2, True, True)
    collisions3 = pygame.sprite.groupcollide(bullets, aliens3, True, True)
    collisions4 = pygame.sprite.groupcollide(bullets, aliens4, True, True)
    if collisions1:
        for aliens1 in collisions1.values():
            stats.score += ai_settings.alien1_points * len(aliens1)
    elif collisions2:
        for aliens2 in collisions2.values():
            stats.score += ai_settings.alien2_points * len(aliens2)
    elif collisions3:
        for aliens3 in collisions3.values():
            stats.score += ai_settings.alien3_points * len(aliens3)
    elif collisions4:
        alien4.destroy(ai_settings, stats)

    sb.prep_score()
    check_high_score(stats, sb)

    if len(aliens1) == 0 and len(aliens2) == 0 and len(aliens3) == 0:
        bullets.empty()
        alienbullets.empty()
        alien4.destroy(ai_settings, stats)
        stats.score -= alien4.points
        alien4.destroyed = False
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens1, aliens2, aliens3, spritesheet)
        ship.center_ship()

        stats.level += 1
        sb.prep_level()
        sleep(3)

def check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets,
                                 alienbullets, spritesheet):
    ships = Group()
    ships.add(ship)
    collisions = pygame.sprite.groupcollide(ships, alienbullets, False, False)
    if collisions:
        ship_hit(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                 spritesheet)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (1.25 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (1.25 * alien_height))
    return number_rows

def create_alien1(ai_settings, screen, aliens1, alien_number, row_number, spritesheet):
    alien1 = Alien1(ai_settings, screen, spritesheet)
    alien1_width = alien1.rect.width
    alien1.x = alien1_width + 1.25 * alien1_width * alien_number
    alien1.rect.x = alien1.x
    alien1.rect.y = alien1.rect.height + 1.25 * alien1.rect.height * row_number
    aliens1.add(alien1)

def create_alien2(ai_settings, screen, aliens2, alien_number, row_number, spritesheet):
    alien2 = Alien2(ai_settings, screen, spritesheet)
    alien2_width = alien2.rect.width
    alien2.x = alien2_width + 1.25 * alien2_width * alien_number
    alien2.rect.x = alien2.x
    alien2.rect.y = alien2.rect.height + 1.25 * alien2.rect.height * row_number
    aliens2.add(alien2)

def create_alien3(ai_settings, screen, aliens3, alien_number, row_number, spritesheet):
    alien3 = Alien3(ai_settings, screen, spritesheet)
    alien3_width = alien3.rect.width
    alien3.x = alien3_width + 1.25 * alien3_width * alien_number
    alien3.rect.x = alien3.x
    alien3.rect.y = alien3.rect.height + 1.25 * alien3.rect.height * row_number
    aliens3.add(alien3)

def create_fleet(ai_settings, screen, ship, aliens1, aliens2, aliens3, spritesheet):
    alien = Alien1(ai_settings, screen, spritesheet)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(int(number_rows/3)):
        for alien_number in range(number_aliens_x):
            create_alien3(ai_settings, screen, aliens3, alien_number, row_number, spritesheet)
    for row_number in range(int(number_rows/3), int(number_rows*2/3)):
        for alien_number in range(number_aliens_x):
            create_alien2(ai_settings, screen, aliens2, alien_number, row_number, spritesheet)
    for row_number in range(int(number_rows*2/3), int(number_rows)):
        for alien_number in range(number_aliens_x):
            create_alien1(ai_settings, screen, aliens1, alien_number, row_number, spritesheet)


def check_fleet_edges(ai_settings, aliens1, aliens2, aliens3):
    check = 0
    for alien1 in aliens1.sprites():
        if alien1.check_edges():
            check = 1
            break
    if check != 1:
        for alien2 in aliens2.sprites():
            if alien2.check_edges():
                check = 1
                break
    if check != 1:
        for alien3 in aliens3.sprites():
            if alien3.check_edges():
                check = 1
                break
    if check == 1:
        change_fleet_direction(ai_settings, aliens1, aliens2, aliens3)

def change_fleet_direction(ai_settings, aliens1, aliens2, aliens3):
    for alien1 in aliens1.sprites():
        alien1.rect.y += ai_settings.fleet_drop_speed
    for alien2 in aliens2.sprites():
        alien2.rect.y += ai_settings.fleet_drop_speed
    for alien3 in aliens3.sprites():
        alien3.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                  spritesheet):
    check_fleet_edges(ai_settings, aliens1, aliens2, aliens3)
    aliens1.update()
    aliens2.update()
    aliens3.update()
    if alien4.active == True:
        alien4.update()
        if alien4.rect.left == alien4.screen_rect.right:
            alien4.destroy(ai_settings, stats)
            stats.score -= alien4.points
            alien4.destroyed = False

    if pygame.sprite.spritecollideany(ship, aliens1) or pygame.sprite.spritecollideany(ship, aliens2) or \
            pygame.sprite.spritecollideany(ship, aliens3):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                 spritesheet)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                        spritesheet)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
             spritesheet):
    ship.hit = True
    for x in range(1, 11):
        update_screen(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                      x, x, x, x, x, x, x)
        sleep(0.1)

    if stats.ships_left > 0:
        stats.ships_left -= 1

        sb.prep_ships()

        aliens1.empty()
        aliens2.empty()
        aliens3.empty()
        alien4.destroy(ai_settings, stats)
        stats.score -= alien4.points
        alien4.destroyed = False
        alienbullets.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens1, aliens2, aliens3, spritesheet)
        ship.center_ship()

        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        for x in range(0, len(stats.high_score_list)):
            if stats.score > stats.high_score_list[x]:
                stats.high_score_list.insert(x, stats.score)
                stats.high_score_list.pop()
                break
        high_score_file = open("High_Scores.txt", "w")
        for x in range (0, len(stats.high_score_list) - 1):
            high_score_file.write(str(stats.high_score_list[x]) + "\n")
        high_score_file.write(str(stats.high_score_list[8]))
        high_score_file.close()
        print(list(map(str, stats.high_score_list)))

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                        spritesheet):
    screen_rect = screen.get_rect()
    for alien1 in aliens1.sprites():
        if alien1.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                     spritesheet)
            break
    for alien2 in aliens2.sprites():
        if alien2.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                     spritesheet)
            break
    for alien3 in aliens3.sprites():
        if alien3.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                     spritesheet)
            break
