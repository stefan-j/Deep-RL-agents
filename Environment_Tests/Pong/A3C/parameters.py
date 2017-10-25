
ENV = "Pong-v0"

LOAD = False
DISPLAY = True


OPTIMIZER_RATE = 0.99

FRAME_SKIP = 4
FRAME_BUFFER_SIZE = 4

THREADS = 2
LIMIT_RUN_TIME = 10000000

VALUE_REG = 0.5
ENTROPY_REG = 0.01

MAX_GRADIENT_NORM = 40
LEARNING_RATE = 1e-3

MAX_EPISODE_STEP = 10000000
MAX_LEN_BUFFER = 5

DISCOUNT = 0.99
GENERALIZED_LAMBDA = 0.96

CONV = True
LAYERS_SIZE = [8, 8]

LSTM = True
LSTM_CELLS = 256

# Display Frequencies
DISP_EP_REWARD_FREQ = 25
PLOT_FREQ = 100
RENDER_FREQ = 50

SAVE_FREQ = 250
EP_ELONGATION = 500