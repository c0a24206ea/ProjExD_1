import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習8
    tori_img = pg.image.load("fig/3.png")
    tori_img = pg.transform.flip(tori_img, True, False)
    tori_rect = tori_img.get_rect() #rectの抽出　10-1
    tori_rect.center = 300, 200 #こうかとんの初期座標の設定 10-2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tori_rect.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            tori_rect.move_ip((0, +1))
        if key_lst[pg.K_LEFT]:
            tori_rect.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            tori_rect.move_ip((+1, 0))
        x = tmr%3200 #練習9
        screen.blit(bg_img, [-x, 0]) #練習6
        screen.blit(bg_img2, [-x+1600, 0]) #練習7
        screen.blit(bg_img, [-x+3200, 0])
        # screen.blit(tori_img, [300,200])
        screen.blit(tori_img, tori_rect) #tori_rectには300,200の座標が存在
        pg.display.update()
        tmr += 1      
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()