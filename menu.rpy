
screen demomenu:
    on "show" action Play("music", "audio/som_fundo/fato_shadow_-_last_angel.ogg", fadein=1.5, loop=True)
    on "hide" action Stop("music")
    #add Movie(size=(1920, 1080))
    #on "show" action Play("movie", "images/cenario.gif", loop=True)
    #on "hide" action Stop("movie")
    #on "replaced" action Replaced ("movie")
    add im.Scale("gui/deserto.jpeg", 1920, 1080)
    add Movie(size=(1920, 1080), play="gui/cenario1-1.webm")
    add "gui/advita.png" zoom 2.0 xpos 500 ypos 200

    #on "show" action Play("movie", "gui/cenario2-1.gif", loop=True)
    tag menu
    vbox:
        xalign 0.02
        yalign 0.1
        spacing 20
        #imagebutton auto "images/menu/iniciar_%s.png" action ShowMenu("campanha") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        textbutton _("Iniciar")action ShowMenu("campanha") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

        textbutton _("Ajuda")action ShowMenu("helpdemo") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/menu/ajuda_%s.png" action ShowMenu("helpdemo") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

        textbutton _("Preferencias")action ShowMenu("preferencesdemo") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/menu/preferencias_%s.png" action ShowMenu("preferencesdemo") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

        textbutton _("Sobre")action ShowMenu("aboutdemo") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/menu/sobre_%s.png" action ShowMenu("aboutdemo") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

        textbutton _("Sair")action Quit(confirm=False) activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/menu/sair_%s.png" action Quit(confirm=False) activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"


#screen depois de lcicar em load, preferencias e etc...
#imagebutton "images/general_background.png" focus_mask True action ShowMenu("help")    --TESTE Q TALVEZ DE PRA USAR--
screen preferencesdemo():
    tag menu
    add im.Scale("gui/base_deserto.jpg", 1920, 1080) alpha 0.7 xalign 0.5 yalign 0.2 ##para aplicar opacidade na imagem=alpha...
    text " {size=+10} {font=NAPAV.ttf}PREFERENCIAS{/font}{/size}" xalign 0.5 yalign 0.2

    hbox:
        xalign 1.1
        yalign 0.6
        spacing 20
        box_wrap True
        if renpy.variant("pc") or renpy.variant("web"):
             vbox:
                 style_prefix "radio"
                 label _("Display")
                 textbutton _("Window") action Preference("display", "window") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
                 textbutton _("Fullscreen") action Preference("display", "fullscreen") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"




        vbox:
            style_prefix "check"
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
            textbutton _("After Choices") action Preference("after choices", "toggle") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"



        null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"

            vbox:

                label _("Text Speed")

                bar value Preference("text speed")

                label _("Auto-Forward Time")

                bar value Preference("auto-forward time")






            vbox:

                if config.has_music:
                    label _("Music Volume")

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("Sound Volume")

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    label _("Voice Volume")

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
                        style "mute_all_button"


    vbox:  #texbutton voltar
        style_prefix "under"
        textbutton _("Voltar") action ShowMenu("demomenu") pos (25, 980)activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

    ##frame do canto
    vbox:
        #style_prefix "gm_nav"
        xalign 0.02
        yalign 0.2
        spacing 20
        textbutton _("Preferencia") action ShowMenu("preferencesdemo")
        textbutton _("Ajuda") action ShowMenu("helpdemo")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #textbutton _("Save Game") action ShowMenu("save")
        #textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Sobre") action ShowMenu("aboutdemo")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"


screen helpdemo:
    tag menu
    add im.Scale("gui/menuajuda.jpeg", 1920, 1080)alpha 0.5 xalign 0.5 yalign 0.18 ##para aplicar opacidade na imagem=alpha...
    text " {size=+10} {font=NAPAV.ttf}AJUDA{/font}{/size}" xalign 0.5 yalign 0.15
    default device = "keyboard"
    style_prefix "help"

    vbox:
        xalign 0.8#0.7
        yalign 0.5#0.9
        spacing 18

        hbox:
            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3" xpos 200
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3" xpos 300

            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")


        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help



    ##frame do canto
    vbox:
        #style_prefix "gm_nav"
        xalign 0.02
        yalign 0.21
        spacing 20
        textbutton _("Preferencia") action ShowMenu("preferencesdemo")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        textbutton _("Ajuda") action ShowMenu("helpdemo")
        #textbutton _("Save Game") action ShowMenu("save")
        #textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Sobre") action ShowMenu("aboutdemo")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

        vbox:  #texbutton voltar
            style_prefix "under"
            textbutton _("Voltar") action ShowMenu("demomenu") pos (-06, 650)activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"



screen aboutdemo():
    tag menu
    add im.Scale("gui/menusobre.jpeg", 1920, 1080)alpha 0.6 xalign 1.05 yalign 0.19 ##para aplicar opacidade na imagem=alpha...
    text " {size=+10} {font=NAPAV.ttf}SOBRE{/font}{/size}" xalign 1.05 yalign 0.19


    style_prefix "history"
    hbox:
        xpos 400
        yalign 0.4
        spacing 20

        vbox:
            label "[config.name!t]" xpos -610
            text _("Version [config.version!t]\n") ypos 10

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n" ypos 100
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") xpos 250 ypos 200



    ##frame do canto
    vbox:
        #style_prefix "gm_nav"
        xalign 0.02
        yalign 0.2
        spacing 20
        textbutton _("Preferencia") action ShowMenu("preferencesdemo")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        textbutton _("Ajuda") action ShowMenu("helpdemo")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #textbutton _("Save Game") action ShowMenu("save")
        #textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Sobre") action ShowMenu("aboutdemo")

        vbox:  #texbutton voltar
            style_prefix "under"
            textbutton _("Voltar") action ShowMenu("demomenu") pos (-06, 650)activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

###in game menu
screen savedemo():
    tag menu
    add "gui/sobre.png"#alpha 0.6 xalign 1.05 yalign 0.19 ##para aplicar opacidade na imagem=alpha...
    text " {size=+10} {font=NAPAV.ttf}Save{/font}{/size}" xalign 1.05 yalign 0.19

    #use file_slots(_("Save"))


screen loaddemo():
    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
