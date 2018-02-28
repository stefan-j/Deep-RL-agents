
import tensorflow as tf
import threading
import time
from multiprocessing import cpu_count

import Actor
from Learner import Learner
from Displayer import DISPLAYER
import settings


if __name__ == '__main__':


    tf.reset_default_graph()

    config = tf.ConfigProto(log_device_placement=False,
                            device_count={"CPU":cpu_count(), "GPU":1},
                            inter_op_parallelism_threads=cpu_count())
    
    with tf.Session(config=config) as sess:

        workers = []
        for i in range(settings.NB_ACTORS):
            with tf.device("/device:CPU:"+str(i+1)):
                workers.append(Actor.Actor(sess, i + 1))

        with tf.device("/device:GPU:0"):
            learner = Learner(sess, *workers[0].get_env_features())

        threads = []
        for i in range(settings.NB_ACTORS):
            thread = threading.Thread(target=workers[i].run)
            threads.append(thread)

        threads.append(threading.Thread(target=learner.run))

        try:
            sess.run(tf.global_variables_initializer())
        except:
            raise Exception("The program don't see any GPU available.")

        for t in threads:
            t.start()
        print("Running...")

        try:
            while not Actor.STOP_REQUESTED:
                time.sleep(1)
        except KeyboardInterrupt:
            Actor.request_stop()

        for t in threads:
            t.join()
