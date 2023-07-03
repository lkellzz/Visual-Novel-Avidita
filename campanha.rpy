screen campanha:

    add "images/background_prancheta_caps.png"
    text"{size=+15} {font=NAPAV.ttf}CAMPANHA{/font}{/size}"xalign 0.1 yalign 0.12

    #add "images/campanha_idle.png" xalign 0.13 yalign 0.11
    #add "images/capitulos_hover.png" xalign 0.14 yalign 0.4
    tag menu

    vbox:
        xalign 0.14
        yalign 0.5
        spacing 150
        textbutton _("{size=+10}Capitulos{/size}")action [ShowMenu("capitulos"), Stop("movie")]xpos -40 ypos -30 activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/capitulos_%s.png" action ShowMenu("capitulos") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

        textbutton _("{size=+10}Voltar{/size}")action [Hide("capitulos"), Show("demomenu")]xpos -20 ypos -30 activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

        #imagebutton auto "images/voltar_%s.png" action [ Hide ("capitulos"), Show ("demomenu") ] activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"



##teste para o pull request q eu n to sabenod fazer ;-;
screen capitulos:
    add "images/forma.png" xalign 0.5 yalign 0.2
    add im.Scale("images/campdistante.png", 360, 260) xalign 0.5 yalign 0.21#imagem do primeiro capitulo
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 10
        textbutton _("{size=+2}Start{/size}")action Start("start")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/comece_%s.png" action Start("start") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
###capitulo 1<<<<<<<<<<<<<<<<<<
    hbox:
        vbox:
            xpos 1350
            ypos 200
            spacing 10
            text"{size=+6}{font=army.ttf}Capitulo 1{/font}{/size}"
            text"O começo de uma grande jornada" xpos -150 ypos 20
            text"em busca de respostas."xpos -100
            #serve para fixar mensagem onde quiser
            #fixed:
            #    text "Are you sure?" xalign 0.5 yalign 0.3

            #xpos 500 ypos -300
###capitulo 2
    add "images/forma.png" xalign 0.908 yalign 0.8102
    add im.Scale("images/acampamento_sala.jpeg", 360, 260) xalign 0.9 yalign 0.8#imagem do primeiro capitulo
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 10
        textbutton _("{size=+2}Start{/size}")action Start("start")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/comece_%s.png" action Start("start") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

    hbox:
        vbox:
            xpos 1000
            ypos 700
            spacing 10
            text"{size=+6}{font=army.ttf}Capitulo 2{/font}{/size}" xpos -90
            text"Agora com o caminho ficando mais" xpos -250 ypos 25
            text"pedregoso, você perceberá que nem" xpos -252 ypos 14
            text"tudo é oque parece ser." xpos -150
