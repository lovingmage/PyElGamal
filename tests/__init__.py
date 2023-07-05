"""
Tests for PyElGamal Package

Author: Chenghong Wang
Email: cw374@duke.edu

This package contains the unit tests for the PyElGamal package, which implements the ElGamal encryption scheme.
The tests cover the functionality of the Elliptic Curve ElGamal implementation, vectorized operations, and the RFC 3526 ElGamal implementation.
"""

import unittest
from .test_ec_elgamal import *
from .test_vector_ec_elgamal import *
from .test_rfc3526_elgamal import *

if __name__ == '__main__':
    unittest.main()
