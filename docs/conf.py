# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
from unittest.mock import Mock


sys.path.insert(0, os.path.abspath('../sphero_bolt_control/scripts'))
sys.path.insert(0, os.path.abspath('../sphero_bolt_driver/scripts'))
sys.path.insert(0, os.path.abspath('../spherov2.py'))

# Mock the rospy module and any other ROS-related modules
MOCK_MODULES = ['rospy', 'sensor_msgs', 'std_msgs', 'geometry_msgs', 'geometry_msgs.msg' , 
                'std_msgs.msg' , 'tf', 'sensor_msgs.msg', 'rospy.msg', 'rospy.rostime', 'rospy.timer' ]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
]

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'demo-iridia-swarm-robotics'
copyright = '2024, Florian Noussa Yao'
author = 'David Garzón Ramos \n Siméon Michel \n Florian Noussa Yao'
release = '0.0.1'
version = '0.0.1'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'sphinx_rtd_theme'