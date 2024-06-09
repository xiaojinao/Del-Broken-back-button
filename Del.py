import sys

import keyboard
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
                             QMenu, QPushButton, QSystemTrayIcon)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = '键盘映射'
        self.is_listening = False
        self.mapped_key = None
        self.target_key = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(300, 250)
        self.initTrayIcon()
        self.initButtons()
        self.initComboBoxes()

    def initTrayIcon(self):
        # 初始化系统托盘图标和菜单
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('E:\\Python\\retr.ico'))  # 确保图标路径正确
        tray_menu = QMenu()
        exit_action = tray_menu.addAction('退出')
        exit_action.triggered.connect(self.exit_app)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.tray_icon_activated)
        self.tray_icon.show()

    def initButtons(self):
        # 初始化按钮
        self.button = QPushButton('开始监听', self)
        self.button.setToolTip('点击开始')
        self.button.resize(180, 30)
        self.button.move(60, 150)
        self.button.clicked.connect(self.on_click)

    def initComboBoxes(self):
        # 初始化下拉菜单
        self.label_mapped = QLabel('映射按键:', self)
        self.label_mapped.move(60, 30)
        self.comboBox_mapped = QComboBox(self)
        self.comboBox_mapped.addItems(['Del', 'Ctrl', 'Alt', 'Enter', 'Shift', 'Space', 'Backspace'])
        self.comboBox_mapped.move(130, 30)

        self.label_target = QLabel('被映射按键:', self)
        self.label_target.move(60, 80)
        self.comboBox_target = QComboBox(self)
        self.comboBox_target.addItems(['Del', 'Ctrl', 'Alt', 'Enter', 'Shift', 'Space', 'Backspace'])
        self.comboBox_target.move(130, 80)

    @pyqtSlot()
    def on_click(self):
        # 处理按钮点击事件
        try:
            if not self.is_listening:
                self.mapped_key = self.comboBox_mapped.currentText()
                self.target_key = self.comboBox_target.currentText()
                keyboard.add_hotkey(self.mapped_key, lambda: keyboard.press_and_release(self.target_key), suppress=True)
                self.button.setText(f'正在监听 {self.mapped_key} 键')
                self.is_listening = True
            else:
                keyboard.remove_hotkey(self.mapped_key)
                self.button.setText('开始监听')
                self.is_listening = False
                self.mapped_key = None
                self.target_key = None
        except Exception as e:
            print(f"发生错误: {e}")
            self.tray_icon.showMessage('错误', f'发生错误: {e}', QSystemTrayIcon.Critical, 2000)

    def tray_icon_activated(self, reason):
        # 处理托盘图标激活事件
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()

    def closeEvent(self, event):
        # 处理窗口关闭事件
        event.ignore()
        self.hide()
        self.tray_icon.showMessage('运行中', '您的应用程序已最小化到托盘。', QSystemTrayIcon.Information, 2000)

    def exit_app(self):
        # 退出应用程序
        self.tray_icon.hide()
        QCoreApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with app:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
