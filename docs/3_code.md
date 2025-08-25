# Open Source

[![github_sma2.svg](./assets/badges/github_sma2.svg)](https://github.com/smarie)

While most of my coding time is devoted to internal Schneider Electric software, I maintain some open source 
activity focused on addressing "common" transverse issues. Quality is "best effort given the allocated time".

## Footprint

Below is the number of packages downloads for my python codes, in million of downloads per year:

```plotly
{"file_path": "./assets/plotly/YearlyTotalsDetails.json"}
```

I also contribute to other's codes. Below is an attempt to present both activities.

!!! warning "Disclaimer"
    The distinction below between "significant" and "other" contributions should be understood as "my own perception of 
    the impact of my work", and by no means any sort of judgement about the quality of the projects cited below.

## Significant contributions

### Author

- [`m5py`](https://smarie.github.io/python-m5p/) `scikit-learn`-compliant M5 prime (M5’) model trees for python, 2022
  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10552219.svg)](https://doi.org/10.5281/zenodo.10552219)
  [![Downloads](https://pepy.tech/badge/m5py)](https://pepy.tech/project/m5py)
  [![Downloads per week](https://pepy.tech/badge/m5py/week)](https://pepy.tech/project/m5py)  
  *Publication: [PyConDE PyData 2022](2_publications.md#pyconde22)*
- [`mkdocs-gallery`](https://smarie.github.io/mkdocs-gallery) bringing all features of the great sphinx-gallery on mkdocs, 2021 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5786851.svg)](https://doi.org/10.5281/zenodo.5786851)
  [![Downloads](https://pepy.tech/badge/mkdocs-gallery)](https://pepy.tech/project/mkdocs-gallery)
  [![Downloads per week](https://pepy.tech/badge/mkdocs-gallery/week)](https://pepy.tech/project/mkdocs-gallery)
- [`qdscreen`](https://python-qds.github.io/qdscreen/) a python implementation of the quasi-determinism screening algorithm, 2021 [![Downloads](https://pepy.tech/badge/qdscreen)](https://pepy.tech/project/qdscreen)
  [![Downloads per week](https://pepy.tech/badge/qdscreen/week)](https://pepy.tech/project/qdscreen)  
  *Publication: [ECML PKDD 2022](2_publications.md#ecml22)*
- [`odsclient`](https://smarie.github.io/python-odsclient/), a non-official python client for opendatasoft API (e.g. datasets retrieval for benchmarks), 2020
  [![Downloads](https://pepy.tech/badge/odsclient)](https://pepy.tech/project/odsclient)
  [![Downloads per week](https://pepy.tech/badge/odsclient/week)](https://pepy.tech/project/odsclient)
- [`pyfields`](https://smarie.github.io/python-pyfields/), eases object-oriented python with easy and user-friendly type and value validation, 2019 [![Downloads](https://pepy.tech/badge/pyfields)](https://pepy.tech/project/pyfields)
  [![Downloads per week](https://pepy.tech/badge/pyfields/week)](https://pepy.tech/project/pyfields)
- [`pytest-cases`](https://smarie.github.io/python-pytest-cases/), to separate test cases from test functions for benchmarks, 2018 
  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3937829.svg)](https://doi.org/10.5281/zenodo.3937829)
  [![Downloads](https://pepy.tech/badge/pytest-cases)](https://pepy.tech/project/pytest-cases)
  [![Downloads per week](https://pepy.tech/badge/pytest-cases/week)](https://pepy.tech/project/pytest-cases)  
  *Publication: [Europython 2021](2_publications.md#europy21)*
- [`pytest-harvest`](https://smarie.github.io/python-pytest-harvest/), a `pytest` extension to generate reproducible tests/benchmark result tables easily,2018
  [![Downloads](https://pepy.tech/badge/pytest-harvest)](https://pepy.tech/project/pytest-harvest)
  [![Downloads per week](https://pepy.tech/badge/pytest-harvest/week)](https://pepy.tech/project/pytest-harvest)
- [`autoclass`](https://smarie.github.io/python-autoclass/), removes boilerplate code from python classes, 2017
  [![Downloads](https://pepy.tech/badge/autoclass)](https://pepy.tech/project/autoclass)
  [![Downloads per week](https://pepy.tech/badge/autoclass/week)](https://pepy.tech/project/autoclass)
- [`azmlclient`](https://smarie.github.io/python-azureml-client/), a non-official python client for AzureML API (e.g. analytics web services), 2016
  [![Downloads](https://pepy.tech/badge/azmlclient)](https://pepy.tech/project/azmlclient)
  [![Downloads per week](https://pepy.tech/badge/azmlclient/week)](https://pepy.tech/project/azmlclient)
- [`octminer`](https://github.com/smarie/java-octminer), an interface between Rapidminer and Octave to execute Octave code within Rapidminer processes, 2012.  
  *Publication: [RCOMM 2012](2_publications.md#rcomm12)*
- [`xml-java-osgi`](https://github.com/smarie/java-xml-osgi), a stack of packaged xml bundles with small footprint for embedded OSGi, 2009
- [`osgi-dpwsdriver`](https://github.com/smarie/java-osgi-dpwsdriver), a dpws (Devices Profile for Web Services) driver for OSGi compliant with RFP 86, 2007  
  *Publications: [OSGi Alliance 2007](2_publications.md#osgicom07), [RFP 86](2_publications.md#osgirfp08) , [RFC08](2_publications.md#osgirfc08). 
  Also used in [AINA 2008](https://doi.org/10.1109/AINA.2008.14), [ICMDM 2011](https://doi.org/10.1109/MDM.2011.47)...*

### Contributor

- [`pandas`](https://github.com/pandas-dev/pandas/pull/51459), significantly improved performance of `Period`'s default formatter, 2023
- [`pandas`](https://github.com/pandas-dev/pandas/pull/53003), added tests for `Period` str and repr, 2023
- [`pandas`](https://github.com/pandas-dev/pandas/pull/46405), fixed non-utf8 locale-related `Period` formatting issue, 2022
- [`pandas`](https://github.com/pandas-dev/pandas/pull/47570), fixed locale-related issue in the testing tools, 2022
- [`pandas`](https://github.com/pandas-dev/pandas/pull/46759), improved performance for date/time formatting and SQL time inserts, 2022
- [`pandas`](https://github.com/pandas-dev/pandas/pull/46361), fixed `Period` and `PeriodIndex` formatting, 2022
- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/17266), improved R² and explained variance 
  scores through a new `force_finite` parameter, 2022
- [`pandas`](https://github.com/pandas-dev/pandas/pull/42494), improved documentation for `to_datetime` – in particular about timezone handling, 2022
- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/12069), added a new randomized SVD solver to `KernelPCA`, 2021
- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/18149), fixed `KernelPCA`'s numerical consistency between 32-64bits, 2020
- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/13511), fixed pseudo-random number generator for `libsvm` and `liblinear`, 2020
- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/12145), added checks for eigenvalue decomposition numerical/conditioning issues in `KernelPCA`, 2019
- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/12143), fixed transform issue in `KernelPCA` when zero eigenvalues are present and not removed, 2019
- [`MATLAB`](https://www.mathworks.com/help/matlab/data_analysis/time-series-objects.html), fixed 3 bugs in `R2009` time series toolbox (Rounding and conversion errors in several functions), 2010
- [`wsman-osgi`](https://github.com/smarie/java-wsman-osgi), a Java OSGI implementation of the DMTF WS-Management specification, 2008
- [`dpws4j`](https://forge.soa4d.org/projects/dpws4j/), a dpws (Devices Profile for Web Services) driver for java, various contributions, 2007

### Coach

- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/31247) faster eigendecomposition for Isomap & 
  KernelPCA, 2025 (under finalization)
  {: #eigsh25 }
- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/31227) replacement of the Yeo-Johnson power 
  transformer implementation by scipy’s >= 1.9, 2025
  {: #yeo25 }
- [`scikit-learn`](https://github.com/scikit-learn/scikit-learn/pull/17157), statistical uniformity tests of the new libsvm/liblinear pseudo-random number generator, 2020

## Other contributions

### Author

- [`genbadge`](https://smarie.github.io/python-genbadge/), a code quality badge generator to motivate coders through gamification, 2021
  [![Downloads](https://pepy.tech/badge/genbadge)](https://pepy.tech/project/genbadge)
  [![Downloads per week](https://pepy.tech/badge/genbadge/week)](https://pepy.tech/project/genbadge)
- [`marshmallow-pyfields`](https://smarie.github.io/python-marshmallow-pyfields/), to generate marshmallow schemas from classes using pyfields, 2020
  [![Downloads](https://pepy.tech/badge/marshmallow-pyfields)](https://pepy.tech/project/marshmallow-pyfields)
  [![Downloads per week](https://pepy.tech/badge/marshmallow-pyfields/week)](https://pepy.tech/project/marshmallow-pyfields)
- [`doit-api`](https://smarie.github.io/python-doit-api/), a pythonic API for doit, 2020
  [![Downloads](https://pepy.tech/badge/doit-api)](https://pepy.tech/project/doit-api)
  [![Downloads per week](https://pepy.tech/badge/doit-api/week)](https://pepy.tech/project/doit-api)
- [`vtypes`](https://smarie.github.io/python-vtypes/), validating types for python: isinstance() validates both type and value, 2020
  [![Downloads](https://pepy.tech/badge/vtypes)](https://pepy.tech/project/vtypes)
  [![Downloads per week](https://pepy.tech/badge/vtypes/week)](https://pepy.tech/project/vtypes)
- [`pytest-pilot`](https://smarie.github.io/python-pytest-pilot/), a pytest extension to slice in a test base more easily (e.g. for large benchmarks), 2019
  [![Downloads](https://pepy.tech/badge/pytest-pilot)](https://pepy.tech/project/pytest-pilot)
  [![Downloads per week](https://pepy.tech/badge/pytest-pilot/week)](https://pepy.tech/project/pytest-pilot)
- [`fprules`](https://smarie.github.io/python-fprules/), make-like file pattern rules for build tools such as doit, 2019
  [![Downloads](https://pepy.tech/badge/fprules)](https://pepy.tech/project/fprules)
  [![Downloads per week](https://pepy.tech/badge/fprules/week)](https://pepy.tech/project/fprules)
- [`decopatch`](https://smarie.github.io/python-decopatch/), (labelled “critical” project by PyPi in 2023) python 
  decorators made easy, 2019
  [![Downloads](https://pepy.tech/badge/decopatch)](https://pepy.tech/project/decopatch)
  [![Downloads per week](https://pepy.tech/badge/decopatch/week)](https://pepy.tech/project/decopatch)
- [`makefun`](https://smarie.github.io/python-makefun/), (labelled “critical” project by PyPi in 2022) a toolbox for 
  dynamic functions creation with a given signature, 2019
  [![Downloads](https://pepy.tech/badge/makefun)](https://pepy.tech/project/makefun)
  [![Downloads per week](https://pepy.tech/badge/makefun/week)](https://pepy.tech/project/makefun)
- [`getversion`](https://smarie.github.io/python-getversion/), get the version number of any python module or package, reliably, 2019
  [![Downloads](https://pepy.tech/badge/getversion)](https://pepy.tech/project/getversion)
  [![Downloads per week](https://pepy.tech/badge/getversion/week)](https://pepy.tech/project/getversion)
- [`pytest-steps`](https://smarie.github.io/python-pytest-steps/), a pytest extension to create step-wise / incremental tests in pytest, 2018
  [![Downloads](https://pepy.tech/badge/pytest-steps)](https://pepy.tech/project/pytest-steps)
  [![Downloads per week](https://pepy.tech/badge/pytest-steps/week)](https://pepy.tech/project/pytest-steps)
- [`yamlable`](https://smarie.github.io/python-yamlable/), a thin wrapper of PyYaml to convert python objects to YAML and back., 2018
  [![Downloads](https://pepy.tech/badge/yamlable)](https://pepy.tech/project/yamlable)
  [![Downloads per week](https://pepy.tech/badge/yamlable/week)](https://pepy.tech/project/yamlable)
- [`spawny`](https://smarie.github.io/python-spawny/), a library to help spawning python processes from other places e.g. from MATLAB, 2017
  [![Downloads](https://pepy.tech/badge/spawny)](https://pepy.tech/project/spawny)
  [![Downloads per week](https://pepy.tech/badge/spawny/week)](https://pepy.tech/project/spawny)
- [`mini-lambda`](https://smarie.github.io/python-mini-lambda/), a library to create symbolic single variable expressions (simple lambdas) in python, 2017
  [![Downloads](https://pepy.tech/badge/mini-lambda)](https://pepy.tech/project/mini-lambda)
  [![Downloads per week](https://pepy.tech/badge/mini-lambda/week)](https://pepy.tech/project/mini-lambda)
- [`valid8`](https://smarie.github.io/python-valid8/), a validation toolbox for python, 2017
  [![Downloads](https://pepy.tech/badge/valid8)](https://pepy.tech/project/valid8)
  [![Downloads per week](https://pepy.tech/badge/valid8/week)](https://pepy.tech/project/valid8)
- [`envswitch`](https://smarie.github.io/env-switcher-gui/), a very simple GUI to easily switch between environments, in particular HTTP proxies, 2017
  [![Downloads](https://pepy.tech/badge/envswitch)](https://pepy.tech/project/envswitch)
  [![Downloads per week](https://pepy.tech/badge/envswitch/week)](https://pepy.tech/project/envswitch)
  [![Downloads](https://img.shields.io/github/downloads/smarie/env-switcher-gui/total?label=downloads%20(app))]
  (https://github.com/smarie/env-switcher-gui/releases)
- [`pyqt5-minimal`](https://github.com/smarie/PyQt5-minimal), a minimal version of the PyQt5 GPL package for lightweight distributions, 2017
  [![Downloads](https://img.shields.io/github/downloads/smarie/PyQt5-minimal/total)](https://github.com/smarie/PyQt5-minimal/releases)
- [`parsyfiles`](https://github.com/smarie/python-parsyfiles), a declarative parsing framework in python based on type declarations, 2017
  [![Downloads](https://pepy.tech/badge/parsyfiles)](https://pepy.tech/project/parsyfiles)
  [![Downloads per week](https://pepy.tech/badge/parsyfiles/week)](https://pepy.tech/project/parsyfiles)
- [`commonsjavaosgi`](https://forge.soa4d.org/projects/commonsjavaosgi/), utils for java and OSGi, e.g. exec environments, jsr support for embedded, etc., 2009 

### Contributor

- [`pandera`](https://github.com/unionai-oss/pandera/pull/1538) performance improvement for the check_nullable checker with pandas backend, 2024
- [`mkdocs-bibtex`](https://github.com/shyamd/mkdocs-bibtex/pull/224) added logging, 2024
- [`mkdocs-bibtex`](https://github.com/shyamd/mkdocs-bibtex/pull/222) fixed utf-8 encoding errors with pandoc, 2024
- [`mkdocs`](https://github.com/mkdocs/mkdocs/pull/2807) configuration objects validation improvement, 2022 
- [`pytest-xdist`](https://github.com/pytest-dev/pytest-xdist/pull/766) added non-regression tests for warning serialization across distributed workers, 2022 
- [`requests-oauthlib`](https://github.com/requests/requests-oauthlib/pull/407) fixed an issue where the ssl certificate verification flag was ignored, 2022
- [`requests-oauthlib`](https://github.com/requests/requests-oauthlib/pull/409) fixed an issue where the client scope was not used, 2022
- [`setuptools_scm`](https://github.com/pypa/setuptools_scm/pull/584) support for custom and non-normalizing version processors, 2021
- [`request`](https://github.com/psf/requests/pull/5670) documentation on usage with HTTP(s) proxies, 2020
- [`nox`](https://github.com/theacodes/nox/pull/316) ability to work with no venv_backend, and to better configure default/forced backend (even none), 2020
- [`nox`](https://github.com/theacodes/nox/pull/314) ability to execute an existing conda session when user is offline, 2020
- [`pyLODE`](https://github.com/RDFLib/pyLODE/pull/81) fixed package imports/initialization, 2020 
- [`nox`](https://github.com/theacodes/nox/pull/312) fixed package installation using conda when version constraints are used, 2020
- [`nox`](https://github.com/theacodes/nox/pull/310) fixed default python paths using conda, 2020
- [`oauth-lib`](https://github.com/oauthlib/oauthlib/pull/731) fix authorization token scope inconsistency, 2020  
- [`oauth-lib`](https://github.com/oauthlib/oauthlib/pull/729) fix for default values passing 2, 2020 
- [`oauth-lib`](https://github.com/oauthlib/oauthlib/pull/726) fix for default values passing, 2020 
- [`PyCharm`](https://github.com/JetBrains/intellij-community/pull/1333) fixed autocomplete: added support for descriptors and metaclass members, 2020 
- [`pytest`](https://github.com/pytest-dev/pytest/pull/6939) improved time counters used to compute tests duration, to have more precise durations, 2020 
- [`pytest-xdist`](https://github.com/pytest-dev/pytest-xdist/pull/505) new API to detect worker status in distributed testing., 2020 
- [`typing-inspect`](https://github.com/ilevkivskyi/typing_inspect/pull/56) retro-compatibility with python 3.5.0 and 3.5.1, 2020 
- [`typing-inspect`](https://github.com/ilevkivskyi/typing_inspect/pull/45) retro-compatibility with python 3.5.2 and 3.5.3, 2020 
- [`attrs`](https://github.com/python-attrs/attrs/pull/590) fix for a bug happening in an edge case, 2020 
- [`funcsigs`](https://github.com/testing-cabal/funcsigs/pull/37) retrocompatibility: added support for `follow_wrapped` (aligned with latest python versions), 2020 
- [`pytest-profile`](https://github.com/man-group/pytest-plugins/pull/99) fixed SVG profiling report on windows, 2019 
- [`stdlib-list`](https://github.com/jackmaney/python-stdlib-list/pull/23) new API to check if a module is part of stdlib, 2019 
- [`typing-inspect`](https://github.com/ilevkivskyi/typing_inspect/pull/26) new API to check if a type is optional, and type variable helpers, 2018 
- [`enforce`](https://github.com/RussBaz/enforce/pull/65) various type-based validation improvements, 2018 
- [`decorator`](https://github.com/micheles/decorator/pull/57) added support for generators, 2018 
- [`blync4CI`](https://github.com/shazz/blync4CI/pull/1) added support for multiple lights, and various improvements, 2016 
- [`windows-azure-storage-plugin`](https://github.com/jenkinsci/windows-azure-storage-plugin) various usability improvements, 2015 
- [`ws-management4j`](https://forge.soa4d.org/projects/ws-management4j/) a Java implementation of DMTF's WS-Management standard for dpws4j, 2008 
- [`ws-sec4j`](https://forge.soa4d.org/projects/wssec4j/) implementation of the WS-Security standard for dpws4j, 2007
