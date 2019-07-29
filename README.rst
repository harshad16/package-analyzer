Thoth Package Analyzer
---------------------

A tool for gathering digests of packages and files present inside packages for various ecosystems.

Gathering digests of packages
=============================

The tool downloads all distributions for published platforms for a given ``package_name`` and a specific ``package_version`` from a given ``index_url``. It extracts all files from the packages, calculates checksums for them and provides a structured output of files and checksums.

The result of this project is used in `Thoth project <https://thoth-station.ninja>`_ to check provenance that the images analyzed by `Package Extract <https://github.com/thoth-station/package-extract>`_ contain valid python packages installed from authentic sources such as `AICoE <https://tensorflow.pypi.thoth-station.ninja>`_, `PyPI <https://pypi.org/>`_. 


Example of gathering digests
============================

An example of gathering digests for ``tensorflow v0.12.0rc0``:

.. code-block:: console

  $ pipenv install --dev
  $ PYTHONPATH=. pipenv run python3 ./thoth-package-analyzer python -p tensorflow -v 0.12.0rc0 -i https://pypi.org/simple

.. code-block:: json

  {
    "metadata": {
      "analyzer": "thoth-package-analyzer",
      "analyzer_version": "0.1.0",
      "arguments": {
        "python": {
          "index_url": "https://pypi.org/simple",
          "no_pretty": false,
          "output": "http://result-api/api/v1/package-analysis-result",
          "package_name": "tensorflow",
          "package_version": "0.12.0rc0"
        },
        "thoth-package-analyzer": {
          "verbose": false
        }
      },
      "datetime": "2019-07-26T18:25:52.026665",
      "distribution": {
        "codename": "Core",
        "id": "centos",
        "like": "rhel fedora",
        "version": "7",
        "version_parts": {
          "build_number": "",
          "major": "7",
          "minor": ""
        }
      },
      "hostname": "package-analyzer-838e1a21f149d7e1-f5dbh",
      "python": {
        "api_version": 1013,
        "implementation_name": "cpython",
        "major": 3,
        "micro": 3,
        "minor": 6,
        "releaselevel": "final",
        "serial": 0
      },
      "timestamp": 1564165552
    },
    "result": {
      "https://pypi.org/simple": {
        "files": [
          {
            "digests": [
              {
                "filepath": "tensorflow-0.12.0rc0.data/purelib/external/__init__.py",
                "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
              },
              ...,
              {
                "filepath": "tensorflow-0.12.0rc0.data/purelib/external/boringssl/src/crypto/aes/internal.h",
                "sha256": "303e235a89468d8719672792d19b2c80dd48d9d7c09e5620fdd0e6f3111415e8"
              }
            ],
            "name": "tensorflow-0.12.0rc0-cp27-cp27m-macosx_10_11_x86_64.whl",
            "sha256": "feaf06c7df5c0a480654bf1f38dd4d3b809c7315502a7d9f295033f9d2bd9b13"
          },
          ...,
          {
            "digests": [
              {
                "filepath": "tensorflow-0.12.0rc0.data/purelib/tensorflow/__init__.py",
                "sha256": "14e7778e70d208cb35a9f8da286005edd57d43f3f465e8a27c503be3956d038c"
              },
              ...,
              {
                "filepath": "tensorflow-0.12.0rc0.data/purelib/tensorflow/models/__init__.py",
                "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
              },
            ],
            "name": "tensorflow-0.12.0rc0-cp27-cp27mu-manylinux1_x86_64.whl",
            "sha256": "d4b6ca2cacb64513350c1544c33a6e9493073f928398407d20ba018d991fb28e"
          }
        ],
        "index_url": "https://pypi.org/simple",
        "package_name": "tensorflow",
        "package_version": "0.12.0rc0"
      }
    }
  }