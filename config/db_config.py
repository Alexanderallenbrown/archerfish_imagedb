import os

BASE_PATH = "fishdb"
ANNOT_PATH = os.path.sep.join([BASE_PATH,"frame/2019_01_28_09_31_annotations.csv"])
TRAIN_RECORD = os.path.sep.join([BASE_PATH,"records/training.record"])
TEST_RECORD = os.path.sep.join([BASE_PATH,"testing.record"])
CLASSES_FILE = os.path.sep.join([BASE_PATH,"records/classes.pbtxt"])

TEST_SIZE = 0.25

CLASSES = {"archerfish":1}