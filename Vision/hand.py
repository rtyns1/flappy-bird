#Here, i need to detect
# we use object oriented programming here, so constructors and initiating is needed

import mediapipe as mp
import cv2

class HandDetector:
    def __init__(self):
        """
        Initialises mediapipe hands
        sets up hand tracking parameters
        create variables to store previous positions for movement detection
        """
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode = False,
            max_num_hands = 1,
            min_detection_confidence = 0.7,
            min_tracking_confidence = 0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.prev_wrist_y = None
        self.prev_index_y = None

    def process_frame(self, frame):
        """
        takes a BGR frame from opencv-digital image/vid thwere coloers are represented in BGR instead of RGB
        converts this BGR to RGB because mediapipe needs RGB
        Runs mediapipe hand detection
        returns the results object
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        return results

    def get_wrist_y(self, results):
        """
        Extracts wrist Y coordinate(landmark 0)
        Returns normalized Y value (0-1) or None if no hand
        """
        if results.multi_hand_landmarks:
            first_hand = results.multi_hand_landmarks[0]
            wrist_y = first_hand.landmark[0].y
            return wrist_y
        return None

    def get_index_y(self, results):
        """
        Extract index fingertip y coordinate (landmaek 8)
        returns normalised Y value (0-1) or None if no hand
        """
        if results.multi_hand_landmarks:
            first_hand = results.multi_hand_landmarks[8]
            index_y = first_hand.landmark[0].y
            return index_y
        return None

    def detect_flap(self, wrist_y, index_y):
        """
        Takes current Y positions
        Compares to previous Y positions
        Returns True if upward movement is detected
        Updates previous positions
        """
        current_y = wrist_y if wrist_y is not None else index_y

        if current_y is None:
            return False
        if self.prev_wrist_y is not None:
            delta_y = self.prev_wrist_y - current_y
            if delta_y > 0.05:
                return True
        self.prev_wrist_y = current_y
        return False

    def draw_landmarks(self, frame, results):
        """
        draws dots and lines on hand for debugging
        Shows you waht mediapipe sees
        """
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return frame

    def get_average_y(self, wrist_y, index_y):
        """
        returns average of wrist and index finger
        For smoother tracking
        """
        if wrist_y is None and index_y is None:
            return None
        if wrist_y is None:
            return index_y
        if index_y is None:
            return wrist_y

        return (wrist_y + index_y) / 2





