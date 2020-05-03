import sys
from PyQt5.QtWidgets import QApplication
from Core import QtInitialize

app = QApplication(sys.argv)
main_ui = QtInitialize.MainUI()
player_choose_card_ui = QtInitialize.PlayerChooseCardUI()


def enter_player_mode():
    player_choose_card_ui.show()
    main_ui.hide()


if __name__ == '__main__':
    main_ui.main_ui.player_mode.clicked.connect(enter_player_mode)

    main_ui.show()
    sys.exit(app.exec_())
