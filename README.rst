say Hi Tempest Plugin (Out-of-Tree)
=========

Having simple say hi python package.

Create an independent python package to host a tempest plugin with integration test cases.

Plugin implementation will allow to run integration test cases via testr or ostestr test runners along with tempest suites.

Changes from sayHi_tempest_plugin(In-Tree):

* Utilize pbr at setup.py
* Utilize setup.cfg - host package information and entry points.
* Utilize variables from config.py

Package Structure

.. code-block:: bash

  say_hi_tempest_plugin_outtree
  ├── demo_tempest_plugin
  │   ├── config.py                     <─ Configuration Options to be register
  │   ├── __init__.py
  │   ├── plugin.py                     <─ Actual tempest plugin, Registration method of options and groups
  │   └── tests                         <─ Integration Test Cases for the program
  │       ├── api                       ──┐
  │       │   ├── base.py                 │
  │       │   ├── __init__.py             │── Integration Test Cases(optional structure)
  │       │   └── test_int_sayhi.py       │
  │       ├── scenario                    │
  │       └── __init__.py               ──┘ 
  ├── LICENSE
  ├── README.rst
  ├── requirements.txt
  └── setup.cfg                          <─ Added Tempest entry point
  └── setup.py                           <─ Use pbr


Installation
----

To install Tempest

.. code-block:: bash

  $ git clone https://github.com/openstack/tempest/
  $ pip install tempest/

To install say hi plugin

.. code-block:: bash

  $ git clone https://github.com/dlux/sayHi_Package.git
  $ pip install sayHi_Package/

Initialize Tempest

.. code-block:: bash

  # Initialize Tempest
  $ cd tempest
  $ testr init

Run Test Suite
------

Validate Tempest discovered plugin TCs

.. code-block:: bash

  $ testr list-tests | grep -i say

  2016-06-16 18:08:17.242 5732 INFO tempest [-] Using tempest config file
  /etc/tempest/tempest.conf 
  demo_tempest_plugin.tests.api.test_sayhi.TestSayHi.test_hi[smoke]

Run test cases

.. code-block:: bash

  $ ostestr -r demo_tempest_plugin.tests.api.test_sayhi.TestSayHi.test_hi

.. code-block:: bash

  $ testr run demo_tempest_plugin.tests.api.test_sayhi.TestSayHi.test_hi

.. code-block:: bash

  $ testr run --subunit smoke | subunit-1to2 | subunit-trace --color -n

.. code-block:: bash

  $ ./tempest/run_tempest.sh demo_tempest_plugin.tests.api.test_sayhi.TestSayHi.test_hi -N

Other Resources
------

Run say hi program

.. code-block:: bash

  $ dluxsay
  Hello Stranger

  # with parameters
  $ dluxsay Luz
  Hi Luz

Resources

http://docs.openstack.org/developer/tempest/plugin.html

http://docs.openstack.org/developer/oslo.config/cfg.html

http://specs.openstack.org/openstack/qa-specs/specs/tempest/tempest-external-plugin-interface.html
