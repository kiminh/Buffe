import time
from driver import DRIVER

def dispatcher(environment, configuration, trained_model, sn_dir):

    train_mode = not trained_model

    print '... Building controller'
    t0 = time.clock()

    ctrl_optimizer = DRIVER(environment, configuration, trained_model, sn_dir)

    itr = 0

    if train_mode:
        print 'Built controller in %0.2f [min]\n ... Training controller' % ((time.clock()-t0)/60)
    else:
        print 'Built controller in %0.2f [min]\n ... Playing saved model %s' % ((time.clock()-t0)/60 , trained_model)

    while (itr < configuration.n_train_iters):

        # test
        if itr % configuration.test_interval == 0:
            # display a test tranjectory
            ctrl_optimizer.test_step(itr)

            # print info line
            ctrl_optimizer.print_info_line(itr)

            # save snapshot
            if train_mode:
                ctrl_optimizer.save_model(itr)

        # train
        if train_mode:
            ctrl_optimizer.train_step(itr)

        itr += 1