import pyautogui
import time

try:
	while True:
		# Obtenir la position actuelle de la souris
		x, y = pyautogui.position()
		# Afficher les coordonnées
		print(f"Position de la souris: X = {x}, Y = {y}", end="\r")
		# Pause pour éviter d'afficher trop rapidement
		time.sleep(0.5)

except KeyboardInterrupt:
	print("\nProgramme arrêté.")