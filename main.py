import sys
from PyQt5.QtWidgets import QApplication
from Core import QtInitialize

app = QApplication(sys.argv)
main_ui = QtInitialize.MainUI()
player_choose_card_ui = QtInitialize.PlayerChooseCardUI()
create_card_info_ui = QtInitialize.CreateCardInfoUI()


def enter_player_mode():
    player_choose_card_ui.show()
    main_ui.hide()


def enter_create_card_step1():
    create_card_info_ui.show()
    player_choose_card_ui.hide()


if __name__ == '__main__':
    main_ui.main_ui.player_mode.clicked.connect(enter_player_mode)
    player_choose_card_ui.player_choose_card_ui.new_card.clicked.connect(enter_create_card_step1)

    main_ui.show()
    sys.exit(app.exec_())
