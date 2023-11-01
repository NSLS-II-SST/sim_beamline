from setuptools import setup,  find_packages

setup(
    author="Charles Titus",
    author_email="charles.titus@nist.gov",
    install_requires=["caproto", "asyncio", "scipy", "sst_base",
                      "sst_funcs", "numpy"],
    name="simline",
    packages=find_packages(),
    entry_points={'console_scripts': ['simline = simline.sim_sst:start']},
)
