import time
import win32api

try:
	while True:
		# Obtenir la position actuelle de la souris avec win32api
		x, y = win32api.GetCursorPos()
		# Afficher les coordonnées
		print(f"Position de la souris: X = {x}, Y = {y}", end="\r")
		time.sleep(0.1)

except KeyboardInterrupt:
	print("\nProgramme arrêté.")