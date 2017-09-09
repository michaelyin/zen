__author__ = 'michael'

import unittest
import numpy as np


from GMM_PY import GMM_py

class TestGMM(unittest.TestCase):
    def setUp(self):
        #self.gmm = GMM_PY('/home/michael/git/seshat/Config/Grammar/sparels.gmm')
        self.gmm = GMM_py('./config/sparels.gmm')

    def test_1(self):
        self.assertTrue(True)
        #{1, -0.295279384, 2.15847778, -3.2263968, -1.95399809, -2.36295772, -0.272880554, -0.136319846, 0.726878583}
        sample = [1, -0.295279384, 2.15847778, -3.2263968, -1.95399809, -2.36295772, -0.272880554, -0.136319846, 0.726878583]
        prob = np.empty(6, dtype=np.float32)
        print '\nprob initial: ', prob

        sample_arr = np.asarray(sample, dtype=np.float32)

        print type(sample_arr)

        posterior = self.gmm.calc_posterior(sample_arr, prob)

        #expected prob values: {1, 0, 0, 1.1423913e-13, 3.1140608e-18, 0}

        print '\nprob', prob

    def test_2(self):
        #{1, 0.076036863, -5.76036873e-05, -0.69550693, -0.0868663564, 0.0869815648, -0.608640552, -0.543317974, 0.391244233}
        sample = [1.0, 0.076036863, -5.76036873e-05, -0.69550693, -0.0868663564, 0.0869815648, -0.608640552, -0.543317974, 0.391244233]
        sample_arr = np.asarray(sample, dtype=np.float32)
        prob = np.empty(6, dtype=np.float32)
        self.gmm.calc_posterior(sample_arr, prob)
        print '\nprob', prob
        #expected prob values: {1, 1.65917154e-19, 1.14943481e-21, 1.64903494e-21, 7.41738851e-24, 0}
        temp = 1.14943481e-21
        dif = temp - prob[2]
        print 'dif: ', dif
        np.testing.assert_almost_equal(prob[2], temp, 28)

    def test_3(self):
        #sample = [1.0, 5.15999985,  1.29999995,  0.47999999,  1.36000001,  1.24000001,-0.83999997,  0.0, 0.12]
        sample = [1.0, 4.15999985,  1.29999995,  0.47999999,  1.36000001,  1.24000001,-0.83999997,  0.0, 0.12]
        sample_arr = np.asarray(sample, dtype=np.float32)
        prob = np.empty(6, dtype=np.float32)
        self.gmm.calc_posterior(sample_arr, prob)
        print '\nprob from python: ', prob

if __name__ == '__main__':
    unittest.main()