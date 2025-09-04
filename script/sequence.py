import pyautogui
import time
import keyboard
from script.gameBase import GameBase

class Sequence(GameBase):
    def __init__(self) -> None:
        self.start_coords = (0,0)
        self.start_is_found = False
        self.score = 0
        self.list_input_slots = []
        self.list_input_event = []
        self.initial_color = (0,0,0)
        time.sleep(5)

    def check_colors(self) -> None:
        time.sleep(0.001)
        found_coord = (0,0)
        for i in range(len(self.list_input_slots)) :
            coords = self.list_input_slots[i]
            if pyautogui.pixel(int(coords[0]), int(coords[1])) != self.initial_color :
                found_coord = coords
                self.list_input_event.append(i)
                while pyautogui.pixel(int(coords[0]), int(coords[1])) != self.initial_color :
                    if keyboard.is_pressed("p") : exit()
                    time.sleep(0.001)
                    pass

    def click_buttons(self) -> None:
        for i in self.list_input_event :
            coords = self.list_input_slots[i]
            pyautogui.click(coords[0], coords[1])

            while pyautogui.pixel(int(coords[0]), int(coords[1])) != self.initial_color :
                time.sleep(0.01)
                pass

        self.list_input_event.clear()
                



    def start(self) -> bool:
        try : 
            self.start_coords = pyautogui.locateCenterOnScreen("./img/start.png", confidence=0.8)
            self.start_is_found = not self.start_coords == None
            return self.start_is_found
        except Exception as e :
            print(e.with_traceback(e.__traceback__))
            return False
        
    def set_settings(self) -> bool: 
        if not self.start_is_found : return False

        pyautogui.click(self.start_coords[0], self.start_coords[1])

        try: 

            boxes = []
            for box in  list(pyautogui.locateAllOnScreen("./img/sequence_button.png", confidence=0.98)) :
                is_duplicate = False

                for ubox in boxes:
                    if abs(box.left - ubox.left) < 10 and abs(box.top - ubox.top) < 10:
                        is_duplicate = True
                        break

                if not is_duplicate:
                    boxes.append(box)

            self.list_input_slots = [(box.left + box.width // 2, box.top + box.height // 2) for box in boxes]
            self.initial_color = pyautogui.pixel(int(boxes[0].left + boxes[0].width // 2), int(boxes[0].top + boxes[0].height // 2))
            return True
        except Exception as e:
            print(e.with_traceback(e.__traceback__))
            return False
        

    def play(self) -> None:
        while True :
            if keyboard.is_pressed("p") : exit()
            self.check_colors()
            if len(self.list_input_event) == self.score + 1 :
                self.click_buttons()
                self.score += 1
           

if __name__ == "__main__":
    seq = Sequence()
    seq.start()
    seq.set_settings()
    seq.play()