# mostly taken from demo example as example test file
from intro_to_wc_modeling.concepts_skills.software_engineering.unit_testing import core
import unittest
import capturer
import numpy as np

class TestSimulation(unittest.TestCase):
    class NewClass():
        pass

    # execute code which don't need to be rerun over and over again
    @classmethod
    def setUpClass(cls):
        """ Code to execute before all of the tests. For example, this can be used to create temporary
        files.
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """ Code to execute after all of the tests. For example, this can be used to clean up temporary
        files.
        """
        pass

    def setUp(self):
        """ Code to execute before each test. """
        pass

    def tearDown(self):
        """ Code to execute after each test. """
        pass

    def test_run(self):
        self.NewClass

        # run code, where main class to test is Simulation
        sim = core.Simulation()
        hist = sim.run(time_max=5)

        # check whether hist is the correct object
        self.assertIsInstance(hist,Trajectory)

        # check timepoints (length)
        np.testing.assert_equal(hist.times, numpy.arange(0., 6.,.1.)

        # check timepoints (positive/negative)
        # np.all tests whether all array elements evaluate to True
        self.assertTrue(np.all(hist.values >= 0))

    def test_statistics(self):
        sim = core.Simulation()

        time_max = 100
        n_sample = 100

        # np.full fill matrix with whatever parameter provided
        # basically initiated a random/empty matrix
        values = np.full((time_max + 1, n_sample),np.nan)

        for i in range(n_sample):
            hist = sim.run(value_init=5,time_max)
            # store entire column as simulated results from hist each time
            values[:,i] = hist.values

        # see if objects (initial value 5 and mean of simulated data)
            # within rtol tolerance levels
        np.testing.assert_allclose(np.mean(values[:]), 5, rtol=0.1)

    # test standard output
    def test_stdout(self):
        sim = core.Simulation()

        with capturer.CaptureOutput() as captured:
            sim.run()
            stdout = captured.get_text()
            lines = stdout.rstrip().split('\n)
            # makes sure each line matches something
            for line in lines:
                self.assertRegex(line, "^Time \d+: \d+ molecules$")

    def test_invalid_inputs(self):
        sim = core.Simulation()

        with self.assertRaisesRegex(ValueError, '`value_init` must be a non-negative integer'):
            sim.run(value_init=-1, time_max=10)

        with self.assertRaisesRegex(ValueError, '`time_max` must be a non-negative integer'):
            sim.run(value_init=4, time_max=-1)

    def test_trajectory_exception(self):
        with self.assertRaisesRegex(ValueError, '`time_max` must be a non-negative integer'):
            core.Trajectory(-1)

        with self.assertRaisesRegex(ValueError, '`time_max` must be a non-negative integer'):
            core.Trajectory(1.5)


                                          
