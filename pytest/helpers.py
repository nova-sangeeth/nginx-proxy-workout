# -*- coding: UTF-8 -*-
"""
Helper functions
===================

Module contains useful helper functions required for running the test cases

"""
import os as os
import pathlib as pathlib


# Directory name where test-data resides
_TEST_DATA_DIR = "data"

# Directory name where industrial test-data resides
_INDUSTRIAL_DATA_DIR = "industrial"

# Directory name where closed-loop controller data resides
_CNTRLLR_DATA_DIR = "cntrllr_data"

# Directory name where industrial test-data resides
_SIMULATED_DATA_DIR = "simulated"

# Directory name where closed-loop controller configurations reside
_CNTRLLR_CONFIG_DIR = "configs"

# Directory name where closed-loop controller results reside
_CNTRLLR_RESULTS_DIR = "results"

# File pattern for data-files
FILE_PATTERN_DATA_FILES = ".csv"

# File pattern for configuration files
FILE_PATTERN_CONFIG_FILES = ".json"

# File pattern for results files
FILE_PATTERN_RESULTS_FILES = ".csv"

# Keys for controller data
OP_KEY = "OP"
PV_KEY = "PV"
SP_KEY = "SP"
MODE_KEY = "MODE"

# Keys for controller configuration

OP_MIN_KEY = "OP_MIN"
OP_MAX_KEY = "OP_MAX"
PV_MIN_KEY = "PV_MIN"
PV_MAX_KEY = "PV_MAX"
ERR_BAND_KEY = "ACCEPTABLE_ERROR_BAND_PERCENTAGE"
SAMPLE_INTERVAL_KEY = "SAMPLING_INTERVAL"
OUTLIER_DETECT_KEY = "IS_OUTLIER_DETECTION_ON"

# Default floating point comparison tolerance
FLT_CMP_TOL = 1.0E-9


def fetch_file_paths(file_name_pattern, dir_arr):
    """
    Fetch file paths which match the provided file name pattern and present at the
    given path array

    :param file_name_pattern: The file name pattern as a string i.e. only fetches file with the given pattern in the
                              file name
    :type file_name_pattern: string

    :param dir_arr: The list of directory names in the order in which they are nested
    :type dir_arr: list

    :return: A list of file paths
    :rtype: list
    """

    # Get the path where the script is being executed
    here = os.path.dirname(__file__)

    # Create the full path
    file_dir = os.path.join(here, *dir_arr)

    # Scan all the files and get only those files which match the pattern
    file_paths = [os.path.join(file_dir, str(file)) for file in os.listdir(file_dir) if file_name_pattern in str(file)]

    return file_paths


def fetch_corresponding_configs(data_file_paths, dir_arr, config_file_extn):
    """
    Fetch corresponding configuration file paths to the provided list of data-file paths

    :param data_file_paths: A list of paths to closed-loop controller data files
    :type data_file_paths: list

    :param dir_arr: The list of directory names in the order in which they are nested (to find the configuration files)
    :type dir_arr: list

    :param config_file_extn: The file-extension of configuration files
    :type config_file_extn: string

    """
    # Initialize an array of config paths
    config_paths = [None] * len(data_file_paths)

    # Get the path where the script is being executed
    here = os.path.dirname(__file__)

    # Iterate over the data-file paths
    for indx, data_file_path in enumerate(data_file_paths):
        # Get the data-file name alone using pure-path
        pure_path = pathlib.PurePath(data_file_path)

        # Get the name of the file without the file-format extension
        file_name = str(pure_path.stem)

        # Append the config file extension
        file_name += config_file_extn

        # Construct the full-file path
        file_path = os.path.join(here, *dir_arr, file_name)

        # Push it in to the array of config paths
        config_paths[indx] = str(file_path)

    return config_paths


def idfunc_files(fixture_val):
    """
       Test id generator when the fixture loads file-paths

       :param fixture_val: The fixture value, which is a file-path as str or any other value
       :type fixture_val: object

       :return: An id for the test or
       :rtype: Union[string,None]

       """
    # generating automatic id when fixture_val is not a file path
    if not issubclass(type(fixture_val), str):
        return None

    if not os.path.isfile(fixture_val):
        # id creation if string is not a valid file path
        return None

    # Construct a pure-path from the fixture value which itself is a path
    pure_path = pathlib.PurePath(fixture_val)

    file_name = str(pure_path.name)
    return file_name.upper()


def get_industrial_results_file():
    """
    Get the path to the industrial data-set's sample_results file

    :return: The fully qualified path to the industrial data-set's sample_results file
    :rtype: string
    """
    return fetch_file_paths(FILE_PATTERN_RESULTS_FILES, [_TEST_DATA_DIR, _INDUSTRIAL_DATA_DIR, _CNTRLLR_RESULTS_DIR])[0]


def get_industrial_data_files():
    """
    Get the array of file paths to industrial closed-loop controller data-files

    :return: A list of file paths
    :rtype: list
    """

    return fetch_file_paths(FILE_PATTERN_DATA_FILES, [_TEST_DATA_DIR, _INDUSTRIAL_DATA_DIR, _CNTRLLR_DATA_DIR])


def get_industrial_config_files(data_file_path_arr):
    """
    Get the array of file paths to industrial closed-loop controller configuration files in the same order
    of the corresponding data-files

    :param data_file_path_arr: The array of file-paths of the industrial closed-loop controller data-files
    :type data_file_path_arr: list

    :return: A list of file paths
    :rtype: list
    """

    return fetch_corresponding_configs(data_file_path_arr, [_TEST_DATA_DIR, _INDUSTRIAL_DATA_DIR, _CNTRLLR_CONFIG_DIR],
                                       FILE_PATTERN_CONFIG_FILES)


def get_cntrllr_ids(data_file_path_arr):
    """
    Get the array of controller-identifiers (i.e. names) in the same order of the corresponding data-files

    :param data_file_path_arr: The array of file-paths of the industrial closed-loop controller data-files
    :type data_file_path_arr: list

    :return: A list of controller names
    :rtype: list
    """
    return [pathlib.PurePath(file_path).stem for file_path in data_file_path_arr]


# ADDING FUNCTIONS FOR TESTIN SIMULATED DATA
def get_simulated_results_file():
    """
    Get the path to the simulated data-set's sample_results file

    :return: The fully qualified path to the simulated data-set's sample_results file
    :rtype: string
    """
    return fetch_file_paths(FILE_PATTERN_RESULTS_FILES, [_TEST_DATA_DIR, _SIMULATED_DATA_DIR, _CNTRLLR_RESULTS_DIR])[0]


def get_simulated_data_files():
    """
    Get the array of file paths to simulated closed-loop controller data-files

    :return: A list of file paths
    :rtype: list
    """

    return fetch_file_paths(FILE_PATTERN_DATA_FILES, [_TEST_DATA_DIR, _SIMULATED_DATA_DIR, _CNTRLLR_DATA_DIR])


def get_simulated_config_files(data_file_path_arr):
    """
    Get the array of file paths to simulated closed-loop controller configuration files in the same order
    of the corresponding data-files

    :param data_file_path_arr: The array of file-paths of the simulated closed-loop controller data-files
    :type data_file_path_arr: list

    :return: A list of file paths
    :rtype: list
    """

    return fetch_corresponding_configs(data_file_path_arr, [_TEST_DATA_DIR, _SIMULATED_DATA_DIR, _CNTRLLR_CONFIG_DIR],
                                       FILE_PATTERN_CONFIG_FILES)
