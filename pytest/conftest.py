# -*- coding: UTF-8 -*-
"""
Pytest Session/Module Scoped Fixtures
======================================

This module contains fixtures that are shareable across the entire test-suite at a session or module scope.
Automatically discovered by pytest during test-runs

"""
import json
import logging
import os
import pathlib
import shutil

import numpy as np
import pandas as pd
import pytest

import tests.helpers as test_helpers


# Get the logger
LOGGER = logging.getLogger()

# General temporary directory
_TEMP_GEN = "pytest_tmp_dir"

# Temporary directory name to use for controller data
_TEMP_DIR_DATA_NAME = "pytest_tmp_dir_data"

# Temporary directory name to use for controller configurations
_TEMP_DIR_CONFIG_NAME = "pytest_tmp_dir_configs"

# Temporary directory name to use for controller results
_TEMP_DIR_RESULTS_NAME = "pytest_tmp_dir_results"

# Data-type for controller variables
_CNTRLLR_DTYPES = {"OP": np.float64, "PV": np.float64, "SP": np.float64}

# Default mode value to use for all industrial/simulated data
_DEFAULT_MODE_VAL = "LOOP_MODE_AUTO"

# Data-type for results
_RESULTS_FILE_DTYPE_MAP = {

    "AVG_ABS_ERR_PERCENT": np.float64,
    "CONTROL_ELEMENT_TRAVEL_PER_HR": np.float64,
    "CONTROL_ELEMENT_REVERSALS_PER_HR": np.float64,
    "VARIABILITY_INDEX": np.float64,
    "DATA_COMPRESSION_FACTOR": np.float64,
    "HURST_INDEX": np.float64,
    "SERVICE_FACTOR": np.float64,
    "PV_MIN": np.float64,
    "PV_MAX": np.float64,
    "PV_MEAN": np.float64,
    "PV_MEDIAN": np.float64,
    "PV_STD_DEV": np.float64,
    "SP_MIN": np.float64,
    "SP_MAX": np.float64,
    "SP_MEAN": np.float64,
    "SP_MEDIAN": np.float64,
    "SP_STD_DEV": np.float64,
    "OP_MIN": np.float64,
    "OP_MAX": np.float64,
    "OP_MEAN": np.float64,
    "OP_MEDIAN": np.float64,
    "OP_STD_DEV": np.float64,
    "HIGH_LIMIT_SATURATION_PERCENT": np.float64,
    "LOW_LIMIT_SATURATION_PERCENT": np.float64,
    "TOTAL_SATURATION_PERCENT": np.float64,
    "PERCENTAGE_OVERSHOOT": np.float64,
    "OSCILLATIONS_PV": np.bool,
    "OSCILLATION_STATUS": np.str,
    "MINIMUM_OSCILLATION_PERIOD": np.float64,
    "MAXIMUM_OSCILLATION_PERIOD": np.float64,
    "DOMINANT_OSCILLATION_PERIOD": np.float64,
    "OVERALL_HEALTH": np.str,
    "OVERALL_SATURATION": np.str,
    "OVERALL_UTILIZATION": np.str,
    "OVERALL_DIAGNOSIS": np.str

}


@pytest.fixture(scope="module", autouse=True)
def display_docstring(request):
    """
    Fixture to print the docstring of the module being tested

    :return: Nothing
    :rtype: None
    """
    try:
        cols, _ = os.get_terminal_size()
    except:
        cols = 25

    print("\n")
    print("*" * cols)
    print(request.module.__doc__)
    print("\n")

    yield

    print("\n")
    print("*" * cols)


@pytest.fixture()
def gen_file(tmpdir, request):
    """
    Fixture which performs the following actions

    * Uses the built-in py-test fixture tmpdir to create a temporary directory
    * Inspects the request for the file path to a data-file
    * Performs a copy of the data file over to the temporary directory
    * Provides the fully qualified path of the copy of the file in the temporary directory

    """
    # Create a tmp directory and copy these files over (if it doesn't exist already)
    temp_dir = tmpdir.mkdir(_TEMP_GEN)

    # Copy the file over
    # Note : request.param will point to the file-path as it is the test-parameter being passed to this fixture
    shutil.copy(request.param, str(temp_dir))

    # Use path-lib to get the file-name
    file_name = str(pathlib.PurePath(request.param).name)

    return str(os.path.join(str(temp_dir), file_name))


