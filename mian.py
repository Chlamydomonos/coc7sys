import sys
from PyQt5.QtWidgets import QApplication
from Core import QtInitialize

app = QApplication(sys.argv)
main_ui = QtInitialize.MainUI()
player_choose_card_ui = QtInitialize.PlayerChooseCardUI()
create_card_info_ui = QtInitialize.CreateCardInfoUI()
adjust_basics_ui = QtInitialize.AdjustBasicsUI()


def enter_player_mode():
    player_choose_card_ui.show()
    main_ui.hide()


def enter_create_card_step1():
    create_card_info_ui.show()
    player_choose_card_ui.hide()


def enter_create_card_step2():
    if create_card_info_ui.info_complete == 1:
        adjust_basics_ui.get_info_from_last_UI(create_card_info_ui)
        adjust_basics_ui.show()
        create_card_info_ui.hide()
        adjust_basics_ui.initialize_UI()


if __name__ == '__main__':
    main_ui.main_ui.player_mode.clicked.connect(enter_player_mode)
    player_choose_card_ui.player_choose_card_ui.new_card.clicked.connect(enter_create_card_step1)
    create_card_info_ui.create_card_info_ui.next_step.clicked.connect(enter_create_card_step2)

    main_ui.show()
    sys.exit(app.exec_())
