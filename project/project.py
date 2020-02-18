import pygame, requests, sys
from PyQt5 import QtWidgets, uic

pygame.init()
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.open_window)
        self.a = True

    def open_window(self):
        self.ll = self.lineEdit.text()
        self.spn = self.lineEdit_2.text()
        schoolproxy = {'http': '10.92.44.120:8080', 'https': '10.92.44.120:8080'}
        width, height = size = 600, 450
        params = {'ll': self.ll,
                  'spn': self.spn, 'l': 'map'}
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=params, proxies=schoolproxy)

        with open("test.png", "wb") as file:
            file.write(response.content)

        screen = pygame.display.set_mode(size)
        screen.fill((255, 255, 255))
        pygame.display.flip()
        screen.blit(pygame.image.load('test.png'), (0, 0))
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass

        pygame.quit()

app = QtWidgets.QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec())

