import sys
from PyQt5.QtWidgets import QApplication
from Core import QtInitialize

app = QApplication(sys.argv)
main_ui = QtInitialize.MainUI()
player_choose_card_ui = QtInitialize.PlayerChooseCardUI()
create_card_info_ui = QtInitialize.CreateCardInfoUI()
adjust_basics_ui = QtInitialize.AdjustBasicsUI()
choose_profession_ui = QtInitialize.ChooseProfessionUI()
choose_professional_skills_ui = QtInitialize.ChooseProfessionalSkillsUI()
add_skill_points_ui = QtInitialize.AddSkillPointsUI()
set_background_ui = QtInitialize.SetBackgroundUI()


def fix_ui_position(ui1, ui2):
    ui1.move(ui2.x(), ui2.y())


def enter_player_mode():
    player_choose_card_ui.show()
    fix_ui_position(player_choose_card_ui, main_ui)
    main_ui.hide()


def enter_create_card_step1():
    create_card_info_ui.show()
    fix_ui_position(create_card_info_ui, player_choose_card_ui)
    player_choose_card_ui.hide()


def enter_create_card_step2():
    if create_card_info_ui.info_complete:
        adjust_basics_ui.get_info_from_last_UI(create_card_info_ui)
        adjust_basics_ui.show()
        fix_ui_position(adjust_basics_ui, create_card_info_ui)
        create_card_info_ui.hide()
        adjust_basics_ui.initialize_UI()


def enter_create_card_step3():
    if adjust_basics_ui.basics_complete:
        choose_profession_ui.get_info_from_last_ui(adjust_basics_ui)
        choose_profession_ui.show()
        fix_ui_position(choose_profession_ui, adjust_basics_ui)
        adjust_basics_ui.hide()


def enter_create_card_step4():
    if choose_profession_ui.profession_complete:
        choose_professional_skills_ui.get_info_from_last_ui(choose_profession_ui)
        choose_professional_skills_ui.show()
        fix_ui_position(choose_professional_skills_ui, choose_profession_ui)
        choose_profession_ui.hide()


def enter_create_card_step5():
    if choose_professional_skills_ui.skills_complete:
        add_skill_points_ui.show()
        fix_ui_position(add_skill_points_ui, choose_professional_skills_ui)
        add_skill_points_ui.get_info_from_last_ui(choose_professional_skills_ui)
        choose_professional_skills_ui.hide()


def enter_create_card_step6():
    if add_skill_points_ui.points_complete:
        set_background_ui.show()
        fix_ui_position(set_background_ui, add_skill_points_ui)
        set_background_ui.get_info_form_last_ui(add_skill_points_ui)
        add_skill_points_ui.hide()


def finish_create_card():
    player_choose_card_ui.show()
    player_choose_card_ui.initialize_list()
    fix_ui_position(player_choose_card_ui, set_background_ui)
    set_background_ui.hide()
    create_card_info_ui.__init__()
    adjust_basics_ui.__init__()
    choose_profession_ui.__init__()
    choose_professional_skills_ui.__init__()
    add_skill_points_ui.__init__()
    set_background_ui.__init__()
    create_card_info_ui.create_card_info_ui.next_step.clicked.connect(enter_create_card_step2)
    adjust_basics_ui.adjust_basics_ui.next_step.clicked.connect(enter_create_card_step3)
    choose_profession_ui.choose_profession_ui.next_step.clicked.connect(enter_create_card_step4)
    choose_professional_skills_ui.choose_professional_skills_ui.next_step.clicked.connect(enter_create_card_step5)
    add_skill_points_ui.add_skill_points_ui.next_step.clicked.connect(enter_create_card_step6)
    set_background_ui.set_background_ui.finish.clicked.connect(finish_create_card)


if __name__ == '__main__':
    main_ui.main_ui.player_mode.clicked.connect(enter_player_mode)
    player_choose_card_ui.player_choose_card_ui.new_card.clicked.connect(enter_create_card_step1)
    create_card_info_ui.create_card_info_ui.next_step.clicked.connect(enter_create_card_step2)
    adjust_basics_ui.adjust_basics_ui.next_step.clicked.connect(enter_create_card_step3)
    choose_profession_ui.choose_profession_ui.next_step.clicked.connect(enter_create_card_step4)
    choose_professional_skills_ui.choose_professional_skills_ui.next_step.clicked.connect(enter_create_card_step5)
    add_skill_points_ui.add_skill_points_ui.next_step.clicked.connect(enter_create_card_step6)
    set_background_ui.set_background_ui.finish.clicked.connect(finish_create_card)

    main_ui.show()
    sys.exit(app.exec_())