@pytest.fixture()
def cntrllr_data(tmpdir, request):
    """
    Fixture which performs the following actions

    * Uses the built-in py-test fixture tmpdir to create a temporary directory
    * Inspects the request for the file path to a data-file
    * Performs a copy of the data file over to the temporary directory
    * Reads the csv data-file as a dataframe

    """
    # Create a tmp directory and copy these files over
    temp_dir = tmpdir.mkdir(_TEMP_DIR_DATA_NAME)

    # Copy the file over
    # Note : request.param will point to the file-path as it is the test-parameter being passed to this fixture
    shutil.copy(request.param, str(temp_dir))

    # Use path-lib to get the file-name
    file_name = str(pathlib.PurePath(request.param).name)

    # Full-file path
    full_path = str(os.path.join(str(temp_dir), file_name))

    # Read the closed loop controller data as a data-frame
    closed_loop_data = pd.read_csv(full_path, dtype=_CNTRLLR_DTYPES)

    # Inject mode column
    closed_loop_data = closed_loop_data.assign(MODE=lambda row: _DEFAULT_MODE_VAL)

    # Return the data-frame
    return closed_loop_data


@pytest.fixture()
def cntrllr_config(tmpdir, request):
    """
    Fixture which performs the following actions

    * Uses the built-in py-test fixture tmpdir to create a temporary directory
    * Inspects the request for the file path to a data-file
    * Performs a copy of the data file over to the temporary directory
    * Reads the json data file as a dictionary
    """
    # Create a tmp directory and copy these files over
    temp_dir = tmpdir.mkdir(_TEMP_DIR_CONFIG_NAME)

    # Copy the file over
    # Note : request.param will point to the file-path as it is the test-parameter being passed to this fixture
    shutil.copy(request.param, str(temp_dir))

    # Use path-lib to get the file-name
    file_name = str(pathlib.PurePath(request.param).name)

    # Full-file path
    full_path = str(os.path.join(str(temp_dir), file_name))

    with open(full_path, 'r') as config_file:
        config_dict = json.load(config_file)

    # Change sampling interval to float
    config_dict[test_helpers.SAMPLE_INTERVAL_KEY] = float(config_dict[test_helpers.SAMPLE_INTERVAL_KEY])
    # Change error percent to float
    config_dict[test_helpers.ERR_BAND_KEY] = float(config_dict[test_helpers.ERR_BAND_KEY])

    return config_dict


@pytest.fixture(scope="session", autouse=True)
def industrial_results(tmpdir_factory):
    """
    Fixture for loading the sample_results of industrial test-data into the test-scope

    * Uses the built-in py-test fixture tmpdir_factory to create a temporary directory
    * Performs a copy of the industrial test-sample_results data-file over to the temporary directory
    * Reads the file as a data-frame and returns it
    """
    # Create a tmp directory and copy the results file over
    temp_dir = tmpdir_factory.mktemp(_TEMP_DIR_RESULTS_NAME, numbered=True)

    # Get the industrial data-set results file
    results_file = test_helpers.get_industrial_results_file()

    # Copy the file over
    shutil.copy(str(results_file), str(temp_dir))

    # Use path-lib to get the file-name
    file_name = str(pathlib.PurePath(str(results_file)).name)

    # Full-file path
    full_path = str(os.path.join(str(temp_dir), file_name))

    # Parse it as a data-frame and return it
    res_df = pd.read_csv(filepath_or_buffer=full_path, index_col=0, dtype=_RESULTS_FILE_DTYPE_MAP)

    return res_df


# ADDING FIXTURE FOR SIMULATED DATA
@pytest.fixture(scope="session", autouse=True)
def simulated_results(tmpdir_factory):
    """
    Fixture for loading the sample_results of simulated test-data into the test-scope

    * Uses the built-in py-test fixture tmpdir_factory to create a temporary directory
    * Performs a copy of the industrial test-sample_results data-file over to the temporary directory
    * Reads the file as a data-frame and returns it
    """
    # Create a tmp directory and copy the results file over
    temp_dir = tmpdir_factory.mktemp(_TEMP_DIR_RESULTS_NAME, numbered=True)

    # Get the simulated data-set results file
    results_file = test_helpers.get_simulated_results_file()

    # Copy the file over
    shutil.copy(str(results_file), str(temp_dir))

    # Use path-lib to get the file-name
    file_name = str(pathlib.PurePath(str(results_file)).name)

    # Full-file path
    full_path = str(os.path.join(str(temp_dir), file_name))

    # Parse it as a data-frame and return it
    res_df = pd.read_csv(filepath_or_buffer=full_path, index_col=0, dtype=_RESULTS_FILE_DTYPE_MAP)

    return res_df
