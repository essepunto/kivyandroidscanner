from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.camera import Camera
from pyzbar.pyzbar import decode
from PIL import Image as PILImage
from kivy.clock import Clock
import io


class BarcodeScannerApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        # Главный экран
        self.main_screen = Screen(name='main')
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        scan_button = MDRaisedButton(
            text="Start Scanning",
            pos_hint={"center_x": 0.5},
            on_release=self.go_to_scan_screen
        )
        main_layout.add_widget(scan_button)
        self.main_screen.add_widget(main_layout)
        self.screen_manager.add_widget(self.main_screen)

        # Экран сканирования
        self.scan_screen = Screen(name='scan')
        scan_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.camera = Camera(play=True)
        self.camera.resolution = (640, 480)  # Может потребоваться настройка
        scan_layout.add_widget(self.camera)

        # Список для отображения отсканированных кодов
        self.codes_list = MDList()
        self.scanned_barcodes = set()  # Для хранения уникальных отсканированных кодов
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height / 3))
        scroll_view.add_widget(self.codes_list)
        scan_layout.add_widget(scroll_view)

        # Кнопка очистки списка
        clear_button = MDRaisedButton(
            text="Clear List",
            size_hint_y=None,
            height='48dp',
            on_release=self.clear_list
        )
        scan_layout.add_widget(clear_button)

        self.scan_screen.add_widget(scan_layout)
        self.screen_manager.add_widget(self.scan_screen)

        return self.screen_manager

    def go_to_scan_screen(self, instance):
        self.screen_manager.current = 'scan'
        Clock.schedule_interval(self.auto_scan_barcode, 1)  # Автоматическое сканирование каждую секунду

    def auto_scan_barcode(self, dt):
        self.camera.export_to_png("temp.png")  # Сохранение кадра в файл
        self.decode_barcode()

    def decode_barcode(self):
        image = PILImage.open("temp.png")
        decoded_objects = decode(image)

        if decoded_objects:
            for obj in decoded_objects:
                barcode_data = obj.data.decode("utf-8")
                if barcode_data not in self.scanned_barcodes:
                    self.scanned_barcodes.add(barcode_data)
                    self.codes_list.add_widget(OneLineListItem(text=barcode_data))

    def clear_list(self, instance):
        self.codes_list.clear_widgets()
        self.scanned_barcodes.clear()


if __name__ == "__main__":
    BarcodeScannerApp().run()
#