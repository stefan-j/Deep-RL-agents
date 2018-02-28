
import settings


class Feature:
    nb_column = 0

    def __init__(self, name, settings_freq, text, render_needed=False):
        self.settings_freq = settings_freq
        self.render_needed = render_needed

    def get(self, nb_ep):
        if self.render_needed:
            return False

        return self.settings_freq > 0 and nb_ep % self.settings_freq == 0


STOP = False

ep_reward = Feature('EP REWARD', settings.EP_REWARD_FREQ, 'display')
plot = Feature('PLOT', settings.PLOT_FREQ, 'update', True)
render = Feature('RENDER', settings.RENDER_FREQ, 'render', True)
save = Feature('MODEL SAVER', settings.SAVE_FREQ, 'save')
