import cv2
from mediapipe.tasks.metadata.object_detector_metadata_schema_py_generated import FixedAnchorsSchemaEnd

from Vision.hand import HandDetector

class GestureController:
    def __init__(self):
        """
        Create an instance of HandDetector
        Open webcam cvs.VideoCapture(0)
        Create a variable to store whether flap was detected e.g self.flap_detected = False
        """
        self.detector = HandDetector()
        self.cap = cv2.VideoCapture(0)
        self.flap_requested = False

        

    def update (self, dt):
        """
        Read a frame from the camera
        If frame read fails, do nothing and return
        Process the frame using detector's process_frame() method
        Get Y and Indec Y from the results of detectors emthods
        Cll detect_flap() with wrist and index Y values
        Store the results (true/false) in self.flap_detected

        """
        ret, frame = self.cap.read()
        if not ret:
            self.flap_requested = False
            return

        results = self.detector.process_frame(frame)#processes the frame
        # Now, get positions
        wrist_y = self.detector.get_wrist_y(results)
        index_y = self.detector.get_index_y(results)

        #Detect flap
        self.flap_requested = self.detector.detect_flap(wrist_y, index_y)
         #Shows camera feed with landmarks
        frame = self.detector.draw_landmarks(frame, results)
        cv2.imshow("Gesture Control", frame)
        cv2.waitKey(1)

    def should_flap(self):
        """
        Return true if flap was detected
        Then set it back to false so that the same flap doesnt trigger multiple times

        """
        flap = self.flap_requested
        self.flap_requested = False
        return flap

    def should_start(self):
        """
        return self.should_flap()
        spacebar does both flap and start, so my gestue should do the same

        """
        return self.should_flap()



