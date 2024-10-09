
import time
import win32api, win32con
import keyboard
def run():
    # Position du curseur de la souris
    x, y = 821, 52000  # Ajuste les coordonnées selon ton jeu

    # Fonction pour effectuer un clic gauche
    def click(x, y):
        # win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.01)  # Petite pause
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    # Boucle pour effectuer plusieurs clics
    try:
        while True:
            click(x, y)
            time.sleep(0.3)  # Intervalle entre les clics
            if keyboard.is_pressed('esc'):
                print("\nProgramme arrêté.")
                break
    except KeyboardInterrupt:
        print("Auto-clicker arrêté.")

if __name__ == "__main__":
    time.sleep(2)
    run()