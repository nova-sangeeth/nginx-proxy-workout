# -*- coding: UTF-8 -*-
"""
Tests for KPI : Average Absolute Error Percentage
==================================================
This module contains tests for the KPI : Average Absolute Error Percentage for industrial and simulated controller data
"""

import logging

import numpy as np
import numpy.testing as numpy_tests
import pytest as pytest

import cpm.kpi.avg_abs_err as avg_abs_err
import helpers as test_helpers


# List of file-paths to industrial test-data files
INDUSTRIAL_DATA_FILES = test_helpers.get_industrial_data_files()

# List of file-paths to industrial test-configuration files
INDUSTRIAL_CONFIG_FILES = test_helpers.get_industrial_config_files(
    INDUSTRIAL_DATA_FILES
)

# List of controller-names
INDUSTRIAL_CNTRLLR_NAMES = test_helpers.get_cntrllr_ids(INDUSTRIAL_DATA_FILES)

# Get the logger
LOGGER = logging.getLogger(__name__)


class TestAvgAbsErr(object):
    """
    Test class for KPI : Average Absolute Error Percentage
    """

    def display_msg(self):
        """
        Dummy function which does nothing. Only used to print the test-module docstring before any of the tests
        are executed. You CAN consider it a hack/workaround for now

        :return: Nothing
        """
        pass

    @pytest.mark.parametrize(
        "cntrllr_data,cntrllr_id",
        list(zip(INDUSTRIAL_DATA_FILES, INDUSTRIAL_CNTRLLR_NAMES)),
        ids=test_helpers.idfunc_files,
        indirect=["cntrllr_data"],
    )
    def test_avg_abs_err_industrial(
        self, benchmark, cntrllr_data, cntrllr_id, industrial_results
    ):
        """
        Test and benchmark average absolute error percentage kpi using industrial data-set

        :param benchmark: Pytest-benchmark fixture
        :type benchmark: fixture

        :param cntrllr_data: The controller data as a data-frame
        :type cntrllr_data: :class:`pandas.DataFrame`

        :param cntrllr_id: The name of the controller
        :type cntrllr_id: string

        :param industrial_results: The sample_results for the complete set of industrial-data
        :type industrial_results: :class:`pandas.DataFrame`

        :return: Nothing
        :rtype: None
        """

        # Get the required data
        sp = cntrllr_data[test_helpers.SP_KEY].values
        pv = cntrllr_data[test_helpers.PV_KEY].values

        # Compute the kpi while running the benchmark
        result_actual = benchmark(avg_abs_err.compute, pv=pv, sp=sp)[
            avg_abs_err.AVG_ABS_ERR_PERCENT_KEY
        ]

        # Get the expected result
        result_expected = industrial_results.loc[cntrllr_id][
            avg_abs_err.AVG_ABS_ERR_PERCENT_KEY
        ]

        LOGGER.info(
            "Computed value of Average Absolute Error Percentage : %10.10f",
            result_actual,
        )
        LOGGER.info(
            "Expected value of Average Absolute Error Percentage : %10.10f",
            result_expected,
        )

        numpy_tests.assert_allclose(
            result_actual,
            result_expected,
            rtol=test_helpers.FLT_CMP_TOL,
            atol=test_helpers.FLT_CMP_TOL,
        )

    @pytest.mark.xfail(
        reason="Process-Variable is not a floating point array",
        raises=TypeError,
        strict=True,
    )
    def test_invalid_pv_dtype(self):
        """
        Test for the expected failure-scenario of invalid process-variable data-type

        :return: Nothing
        :rtype: None
        """

        # Randomly generate pv, but make it an integer
        pv = np.random.randint(4, size=10).flatten()
        # Randomly generate sp
        sp = np.random.rand(1, 10).flatten()

        # This should fail
        avg_abs_err.compute(pv, sp)

    @pytest.mark.xfail(
        reason="Set-Point-Variable is not a floating point array",
        raises=TypeError,
        strict=True,
    )
    def test_invalid_sp_dtype(self):
        """
        Test for the expected failure-scenario of invalid set-point-variable data-type

        :return: Nothing
        :rtype: None
        """

        # Randomly generate pv
        pv = np.random.rand(1, 10).flatten()
        # Randomly generate sp, but make it an integer
        sp = np.random.randint(4, size=10).flatten()

        # This should fail
        avg_abs_err.compute(pv, sp)

    @pytest.mark.xfail(
        reason="Process-Variable is not a 1D array", raises=ValueError, strict=True
    )
    def test_invalid_pv_shape(self):
        """
        Test for the expected failure-scenario of invalid process-variable array shape

        :return: Nothing
        :rtype: None
        """

        # Randomly generate pv, but give it incorrect shape
        pv = np.random.rand(2, 10)
        # Randomly generate sp
        sp = np.random.rand(1, 10).flatten()

        # This should fail
        avg_abs_err.compute(pv, sp)

    @pytest.mark.xfail(
        reason="Set-Point-Variable is not a 1D array", raises=ValueError, strict=True
    )
    def test_invalid_sp_shape(self):
        """
        Test for the expected failure-scenario of invalid set-point-variable array shape

        :return: Nothing
        :rtype: None
        """

        # Randomly generate pv
        pv = np.random.rand(1, 10).flatten()
        # Randomly generate sp, but give it incorrect shape
        sp = np.random.rand(2, 10)

        # This should fail
        avg_abs_err.compute(pv, sp)

    @pytest.mark.xfail(
        reason="Process-Variable and Set-Point-Variable have unequal lengths",
        raises=ValueError,
        strict=True,
    )
    def test_unequal_pv_sp_size(self):
        """
        Test for the expected failure-scenario where process-variable and set-point-variable signals have unequal
        lengths

        :return: Nothing
        :rtype: None
        """
        # Randomly generate pv, sp but give unequal lengths
        pv = np.random.rand(1, 10).flatten()
        sp = np.random.rand(1, 9).flatten()

        # This should fail
        avg_abs_err.compute(pv, sp)
