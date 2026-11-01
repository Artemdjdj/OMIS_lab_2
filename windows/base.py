from PySide6.QtCore import QEvent, Qt, Signal
from PySide6.QtWidgets import QAbstractButton, QMainWindow, QWidget


class BaseWindow(QMainWindow):
    ui_class = None

    clicked = Signal(object)

    def __init__(self):
        super().__init__()
        self.ui = self.ui_class()
        self.close_handler = None

        self.container = QWidget(self)
        try:
            self.ui.setupUi(self.container)
            self.setCentralWidget(self.container)
            if self.container.windowTitle():
                self.setWindowTitle(self.container.windowTitle())
            if not self.container.size().isEmpty():
                self.resize(self.container.size())
        except AttributeError:
            self.container.deleteLater()
            self.container = None
            self.ui.setupUi(self)

    def accept(self):
        self.close()

    def reject(self):
        self.close()

    def on(self, object_name, signal_name, slot):
        """Подключить сигнал элемента к обработчику по objectName."""
        widget = getattr(self.ui, object_name, None)
        if widget is None:
            print(
                f"[навигация] {type(self).__name__}: в .ui нет объекта "
                f"«{object_name}» — переход не подключён. Проверьте "
                f"objectName в Qt Designer."
            )
            return
        getattr(widget, signal_name).connect(slot)

    def make_clickable(self, widget):
        widget.setCursor(Qt.PointingHandCursor)
        widget.installEventFilter(self)
        for child in widget.findChildren(QWidget):
            child.installEventFilter(self)
            if not isinstance(child, QAbstractButton):
                child.setCursor(Qt.PointingHandCursor)

    def eventFilter(self, obj, event):
        if (
                event.type() == QEvent.Type.MouseButtonRelease
                and not isinstance(obj, QAbstractButton)
        ):
            widget = obj
            while widget is not None:
                click_id = widget.property("clickId")
                if click_id:
                    self.clicked.emit(click_id)
                    return True
                widget = widget.parentWidget()
        return super().eventFilter(obj, event)

    def closeEvent(self, event):
        if self.close_handler is not None:
            event.ignore()
            self.close_handler()
            return
        super().closeEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape and self.close_handler is not None:
            self.close()
            event.accept()
            return
        super().keyPressEvent(event)
